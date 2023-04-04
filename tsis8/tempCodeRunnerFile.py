WIDTH = 800
HEIGHT = 800
FPS = 5
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake")

clock = pg.time.Clock()

running = True