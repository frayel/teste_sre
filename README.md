docker network create --subnet=172.18.0.0/16 rede_teste  
docker run --net rede_teste --ip 172.18.0.2 --name postgres -e "POSTGRES_PASSWORD=pg123" -p 5432:5432 -d postgres  
docker build -t app_consulta app_consulta  
docker build -t app_financeiro app_financeiro  
docker run --net rede_teste --ip 172.18.0.3 -it -p 8010:8010 --name app_consulta -d app_consulta  
docker run --net rede_teste --ip 172.18.0.4 -it -p 8020:8020 --name app_financeiro -d app_financeiro  