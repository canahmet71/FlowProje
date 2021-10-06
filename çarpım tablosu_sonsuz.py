import random
import time

sacarpan = 1

while True:

    carpilan = random.randint(1, 10)
    carpan = random.randint(1, 10)

    print(f"{carpilan} sayısı {carpan} a kadar çarpılıyor")

    while sacarpan < carpan:
        cevap = carpilan * sacarpan
        print(f"{carpilan} * {sacarpan} = {cevap}")
        sacarpan += 1
        time.sleep(0.37)

    sacarpan = 1

    

