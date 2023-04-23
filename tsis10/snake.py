import pygame
from random import randint, randrange
import psycopg2
from config import data
username = input()
db = psycopg2.connect(**data)
   

cursor = db.cursor()

sql = '''
    SELECT * FROM users WHERE username = %s;
'''
cursor.execute(sql, [username])
data = cursor.fetchone()


if data == None:
    sql = '''
        INSERT INTO users (id, username, score) VALUES(12, %s, 0);
    '''
    cursor.execute(sql, [username])
    db.commit()
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 10
cell = 20


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREENYELLOW = (173, 255, 47)
BLUE = (0, 0, 255)
PURPLE = (221, 160, 221)
GRAY = (128, 128, 128)

font_small = pygame.font.SysFont("Verdana", 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

finished = False

clock = pygame.time.Clock()

SPEEDUP = pygame.USEREVENT + 1
pygame.time.set_timer(SPEEDUP, 10000, loops=10000)

food_in_snake = True
class Wall:
    def __init__(self):
        self.body = []
        self.load_wall()

    def load_wall(self, level=1):
        with open(f'level{level}.txt', 'r') as f:
            wall_body = f.readlines()

        for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
                if value == '#':
                    self.body.append([j, i])

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, GRAY, (x * cell, y * cell, cell, cell))


class Food:
    def __init__(self):
        
        self.x = randrange(cell, WIDTH-cell, cell)
        self.y = randrange(cell, HEIGHT-cell, cell)

    def draw(self):
        global food_in_snake
        
        if [self.x,self.y] not in s.body:
            pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell))

    def redraw(self):
        if [self.x,self.y] in s.body:
            self.x = randrange(cell, WIDTH-cell, cell)
            self.y = randrange(cell, HEIGHT-cell, cell)
                


lvl = 1
highscore= 0


class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80], [1000, 1000], [
            1040, 1040], [1080, 1080], [1120, 1120]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = BLUE

    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_d and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_w and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_s and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color,
                             (block[0], block[1], cell, cell))

    def collide_food(self, f: Food):
        global score
        global lvl
        global FPS
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            f.redraw()
            self.body.append([1000, 1000])
            score += 1
        if score == 2:
            wall.load_wall(level=2)
            lvl = 2
        if score == 4:
            wall.body.clear()
            wall.load_wall(level=3)
            lvl = 3

    def collide_self(self):
        global finished
        if self.body[0] in self.body[1:]:
            finished = True

    def collide_level(self):
        global finished
        for i in range(len(wall.body)):
            if self.body[0][0] == wall.body[i][0]*cell and self.body[0][1] == wall.body[i][1]*cell:
                finished = True

    def collide_bord(self):
        global finished
        if self.body[0][0] >= WIDTH-cell or self.body[0][1] >= HEIGHT-cell or self.body[0][0] <= 0 or self.body[0][1] <= 0:
            finished = True


s = Snake()
f = Food()
wall = Wall()

score = 0


while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
            pygame.music.stop
    screen.fill(GREEN)

    for i in range(0, WIDTH, cell):
        for j in range(0, HEIGHT, cell):
            pygame.draw.rect(screen, GREENYELLOW, (i, j, cell, cell), 1)

    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, HEIGHT), cell)
    scores = font_small.render(f"score:{score}", True, BLACK)
    screen.blit(scores, (19, 14))

    cc = font_small.render(f"level:{lvl}", True, BLACK)
    screen.blit(cc, (19, 30))

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
        s.body.append([0, 0])
        f.draw()
        if score == 2:
            wall.load_wall(level=2)
            f.draw()
        if score == 3:
            wall.load_wall(level=3)
            f.draw()
    FPS = 10 * lvl/1.99
    pygame.display.flip()
pygame.quit()
if score > highscore:
    highscore = score
sql = '''
    UPDATE users SET score = %s, highscore = %s, level = %s WHERE username = %s;
'''
cursor.execute(sql, [score, highscore, lvl, username])
db.commit()
cursor.close()
db.close()
