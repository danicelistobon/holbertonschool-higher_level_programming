#!/usr/bin/python3
"""Module Base
"""


import json


class Base:
    """Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class
            Args:
                id (int): unique id of the classes
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
