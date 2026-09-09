from app import topla

def test_topla():
    assert topla(2, 3) == 5

def test_topla_negatif():
    assert topla(-1, 1) == 0