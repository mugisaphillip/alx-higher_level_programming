#!/usr/bin/python3
""" Type check """


class Square:
    """ Private instance attribute: size
    Instantiation with optional """

    def __init__(self, size=0):
        """ initiatization """

        if (type(size) is not int):
            raize TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
