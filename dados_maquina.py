import csv
import random

with open("dados_sensores.csv","w",newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["timestamp","temperatura","pressao","producao"])

    for i in range(20):
        temp = round(random.uniform(20, 120), 2)
        press = round(random.uniform(1, 8), 2)
        producao = round(random.uniform(0,250))
        h = random.randint(0, 23)
        m = random.randint(0, 59)
        s = random.randint(0, 59)
        timestamp = f"{h:02d}:{m:02d}:{s:02d}"

        writer.writerow([timestamp,  temp,  press,  producao])

print("Dados salvos!")