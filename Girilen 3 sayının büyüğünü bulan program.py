import time

sayilar = []


while len(sayilar) < 3:
    sayi = int(input("Sayi Girin"))
    sayilar.append(sayi)

ebs = max(sayilar)

print(f"En Büyük Sayı = {ebs}")

