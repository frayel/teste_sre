import json
import uuid
from base64 import b64encode
import requests

""" 
    Script de teste da API
    Este script irá criar uma consulta com dados aleatorios e em seguida irá finaliza-la
    Para rodar este script nao é necessário nenhuma dependencia do projeto e basta executar:
    python teste_api.py 
"""

username = "admin"
password = "teste123"
endpoint_start = "http://localhost:8010/app/consultation/start/"
endpoint_finish = "http://localhost:8010/app/consultation/finish/"


def main():
    for i in range(1, 50):
        consulta = criar_consulta()
        encerrar_consulta(consulta)


def encerrar_consulta(consulta):
    headers = get_headers()
    data = {
        "consultation_id": consulta["id"],
    }
    response = requests.put(endpoint_finish, json=data, headers=headers, timeout=10)
    response.raise_for_status()
    print(f"Consulta {consulta['id']} encerrada.")


def criar_consulta():
    headers = get_headers()
    data = {
        "physician_id": str(uuid.uuid4()),
        "patient_id": str(uuid.uuid4()),
    }
    response = requests.post(endpoint_start, json=data, headers=headers, timeout=10)
    response.raise_for_status()
    consulta = response.json()
    print(f"Consulta {consulta['id']} criada.")
    return consulta


def get_headers():
    user_pass = b64encode(f"{username}:{password}".encode()).decode("ascii")
    headers = {'Authorization': f"Basic {user_pass}"}
    return headers


if __name__ == "__main__":
    main()

