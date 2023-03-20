import pygame as pg
 
pg.init()
 



FPS = 60
W = 700  
H = 300  
RED = (255, 0 , 0)
WHITE = (255, 255, 225)
 
x = W // 2
y = H // 2
r = 25

screen = pg.display.set_mode((W, H))
 
 
speed = 20
to_left = False
to_right = False
to_up = False
to_down = False
 

while True:
    for event in pg.event.get():
        
        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_LEFT:
                to_left = True
            
            if event.key == pg.K_RIGHT:
                to_right = True
            
            if event.key == pg.K_DOWN:
                to_down = True
            
            if event.key == pg.K_UP:
                to_up = True
 
        
        if event.type == pg.KEYUP:
            
            if event.key == pg.K_LEFT:
                to_left = False
            
            if event.key == pg.K_RIGHT:
                to_right = False
            
            if event.key == pg.K_DOWN:
                to_down = False
            
            if event.key == pg.K_UP:
                to_up = False
 
    
    if to_right:
        x += speed
        to_right = False
    if to_left:
        x -= speed
        to_left = False
    if to_down:
        y += speed
        to_down = False
    if to_up:
        y -= speed
        to_up = False
    if event.type == pg.QUIT:
            pg.quit()
            exit()
 
    screen.fill(WHITE)
    pg.draw.circle(screen, RED, (x, y), r)
   

    pg.display.update()