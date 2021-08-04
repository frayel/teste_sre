# Teste SRE Arquiteto
O teste consiste em 2 microserviços que possibilitam realizar uma consulta entre um médico e um paciente e 
gerar uma entrada financeira de cobrança da consulta.  

Realizado em Agosto/2021 por Felipe Rayel <felipe.rayel@gmail.com>

## Solução
O sistema está distribuído em 3 containers: API Consulta, API Financeira e DB Postgresql.

Dentro do container da API de consulta, também roda o scheduler que irá consumir a fila de 
processamento.

Na fila de processamento estão as pendências de pagamento que devem ser enviadas à api de finanças. 
Este scheduler está programado para ler a fila a cada 5 segundos e caso a api de finanças não
esteja disponível, o sistema continuará tentando realizar o envio.

As pendências de pagamento são alimentadas pelo serviço de término de consulta, que gera um registro
assim que a consulta é encerrada.


## Estrutura
```
├─── api                
│    ├─── config       Arquivo de configuração de negocio. Ex: Preço da consulta
│    ├─── dto          Objetos para transferencia de dados entre camadas
│    ├─── exceptions   Classe de exceções customizadas
│    ├─── models       Entidades de dados relacionais (database models)
│    ├─── repository   Camada de persistência
│    ├─── service      Camada de serviço 
│    │    └── remote   Serviço de integração a APIs externas (ex: financeiro) 
│    ├─── tests        Testes automatizados
│    └─── views        Camada de exposição dos serviços (endpoints)
└─── consultation         
     ├─── settings.py      Arquivo de configuração global
     └─── settings-prd.py  Arquivo de configuração quando estiver dodando em container
```    

 
## Autenticação
Para autenticar nas apis deve-se usar o modo Basic (username: admin, password: teste123)  

## Banco de dados
Estando rodando no docker, o banco de dados usado é o postgresql. 
Rodando em ambiente de desenvolvimento, usará o banco sqlite3.
Foram usadas 3 tabelas:
- consultation: Registra as consultas pela API de consultas.
- pending_payment: Registra uma pendência de processamento ao término de uma consulta.
- payment: Registra a entrada no sistema financeiro pela API de finanças.

Para simplificação, nao foram criados registros para médico e paciente. Portanto, o sistema não irá
validar se o código existe em cadastro.

Dados para conexão no postgresql:

```
ip: 127.0.0.1:5432
db: postgres
username: postgres
password: pg123
```  
 
## Serviço de Consulta
O serviço é responsável por iniciar e encerrar uma consulta e possui 2 endpoints:  
- app/consultation/start - Realiza o registro do inicio de uma consulta  
- app/consultation/finish - Realiza o registro de término de uma consulta e 
faz o envio da entrada no sistema financeiro de modo assíncrono.     

Scheduler:  
* Verifica a cada 5 segundos se existem pendências de entrada financeira a serem processadas.  
Se existir, realiza a chamada da API financeira para registro.  
Em caso de erro ou indisponibilidade, o sistema continuará tentando até conseguir, registrando o número de tentativas.  
	
## Serviço de Finanças	
O serviço é responsável por registrar a entrada financeira de uma consulta. Possui 1 endpoint:  
* app/finance/record - Realiza o registro de uma entrada financeira  

## Containers Docker

### Para criar os containers:
```bash
$> docker build -t app_consulta app_consulta
$> docker build -t app_financas app_financas
```
ou executar docker_build.bat  

### Para criar a rede e executar os containers:
```bash
$> docker network create --subnet=172.18.0.0/16 rede_teste  
$> docker run --net rede_teste --ip 172.18.0.2 --name postgres -e "POSTGRES_PASSWORD=pg123" -p 5432:5432 -d postgres  
$> docker run --net rede_teste --ip 172.18.0.3 -it -p 8010:8010 --name app_consulta -d app_consulta  
$> docker run --net rede_teste --ip 172.18.0.4 -it -p 8020:8020 --name app_financas -d app_financas 
```
ou executar docker_run.bat  

## Ambiente de Desenvolvimento 
Para rodar o ambiente de desenvolvimento localmente:
```bash
$> cd app_consulta/consultation
$> python manage.py migrate
$> python manage.py loaddata initial_data
$> python manage.py runserver 8000
```
```bash
$> cd app_financas/finance
$> python manage.py migrate
$> python manage.py loaddata initial_data
$> python manage.py runserver 8001
```
OBS: As configurações usadas em desenvolvimento ficam no settings.py e quando estão no container são lidas do arquivo settings-prd.py 

## Realizando chamadas

Executar o script teste_api.py para iniciar e encerrar uma consulta
ou realizar as chamadas através de um cliente http:
    
### Registrando o início da consulta:
 
```
POST http://localhost:8010/app/consultation/start/

HEADER 
content-type: application/json
authorization: Basic YWRtaW46dGVzdGUxMjM=
    
BODY
{
    "physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82",
    "patient_id": "86158d46-ce33-4e3d-a822-462bbff5782f"
}
```

### Registrando o término da consulta:
```
PUT http://localhost:8010/app/consultation/finish/

HEADER 
content-type: application/json
authorization: Basic YWRtaW46dGVzdGUxMjM=

BODY
{
    "consultation_id": "25b1b0e4-23cd-4764-ad3d-ac7fcbb76f5a",
    "end_date": "2021-08-02T12:00:00"
}
```    
* A data de término é opcional e será usada a data e hora atual caso não seja informada.
* O registro na API financeira é feito automaticamente pelo sistema de modo assíncrono.

