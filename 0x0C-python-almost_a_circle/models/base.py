#!/usr/bin/python3
""" The base of all other classes in this project. """
import json
import os.path
import csv
import turtle
import random


class Base:
    """ Object to manage id attribute in all other classes
    and to avoid duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw objects """
        colors = ["black", "yellow", "green", "red", "blue"]
        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            pos = random.randint(0, len(colors) - 1)
            turtle.pen(fillcolor=colors[pos], pencolor=colors[pos - 1],
                       pensize=10)
            turtle.right(90)
            for i in range(2):
                turtle.left(90)
                turtle.fd(rect.width)
                turtle.left(90)
                turtle.fd(rect.height)

        for sqr in list_squares:
            turtle.penup()
            turtle.goto(sqr.x, sqr.y)
            turtle.pendown()
            turtle.right(90)
            for i in range(2):
                turtle.left(90)
                turtle.fd(sqr.size)
                turtle.left(90)
                turtle.fd(sqr.size)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        lst = cls.to_json_string(list_dict)

        with open(filename, 'w') as fs:
            fs.write(lst)
            fs.close()

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """ Get list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as fs:
            lst_str = fs.read()

        lst_cls = cls.from_json_string(lst_str)
        lst_inst = []

        for lc in lst_cls:
            new = cls.create(**lc)
            lst_inst.append(new)

        return lst_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save Csv file """
        filename = "{}.csv".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

            with open(filename, 'w') as fs:
                writer = csv.DictWriter(fs, fieldnames=list(list_dict[0]))
                writer.writeheader()

                for dct in list_dict:
                    writer.writerow(dct)
                fs.close()

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists is False:
            return []

        list_inst = []

        with open(filename, 'r') as fs:
            csv_file = csv.DictReader(fs)

            for row in csv_file:
                for key, value in row.items():
                    row[key] = int(value)
                new = cls.create(**row)
                list_inst.append(new)

        return list_inst
