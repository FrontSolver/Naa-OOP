class Area:
    def __init__(self):
        self.pi = 3.14
        self.area = 0
    def square(self, a):
        self.area = a**2
        self.print_area()
    def rectangle(self, b, h):
        self.area = b * h
        self.print_area()
    def parallelogram(self, b,h):
        self.area = b * h
        self.print_area()
    def rhombus(eslf, p ,q):
        self.area = p*q/2
        self.print_area()
    def trapezoid(self,a,b,h):
        self.area = (a+b)*h/2
        self.print_area()
    def circle(self,r):
        self.area = self.pi*(r**2)
        self.print_area()
    def ellipse(self,a ,b):
        self.area = self.pi*a*b
        self.print_area()
    def triangle(self, b,h):
        self.area = b*h/2
        sel.print_area()
    def print_area(self):
        print('Area = ', self.area)  
my_area_square = Area()
my_area_square.square(2)