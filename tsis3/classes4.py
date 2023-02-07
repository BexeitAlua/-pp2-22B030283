import math


class Point(object):
    

    COUNT = 0

    def __init__(self, x, y):
       
        self.X = x
        self.Y = y

    def move(self, dx, dy):
        
        self.X = self.X + dx
        self.Y = self.Y + dy

    

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2 + dy**2)

    def show(x=0,y=0):
        p1 = Point(3, 4)
        print (p1)
        p2 = Point(3,0)
        print (p2)
    
   
    