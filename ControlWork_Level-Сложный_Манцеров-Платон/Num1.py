#№1
class Animal:
    def make_sound(self):
        print("Животное издает звук")

class Kot(Animal):
    def make_sound(self):
        print("Кошка мяукает")

class Dog(Animal):
    def make_sound(self):
        print("Собака лает")

animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()

kot = Kot()
kot.make_sound()
