faktoriel = 1
sayi = 1

nsayi = int(input("Sayi Girin"))

while sayi <= nsayi:
    faktoriel = faktoriel * sayi
    sayi += 1

print(f"{nsayi} sının Faktoriyeli = {faktoriel}")