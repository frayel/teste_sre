@echo off
docker stop postgres app_consulta app_financas
docker rm app_consulta app_financas postgres
docker rmi app_consulta app_financas postgres 
docker volume prune
