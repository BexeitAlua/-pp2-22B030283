import pygame as pg
import random
pg.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

y = 0
ry = 2
score = 0



screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
font = pg.font.SysFont("Times New Roman", 40)
pg.display.set_caption("Racer")

road = pg.image.load("animatedstreet.jpg")

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('Playerr.png')
        self.surf = pg.Surface((40,60))
        self.rect = self.surf.get_rect(center = (400,500))
        self.speed = 5
    
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.top > 0:
            self.rect.move_ip(0, - self.speed)
        if keys[pg.K_s] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.speed)
        if keys[pg.K_a] and self.rect.left > 0:
            self.rect.move_ip(- self.speed, 0)
        if keys[pg.K_d] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)
    
    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40,60)), (0,0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Enemyy.png")
        self.surf = pg.Surface((40,60))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(3,7)
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40,60)), (0,0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))
    def ubivat(self):
        if self.rect.top > HEIGHT:
            self.kill()
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((20,20))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH - 20), -100))
        self.speed = random.randint(1, 6)
        self.random_number = random.randint(0, 6)
        self.image = pg.image.load("coin.png")
        self.mega_coin()
    def move(self):
        self.rect.move_ip(0, self.speed)
    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (20,20)), (0,0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))
    def ubivat(self):
        if self.rect.top > HEIGHT:
            self.kill()
    def mega_coin(self):
        if self.random_number in [0,1,2]:
            self.image = pg.image.load("supercoin.jpg")
    
    def is_mega_coin(self):
        return self.random_number in [0,1,2]
    
p = Player()

enemies = pg.sprite.Group([Enemy() for _ in range(3)])
coins = pg.sprite.Group([Coin() for _ in range(3)])

running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type =dd

    screen.fill(WHITE)
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, y % HEIGHT))
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, -HEIGHT + (y % HEIGHT)))
    
    y += ry

    p.draw()
    p.move()
    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.ubivat()

    for c in coins:
        c.draw()
        c.move()
        c.ubivat()
    
    if enemies.__len__() < 3:
        enemies.add(Enemy())
    if coins.__len__() < 3:
        coins.add(Coin())

    if pg.sprite.spritecollide(p, enemies, False):
        running = False
    
    for c in pg.sprite.spritecollide(p, coins, True):
        score += 1
        if c.is_mega_coin():
            score += 5

    text = font.render(f'{score}', True, BLACK)
    screen.blit(text, (20,20))
    pg.display.update()

pg.quit()
