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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        """
        filename = '{}.json'.format(cls.__name__)
        dic = []

        if list_objs is not None:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))

        with open(filename, 'w', encoding='utf-8') as new_file:
            new_file.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)
