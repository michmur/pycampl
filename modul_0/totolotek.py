from random import random

user_numbers = list()

print("Totolotek v 1.0.0")
print("Podaj sześć liczb")

for i in range(6):
    number = int(input("Podaj liczbę : "))
    user_numbers.append(number)


def generate_lotto_numbers():
    """Generate set of six numbers

    Returns:
        set: set of six numbers
    """
    lotto_numbers = set()
    for i in range(1,7):
        lotto_numbers.add(random.randint(1,49))
    return lotto_numbers