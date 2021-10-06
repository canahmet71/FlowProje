import time
import math

pi = math.pi

r = int(input("Sayı Girin"))

time.sleep(0.10)

cevre = 2 * (pi * r)

time.sleep(0.10)

alan = pi * (r * r)

print(f"Çevre = {cevre}")

time.sleep(0.10)
print(f"Alan = {alan}")