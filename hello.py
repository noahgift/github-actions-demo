def add(x: int | float, y: int | float) -> int | float:
    """This is an add function"""

    return x + y

def subtract(x: int | float, y: int | float) -> int | float:
    """Subtract function"""

    return x - y

if __name__ == "__main__": # pragma: no cover
    print(add(1, 1))

