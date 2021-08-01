# iClinic Teste SRE Arquiteto
O teste consiste em 2 microserviços que possibilitam realizar uma consulta entre um médico e um paciente e gerar uma entrada financeira de cobrança da consulta.  

## Solução
O sistema está distribuido em 3 containers: API Consulta, API Financeira e DB Postgresql.  
 
## Autenticação
	Para autenticar nas apis deve-se usar o modo Basic (username: admin, password: teste123)  
	Se necessario conectar na base de dados: ip: 172.18.0.2:5432, db: postgres, username: postgres, password: pg123  
 
## API Consulta
	* Possui 2 endpoints:  
	app/consultation/start - Realiza o registro do inicio de uma consulta  
	app/consultation/finish - Realiza o registro de termino de uma consulta e realiza o registro de uma pendencia de entrada financeira.  
	* Scheduler:  
	Verifica a cada 5 segundos se existem pendencias de entrada financeira a serem processados.  
	Se existir, realiza a chamada da API financeira para registro.  
	Em caso de erro ou indisponibilidade, o sistema continuará tentando até conseguir, registrando o numero de tentativas.  
	
## API Financeira	
	* Possui 1 endpoint:  
	app/finance/record - Realiza o registro de uma entrada financeira  

## Para criar os containers docker:
	cd app_consulta
	docker build -t app_consulta app_consulta  
	cd app_financeiro
	docker build -t app_financeiro app_financeiro  

## Para subir os containers:
	docker network create --subnet=172.18.0.0/16 rede_teste  
	docker run --net rede_teste --ip 172.18.0.2 --name postgres -e "POSTGRES_PASSWORD=pg123" -p 5432:5432 -d postgres  
	docker run --net rede_teste --ip 172.18.0.3 -it -p 8010:8010 --name app_consulta -d app_consulta  
	docker run --net rede_teste --ip 172.18.0.4 -it -p 8020:8020 --name app_financeiro -d app_financeiro  

## Registrando o início da consulta:
	POST http://172.18.0.4/app/consultation/start/
	HEADER 
		content-type: application/json
		authorization: Basic YWRtaW46dGVzdGUxMjM=
	BODY
		{
			"physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82",
			"patient_id": "86158d46-ce33-4e3d-a822-462bbff5782f"
		}
	
## Registrando o término da consulta:
	POST http://172.18.0.4/app/consultation/finish/
	HEADER 
		content-type: application/json
		authorization: Basic YWRtaW46dGVzdGUxMjM=
	BODY
		{
			"consultation_id": "25b1b0e4-23cd-4764-ad3d-ac7fcbb76f5a"
		}
	
	* O registro na API financeira é feito automaticamente pelo sistema