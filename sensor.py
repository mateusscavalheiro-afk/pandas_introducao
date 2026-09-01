import random
import time

def lersensor():
    temp = round(random.uniform(-20, 150), 2)
    press = round(random.uniform(1, 8), 2)

    print("\n")
    print("-" * 120)

    print(f"Leitura {i+1} - Temperatura: {temp}ºC | Pressão: {press} atm")

    time.sleep(1.2)

    if 0 <= temp <= 100:
        print("ERRO! TEMP. IRREGULAR")
    else:
        print("OK")

    time.sleep(1.2)

    if press > 5:
        print("ERRO! PRESS. IRREGULAR")
    else:
        print("OK")

    print("-" * 120)

    time.sleep(1.2)

print("-" * 60)
time.sleep(1.5)
print("Simulação de telemetria de sensor")
time.sleep(2)

for i in range(5):  
    lersensor()