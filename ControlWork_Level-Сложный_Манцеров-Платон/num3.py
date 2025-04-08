import abc

# Абстрактный класс Shape
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): 
        pass  # Метод для вычисления площади

    @abc.abstractmethod
    def volume(self): 
        pass  # Метод для вычисления объема

# Класс Rectangle, наследующий от Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # Длина
        self.width = width  # Ширина

    def area(self):
        return self.length * self.width  # Площадь прямоугольника

    def volume(self):
        return "Нету"  # Прямоугольник не имеет объема

# Класс Cube, наследующий от Shape
class Cube(Shape):
    def __init__(self, length):
        self.length = length  # Длина ребра куба

    def area(self):
        return 6 * (self.length ** 2)  # Площадь поверхности куба

    def volume(self):
        return self.length ** 3  # Объем куба

# Класс Sphere, наследующий от Shape
class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius  # Радиус сферы

    def area(self):
        return 4 * 3.14 * (self.radius ** 2)  # Площадь поверхности сферы

    def volume(self):
        return (4/3) * 3.14 * (self.radius ** 3)  # Объем сферы

# Класс Piramide, наследующий от Shape
class Pyramid(Shape):
    def __init__(self, height, base_length):
        self.height = height  # Высота пирамиды
        self.base_length = base_length  # Длина основания

    def area(self):
        return self.base_length * (self.base_length + 2 * self.height)  # Площадь пирамиды

    def volume(self):
        return (1/3) * (self.base_length ** 2) * self.height  # Объем пирамиды

# Основной блок программы
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 10),
        Cube(3),
        Sphere(5),
        Pyramid(5, 15)
    ]

    for shape in shapes:
        print(f"Площадь {shape.__class__.__name__}: {shape.area()}")
        print(f"Объем {shape.__class__.__name__}: {shape.volume()}")
