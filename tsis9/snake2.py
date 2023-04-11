import pygame as pg
import random
pg.init()

WIDTH, HEIGHT = 800, 600
FPS = 10
cell = 20

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0 ,0)
BLUE = (0,0,255)
GREY = (105,105,105)
GREEN = (0,255,0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SNAKE")

font_small = pg.font.SysFont("Verdana", 20)

running = True

score = 0
level = 1

clock = pg.time.Clock()
food_in_snake = True
# создаем класс для создания стен во 2 уровне
class Wall:
    def __init__(self):
        self.body = []
        self.load_wall()

    def load_wall(self, level = 1):
        with open(f'level{level}.txt', 'r') as f:
            wall_body = f.readlines()
        
        for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
                if value == "#":
                    self.body.append([j,i])
    def draw(self):
        for x, y in self.body:
            pg.draw.rect(screen, GREY, (x * cell, y * cell, cell, cell))
class Food:
    def __init__(self):
        self.x = random.randrange(cell, WIDTH - cell, cell)
        self.y = random.randrange(cell, HEIGHT - cell, cell)
    def draw(self):
        global food_in_snake
        if [self.x, self.y] not in s.body:
            pg.draw.rect(screen, RED, (self.x, self.y, cell, cell))
    def redraw(self):
        if [self.x, self.y] in s.body:
            self.x = random.randrange(cell, WIDTH - cell, cell)
            self.y = random.randrange(cell, HEIGHT - cell, cell)

class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80], [1000, 1000], [
            1040, 1040], [1080, 1080], [1120, 1120]]
        self.dx = self.speed
        self.destination = ''
        self.color = BLUE
        self.dy = 0
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.destination != 'right':
                    self.dx = - self.speed
                    self.dy = 0
                    self.destination = 'left' 
                if event.key == pg.K_RIGHT and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pg.K_UP and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pg.K_DOWN and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
    def draw(self):
        for i in self.body:
            pg.draw.rect(screen, self.color,(i[0],i[1], cell, cell))
    
    def collide_food(self, f: Food):
        global score
        global level
        global FPS
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            f.redraw()
            self.body.append([1000,1000])
            score += 1
            if score == 4:
                wall.body.clear()
                wall.load_wall(level = 2)
                level = 2
    def collide_self(self):
        global running
        if self.body[0] in self.body[1:]:
            running = False
    def collide_level(self):
        global running
        for i in range(len(wall.body)):
            if self.body[0][0] == wall.body[i][0] * cell and self.body[0][1] == wall.body[i][1] * cell:
                running = False
    def collide_bord(self):
        global running
        if self.body[0][0] >= WIDTH - cell or self.body[0][1] >= HEIGHT - cell:
            running = False
    

s = Snake()
f = Food()
wall = Wall()

while running:
    clock.tick(FPS)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    screen.fill(GREEN)
    f.draw()
    s.draw()
    wall.draw()
    wall.load_wall()
    s.move(events)
    s.collide_food(f)
    s.collide_self()
    s.collide_bord()
    s.collide_level()
    if s.body[0][0] * cell == f.x and s.body[0][1] * cell == f.y:
        s.body.append([0,0])
        f.draw()
        if score == 4:
            wall.load_wall(level = 2)
            level = 2

    pg.display.flip()
pg.quit()