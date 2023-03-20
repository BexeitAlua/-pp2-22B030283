import pygame as pg
from datetime import datetime



pg.init()

WIDTH = 800
HEIGHT = 600
FPS = 45
BLACK = (0,0,0)

pg.display.set_caption('clock')
screen = pg.display.set_mode((WIDTH, HEIGHT))

font = pg.font.SysFont("times New Roman", 35)

clock = pg.time.Clock()

background = pg.image.load("clock.jpg")
h = pg.image.load("min.png")
h2 = pg.image.load("sec.png")

def time(t):
    return 360 - t * 6

def rotate(surface, image, left_pos, angle):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = left_pos).center)

    surface.blit(rotated_image, new_rect)
running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(background, (0,0))
    t = datetime.now()
    angle_sec = time(t.second)
    angle_min = time(t.minute)
    rotate(screen, h2, (255, 150), angle_sec)
    rotate(screen, h, (255, 150), angle_min)
 
    text = font.render(f'{t:%H:%M:%S}', True, BLACK)
    screen.blit(text, (0,0))

    pg.display.flip()

pg.quit()