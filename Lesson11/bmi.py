from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.weight = value
        else:
            raise ValueError("Must have Weight")

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if value > 0:
            self.height = value
        else:
            raise ValueError("Must have height")

    