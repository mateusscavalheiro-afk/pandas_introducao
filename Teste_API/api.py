import requests

# URL local gerada pelo Flask
url = "http://127.0.0.1:5000/sensores"

dados = {"temperatura": 70, "pressao": 2.1}

resposta = requests.post(url, json=dados)

if resposta.status_code in (200, 201):
    print("Dados enviados com sucesso!")
    print("Resposta do servidor:", resposta.json())
else:
    print(f"Erro no envio: {resposta.status_code}")