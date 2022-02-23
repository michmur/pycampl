"""_summary_

Returns:
    _type_: _description_
"""

from random import randint

print("Totolotek v 1.0.0")

def generate_six_numbers():
    """_summary_

    Returns:
        _type_: _description_
    """
    numbers = []
    for i in range(6):
        numbers.append(randint(1,49))
    return numbers

if __name__ == "__main__":
    lotto = generate_six_numbers()
    user = generate_six_numbers()
    