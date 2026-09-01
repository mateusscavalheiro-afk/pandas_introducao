import pandas as pd
import sqlite3

conn = sqlite3.connect('fabrica.db')

cursor = conn.cursor()

dados = pd.read_csv("dados_sensores.csv")

dados.to_sql("dados_sensores", conn, if_exists="replace", index=False)

print("Dados do CSV exportados para o 'fabrica.db' com sucesso!")
print("-" * 120)

cursor.execute("SELECT * FROM dados_sensores")

print("-" * 120)

query = """
INSERT INTO dados_sensores (timestamp, temperatura, pressao, producao)
VALUES (?, ?, ?, ?)
"""
valores = ("12:00", 12, 12, 12)

cursor.execute(query, valores)

conn.commit()

print("Registro inserido com sucesso!")
cursor.execute("SELECT * FROM dados_sensores")
dados = cursor.fetchall()
print(dados)