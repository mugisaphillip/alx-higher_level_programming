#!/usr/bin/python3
"""
add_integer - adds 2 integers
@a: integer 1
@b: integer 2
Return: sum of numbers passed
"""


def add_integer(a, b=98):
    """
    function that adds 2 integers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return (a + b)
