sayac = 0
toplam = 0
dismissed = 0

import time

while sayac < 100:
    sayac += 1
    if sayac%3 == 0 or sayac%5 == 0:
        toplam += sayac
        print(f"sayaç = {sayac} toplam = {toplam}")
        time.sleep(0.15)

    else:
        dismissed += 1
        print(f"sayaç = {sayac} toplam = {toplam}")
        time.sleep(0.15)


print(f"Toplam = {toplam}. {dismissed} kadar sayı umursanmadı")
        


