import time

not1 = int(input("1. notunuzu giriniz"))
not2 = int(input("2. notunuzu giriniz"))
not3 = int(input("3. notunuzu giriniz"))

ortalama = (not1 + not2 + not3) / 3

if ortalama < 47.5:
    time.sleep(0.37)
    print(f"Öğrenci {ortalama} puanıyla kaldı")

else:
    time.sleep(0.37)
    print(f"Öğrenci {ortalama} puanıyla geçti")
