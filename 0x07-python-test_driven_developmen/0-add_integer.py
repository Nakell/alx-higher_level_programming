#!/usr/bin/python3
"""My module containa function 'add_integer' that adds two integers"""


def add_integer(a, b=98):
    """
    adds two integers.

    Args: a the first number, must be an integer or float
    b the second number, must be an integer or float

    Returns: the a + b
    Raises: TypeError if 'a' or 'b' is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
