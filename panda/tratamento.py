import pandas as pd

dados = pd.read_csv("dados_sensores.csv")

media_temp = dados["temperatura"].mean()

print("Temperatura média: ",round(media_temp,2),"°C")

print("-" * 120)

max_press= dados["pressao"].max()

print("A maior pressão registrada foi de: ",round(max_press,2),"bar")

print("-" * 120)

min_prod = dados["producao"].min()

print("A menor produção foi de: ",min_prod)

print("-" * 120)

dados_ordenados = dados.sort_values(by="producao", ascending=False)

print("Ordenação por produção (maior para menor)")

print("\n")
print(dados_ordenados)

print("-" * 120)