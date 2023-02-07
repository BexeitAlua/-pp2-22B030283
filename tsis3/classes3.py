class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

x=int(input())
y=int(input())
newRectangle = Rectangle(x, y)
print(newRectangle.rectangle_area())