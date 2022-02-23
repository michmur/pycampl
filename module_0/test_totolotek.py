from totolotek import generate_six_numbers

def test_generate_six_numbers():
    score = generate_six_numbers()
    assert len(score) == 6