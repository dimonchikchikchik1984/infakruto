class Shape:
    def breadth(self):
        self.b=float(input())
    def height(self):
        self.h=float(input())


class Rectangle(Shape):
    def area(self):
        print(self.b*self.h)


class Triangle(Shape):
    def area(self):
        print(0.5*self.b*self.h)