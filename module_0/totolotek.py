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
    while len(numbers) != 6:
        numbers.append(randint(1,49))
    return numbers

def check_if_you_win():
    """_summary_

    Returns:
        _type_: _description_
    """
    lotto = generate_six_numbers()
    user = generate_six_numbers()
    # user = lotto
    count = 0
    control_list = []

    # while len(control_list) != 6:
    #     control_list = list(set(lotto)&set(user))
    #     if 0 < len(control_list) < 6:
    #         count += 1
    #         print(f"Udało ci się trafić {len(control_list)} liczb {control_list} losowanie nr : {count:,}")
    #         user = generate_six_numbers()
    #     else:
    #         user = generate_six_numbers()
    #         count += 1
    # print(f"{lotto} {user}")
    # return f"Udało ci się trafić 6 za {count:,} razem, wydałeś {count*3:,} zł"

    while lotto != user:
        user = generate_six_numbers()
        print(lotto,user)
        count += 1
        
    return f"Udało ci się trafić 6 za {count:,} razem, wydałeś {count*3:,} zł"

if __name__ == "__main__":
    print(check_if_you_win())
