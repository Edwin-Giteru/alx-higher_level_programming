#!/usr/bin/python3
import json
class Base:

    # Private class attribute
    __nb_objects = 0

    # Class constructor
    def __init__(self, id=None):
        if id is not None:
            # Assign id if provided
            self.id = id
        else:
            # Increment the class attribute __nb_objects
            Base.__nb_objects += 1
            # Assign the new value to the instance's id
            self.id = Base.__nb_objects
    # data representation in json form
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    # class base to by addding a class method taht writes a json representation of a file
         
    @classmethod
    def save_to_file(cls,list_objs):
        if list_objs is None:
            list_objs = []

        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)

        filename = f"{cls.__name__}.json"

        with open(filename,"w") as file:
            file.write(json_string)
    # updating class base to return a list of the JSON string representation
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
