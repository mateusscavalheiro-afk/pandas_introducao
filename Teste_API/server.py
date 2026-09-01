from flask import Flask, render_template_string, request

app = Flask(__name__)

# Lista para armazenar a leitura do sensor em memória
leituras = []


@app.route("/", methods=["GET"])
def pagina_html():
    # Estrutura básica HTML que renderiza os dados recebidos
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Monitor de Sensores</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            table { border-collapse: collapse; width: 300px; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background-color: #f4f4f4; }
        </style>
    </head>
    <body>
        <h2>Últimas Leituras de Sensores</h2>
        <table>
            <tr>
                <th>Temperatura</th>
                <th>Pressão</th>
            </tr>
            {% for item in leituras %}
            <tr>
                <td>{{ item.temperatura }} °C</td>
                <td>{{ item.pressao }} atm</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, leituras=leituras)


@app.route("/sensores", methods=["POST"])
def receber_dados():
    dados = request.get_json()
    leituras.append(dados)
    return {"status": "sucesso", "mensagem": "Dados armazenados com sucesso!"}, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)