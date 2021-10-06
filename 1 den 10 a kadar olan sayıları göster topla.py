import time

sayi = 0
toplam = 0

while sayi < 10:
    toplam += sayi
    sayi += 1
    print(f"sayaç = {sayi} toplam = {toplam}")
    time.sleep(0.25)

print(f"Toplam = {toplam}")