
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area (self): pass       # площадь фигур
    @abc.abstractmethod
    def volume(self): pass
class Rectangle(Shape):
    def __init__(self, len, dight):
        self.len = len
        self.dight = dight
    def area(self):
        return self.dight*self.len
    def volume(self):
        return "Нету"
class Cube(Shape):
    def __init__(self, len):
        self.len = len
    def area(self):
        return self.len**2
    def volume(self):
        return self.len**3
class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 4 * 3,14 * (self.radius ** 2)
    def volume(self):
        return "я не нашел формулу"
class Piramide(Shape):
    def __init__(self, h,a):
        self.h = h
        self.a = a
    def area(self):
        return self.a*(self.a+2*self.h)
    def volume(self):
        return (1/3)*(self.a**2)*self.h

if __name__ == "__main__":
    shapes = [
        Rectangle(5, 10),
        Cube(3),
        Sphere(5),
        Piramide(5,15)
    ]

    for shape in shapes:
        print(f"Площадь {shape.__class__.__name__}: {shape.area()}")
        print(f"Обьем {shape.__class__.__name__}: {shape.volume()}")
