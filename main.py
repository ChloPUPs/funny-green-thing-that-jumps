import pygame as pg
import sys

screen = pg.display.set_mode((640, 480))
clock = pg.Clock()
framerate = 60

key_is_pressed: dict[str, bool] = {
    "right": False,
    "left": False,
    "down": False,
    "up": False,
    "space": False
}

class Player:
    def __init__(self, x: int, y: int, width: int, height: int, rgb: list[int]):
        self.rect = pg.Rect(x, y, width, height)
        self.rgb: list[int] = rgb
        self.velocity_y = 0
        self.gravity: float = 0.5

    def update(self):
        self.velocity_y += self.gravity

        self.rect.y += self.velocity_y

    def draw(self):
        pg.draw.rect(screen, self.rgb, self.rect)
    
    def jump(self):
        self.velocity_y = -10

player = Player(100, 50, 32, 32, [255, 0, 0])

def draw_screen(background_color: list[int]):
    screen.fill(background_color)
    player.draw()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit(0)
        
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_RIGHT:
                key_is_pressed["right"] = True
            if e.key == pg.K_LEFT:
                key_is_pressed["left"] = True
            if e.key == pg.K_DOWN:
                key_is_pressed["down"] = True
            if e.key == pg.K_UP:
                key_is_pressed["up"] = True
                player.jump()
            if e.key == pg.K_SPACE:
                key_is_pressed["space"] = True
                player.jump()

        if e.type == pg.KEYUP:
            if e.key == pg.K_RIGHT:
                key_is_pressed["right"] = False
            if e.key == pg.K_LEFT:
                key_is_pressed["left"] = False
            if e.key == pg.K_DOWN:
                key_is_pressed["down"] = False
            if e.key == pg.K_UP:
                key_is_pressed["up"] = False
            if e.key == pg.K_SPACE:
                key_is_pressed["space"] = False
    
    draw_screen([0, 0, 0])
    player.update()

    clock.tick(framerate)
    pg.display.update()