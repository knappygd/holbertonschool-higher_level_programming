#!/usr/bin/python3
""" Base of all classes. """
import json


class Base:
    """ Base of all classes. """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return JSON representation. """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__ + ".json"
        with open(file, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_objs_dict = [i.to_dictionary() for i in list_objs]
                file.write(cls.to_json_string(list_objs_dict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set. """
        if cls.__name__ == "Rectangle":
            new = cls(5, 3)
        else:
            new = cls(5)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                file_list = Base.from_json_string(file.read())
                return [cls.create(**d) for d in file_list]
        except FileNotFoundError:
            return []
