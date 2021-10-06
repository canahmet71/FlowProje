import time

not1 = int(input("1. notunuzu giriniz"))
not2 = int(input("2. notunuzu giriniz"))

ortalama = (not1 + not2) / 2

if ortalama < 47.5:
    time.sleep(0.37)
    print(f"Öğrenci {ortalama} puanıyla kaldı")

else:
    time.sleep(0.37)
    print(f"Öğrenci {ortalama} puanıyla geçti")
