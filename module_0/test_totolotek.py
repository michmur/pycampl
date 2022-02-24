from totolotek import generate_six_numbers, check_if_you_win

def test_generate_six_numbers():
    score = generate_six_numbers()
    assert len(score) == 6

def test_check_if_you_win():
    score = check_if_you_win()
    assert len(score) == 6