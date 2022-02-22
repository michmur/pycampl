from random import random


import random

user_numbers = list()
lotto_numbers = set()

print("Totolotek v 1.0.0")
print("Podaj sześć liczb")

for i in range(6):
    number = int(input("Podaj liczbę : "))
    user_numbers.append(number)

for i in range(1,7):
    lotto_numbers.add(random.randint(1,49))

print(f"Numery wytypowane przez użytnownika ")
print(user_numbers)
print("Szczęśliwe numery")
print(lotto_numbers)
