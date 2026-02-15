import random

angka = random.randint(1, 10)
tebakan = int(input("Tebak angka 1-10: "))

if tebakan == angka:
    print("Benar!")
else:
    print("Salah! Jawabannya:", angka)
