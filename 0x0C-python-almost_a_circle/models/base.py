#!/usr/bin/python3
"Defines a base model class"


class Base:
    """
        Represent Base class model
        Attributes:
            __nb_objects (int)L The number is instances without id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing objects
        Args:
            id (int): id of new object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
