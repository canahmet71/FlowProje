import time

sayi = []
i = 1

while i <= 5:
    yi = int(input(f"{i}. Sayıyı Giriniz"))
    sayi.append(yi)
    i += 1

ebs = max(sayi)

print(f"En Büyük Sayı = {ebs}")
