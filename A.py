class Complex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Complex(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return Complex(self.x*other.x, self.y*other.y)

    def __truediv__(self, other):
        return Complex(self.x/other.x, self.y/other.y)
    
