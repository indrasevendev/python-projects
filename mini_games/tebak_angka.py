import random

angka = random.randint(1, 10)
tebakan = int(input("Tebak angka 1-10: "))

if tebakan == angka:
    print("Kamu menebak dengan tepat!")
else:
    print("Salah! Jawabannya:", angka)
