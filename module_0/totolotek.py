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
    while(len(numbers) != 6):
        numbers.append(randint(1,49))
    return numbers

if __name__ == "__main__":
    lotto = generate_six_numbers()
    user = generate_six_numbers()
    count = 0

    while(True):
        if len(set(lotto)&set(user)) == 6:
            break
        else:
            user = generate_six_numbers()
            count += 1
            print(f"Nie udało się trafić szóstki losujemy dalej dla liczb : {user} losowanie numer {count}")
    