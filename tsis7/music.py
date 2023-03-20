import pygame as pg

pg.init()


pg.mixer.init()
pg.mixer.music.load("BTS Black swan.mp3")
pg.mixer.music.play(-1)

WIDTH = 100
HEIGHT = 100
FPS = 60

BLACK = (0,0,0)


screen = pg.display.set_mode((WIDTH,HEIGHT))

clock = pg.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                pg.mixer.music.pause()
            if event.key == pg.K_s:
                pg.mixer.music.unpause()
            if event.key == pg.K_RIGHT:
                pg.mixer.music.load("BTS Run bts.mp3")
                pg.mixer.music.play(-1)
            if event.key == pg.K_LEFT:
                pg.mixer.music.load('BTS Black swan.mp3')
                pg.mixer.music.play(-1)   
            screen.fill(BLACK)
    
    
    pg.display.flip()

pg.quit()