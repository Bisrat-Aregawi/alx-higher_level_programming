#!/usr/bin/python3
"""Module Defines 'Base' class."""
import json


class Base:
    """Class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize object with 'id' instance attribute.

        Args:
            self (object): Refers to the object instance
            id (int, optional): Id of created instances
        Returns:
            None
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
        return None

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static class method to serialize iterable objects.

        Returns a serialized string from @list_dictionaries object by using the
        json module.

        Args:
            list_dictionaries (list): A list of dictionary objects.

        Returns:
            None
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Create a json file of @list_objs.

        Args:
            cls (class): Refers to 'Base' class
            list_objs (list): List of instance that inherit 'Base'

        Returns:
            None
        """
        j_list = []
        if list_objs:
            for obj in list_objs:
                j_list.append(obj.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(j_list))
        return None

    @staticmethod
    def from_json_string(json_string):
        """Create a list object from passed string.

        Args:
            json_string (str): String representing list of dictionaries

        Returns:
            List of JSON string representation @json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    pass
