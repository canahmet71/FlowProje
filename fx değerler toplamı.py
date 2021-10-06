import time

x = 3

def f(x):
    fx = x * x + 7 * x + 14

    time.sleep(2.5)

    return fx

print("Eğer f(x) = x * x + 7 * x + 14 ise ")

time.sleep(2.5)

print(f"f({x}) = {f(x)} olur")

