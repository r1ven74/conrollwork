# Определяем базовый класс Animal
class Animal:
    # Метод make_sound, который будет переопределен в подклассах
    def make_sound(self):
        print("Животное издает звук")

# Определяем класс Kot, который наследует от Animal
class Kot(Animal):
    # Переопределяем метод make_sound для класса Kot
    def make_sound(self):
        print("Кошка мяукает")

# Определяем класс Dog, который также наследует от Animal
class Dog(Animal):
    # Переопределяем метод make_sound для класса Dog
    def make_sound(self):
        print("Собака лает")

# Создаем экземпляр базового класса Animal
animal = Animal()
# Вызываем метод make_sound для объекта animal
animal.make_sound()  # Вывод: Животное издает звук

# Создаем экземпляр класса Dog
dog = Dog()
# Вызываем метод make_sound для объекта dog
dog.make_sound()  # Вывод: Собака лает

# Создаем экземпляр класса Kot
kot = Kot()
# Вызываем метод make_sound для объекта kot
kot.make_sound()  # Вывод: Кошка мяукает
