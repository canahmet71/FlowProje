import time

sayi = 0
toplam = 0

while sayi < 20:
    toplam += sayi
    sayi += 1
    print(f"sayaç = {sayi}")
    time.sleep(0.25)

print(f"Toplam = {toplam}")