import random
import time

def lersensor():
    temp = round(random.uniform(20, 120), 2)
    press = round(random.uniform(1, 8), 2)

    print("\n")
    print("-" * 120)

    print(f"Leitura {i+1} - Temperatura: {temp}ºC | Pressão: {press} atm")

    time.sleep(1.2)

    if temp > 80:
        print("ALERTA! TEMPERATURA ALTA")
    else:
        print("Normar")

    time.sleep(1.2)

    if press > 5:
        print("ALERTA! PRESSÃO ALTA")
    else:
        print("Tudo normar")

    print("-" * 120)

    time.sleep(1.2)

print("-" * 60)
time.sleep(1.5)
print("Simulação de telemtria de sensor")
time.sleep(2)

for i in range(5):  
    lersensor()