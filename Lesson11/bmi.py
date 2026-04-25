from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}")

    @property
    def name(self, name):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def age(self, age):
        return self.age

    @age.setter
    def age(self, age):
        self.age

