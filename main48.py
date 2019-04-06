from abc import ABCMeta, abstractmethod, ABC


class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class square(shape):
    type="square"
    side=4
    def __init__(self):
        self.length=5
    def printarea(self):
        return self.length*self.length
class triangle(shape):
    type="triangle"
    side=3
    def __init__(self):
        self.breadth=8
        self.height=10
    def printarea(self):
        return 1/2*(self.breadth * self.height)
class parallellogram(shape):
    type="parallelllogram"
    side=4
    def __init__(self):
        self.breadth=8
        self.height=10
    def printarea(self):
        return self.breadth * self.height


class circle(shape):
    type = "circle"
    area = 360
    def __init__(self):
        self.radius=10
    def printarea(self):
        return 22/7*(self.radius*self.radius)

class rectangle(shape):
    type="rectangle"
    sides=4
    def __init__(self):
        self.length=9
        self.breadth=9

    def printarea(self):
        return self.length * self.breadth
rec1=rectangle()
rad1=circle()
tri1=triangle()
sqa1=square()
para1=parallellogram()
print(para1.printarea())