import pygame as pg  
import random
pg.init()

WIDTH=800
HEIGHT=800
FPS=5
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
events = pg.event.get()
clock=pg.time.Clock()
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("SNAKE")
 # параметры снейка
class Snake:
    def __init__(self):
        self.length = 1
        self.color = BLUE
        self.score = 0
        self.body = [[80,80]] # изначальные координаты тела снейка
        self.speed = 40
        self.dx = self.speed
        self.dy = 0
    #перемещение снейка
    def move(self):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.dx == 0: #при нажиманий клавиши лефт снейк движется по оси x а по оси y остается неподвижным
                    self.dx = -self.speed
                    self.dy = 0
                if event.key ==pg.K_UP and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_DOWN and self.dy == 0:
                    self.dy = self.speed
                    self.dx = 0
                if event.key == pg.K_RIGHT and self.dx == 0:
                    self.dy = 0
                    self.dx = self.speed
        self.body[0][0] += self.dx # к координате x добавляется перемещение по оси х
        self.body[0][1] += self.dy # к координате у добавляется перемещение по оси у
# так как снейк растет по мере поедания то сначало его тело равно 80 на 80 но перемещаясь он растет и его размеры хранятся в листе self.body: [[80,80],[120,80],[160,80]]
    def draw(self): # рисуем сам снейк
        for i in self.body:
            pg.draw.rect(screen,self.color,(i[0],i[1],40,40),5) # поверхность; цвет; координаты верхнего левого угла; ширина и высота
    
    #если он сьедает себя снейк умирает
    def collision(self):
        if self.body[0] in self.body[1:]:
            print("GAME OVER")

    def eat(self,food):
        if self.body[0][0] == food.x  and self.body[0][1]== food.y:
            self.length+=1
            self.body.append([1000,1000])
            self.score+=1
            food.gen()

class Food:
    def __init__(self):
        self.x = random.randint(0,WIDTH) % 20 * 40 # рандомно появляющийся фуд
        self.y = random.randint(0,HEIGHT) % 20 * 40
        self.r = 20
    def draw(self):
        pg.draw.circle(screen,(0,255,0),(self.x + self.r,self.y+self.r),self.r)

    def gen(self):
        self.x = random.randint(0,WIDTH) % 20 * 40 
        self.y = random.randint(0,HEIGHT) % 20 * 40

class WALL:
    def __init__(self):
        self.x = x
        self.y = y
    def draw(self):
        pg.draw.rext(screen,(255,0,0), (self.x,self.y,40,40))

s = Snake()
f=Food()

running=True

while running:
    clock.tick(FPS)
    for event in events:
        if event.type == pg.QUIT:
            running=False
    screen.fill(WHITE)
    s.draw()
    s.move()
    s.collision()
    f.draw()
    s.eat(f)

    pg.display.update()
pg.quit()

