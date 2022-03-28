import pyautogui as pg
import time, random

dni, edad, numAf = list(), list(), list();

for i in range(1000):
    ndni = random.randint(00000000, 99999999)
    while len(str(ndni)) != 8:
        ndni = random.randint(00000000, 99999999)
    nedad = random.randint(6, 120)
    nnumAf = random.randint(0, 999999)
    
    dni.append(ndni)
    edad.append(nedad)
    numAf.append(nnumAf)
    

letras = ["T","R", "W", "A", "G","M", "Y","F","P","D","X","B","N", "J", "Z","S","Q", "V","H","L", "C","K","E"]
for num in range(1000):
    letra = dni[num] % 23
    nuevo = str(dni[num]) + letras[letra]
    dni[num] = nuevo
    
for i in range(1000):
    pg.write(f'insert into aficionado values ("{dni[i]}", {edad[i]}, "{numAf[i]}");')
    time.sleep(0.1)
    pg.press('enter')
    