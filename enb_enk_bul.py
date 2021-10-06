import time

sayi = []
i = 0
sonucindex = 1

while i < 5:
    yi = int(input("Sayı Girin"))
    sayi.append(yi)
    i += 1
    
for notsum in sayi:
    print(f"{sonucindex}. sayı = {notsum}")
    time.sleep(0.05)
    notsum += notsum
    sonucindex += 1

print(f"Toplam = {nots