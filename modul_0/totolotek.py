"""_summary_

Returns:
    _type_: _description_
"""

from random import randint

print("Totolotek v 1.0.0")

def user_numbers():
    """_summary_

    Returns:
        _type_: _description_
    """
    numbers = []
    for i in range(6):
        number = int(input("Podaj liczbę : "))
        numbers.append(number)
    return numbers


def lotto_numbers():
    """_summary_

    Returns:
        _type_: _description_
    """
    numbers = set()
    for i in range(7):
        numbers.add(randint(1,49))
    return numbers

lotto = user_numbers

if __name__ == "__main__":
   p = lotto_numbers()
   print(p)
