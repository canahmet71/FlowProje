import time

derece = int(input("Su Şuan Kaç Derece"))

if derece <= 0:
    print(f"Su {derece} de katıdır")

elif 0 < derece < 100:
    print(f"Su {derece} de sıvıdır")

else:
    print(f"Su {derece} de gazdır")