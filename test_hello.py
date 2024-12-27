from hello import add, subtract


def test_add() -> None:
    assert 2 == add(1, 1)

def test_subtract() -> None:
    assert -1. == subtract(1., 2)