import time

carpan = 1

while True:
    carpilan = int(input("Sayı Girin"))

    while carpan < 10:
        cevap = carpilan * carpan
        print(f"{carpilan} * {carpan} = {cevap}")
        carpan += 1
        time.sleep(0.05)

    carpan = 1

    onay = input("Devam Etmek İçin E ye Çıkmak İçin H ye basın")

    if onay =="E" or onay =="e":
        continue

    else:
        break
        
