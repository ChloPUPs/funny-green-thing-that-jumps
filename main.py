import pygame as pg
import sys
import random
from time import *

screen = pg.display.set_mode((640, 480))
pg.display.set_caption("funny green thing that jumps")
window_icon = pg.image.load("assets/icon.ico")
pg.display.set_icon(window_icon)

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
        self.startx = x
        self.starty = y
        self.rgb: list[int] = rgb
        self.velocity_y = 0
        self.gravity: float = 0.5
        self.img = pg.image.load("./assets/fbplayer.png")

    def update(self):
        self.velocity_y += self.gravity

        self.rect.y += self.velocity_y

    def draw(self):
        # pg.draw.rect(screen, self.rgb, self.rect)
        screen.blit(self.img, self.rect.topleft)
    
    def jump(self):
        self.velocity_y = -10

class Pipe:
    def __init__(self, speed: float):
        self.brect = pg.Rect(500, random.randrange(200, 451), 100, 800)
        self.trect = pg.Rect(self.brect.x, (self.brect.y - self.brect.height) - 170, self.brect.width, self.brect.height)
        self.speed = speed
        self.bimg = pg.image.load("assets/pipe.png")
        self.timg = pg.transform.flip(self.bimg, False, True)

    def update(self):
        self.brect.x -= self.speed
        self.trect.x = self.brect.x
        self.trect.y = (self.brect.y - self.brect.height) - 170

        if self.brect.right < 0:
            self.brect.left = 640
            self.brect.y = random.randrange(200, 451)
    
    def draw(self):
        screen.blit(self.bimg, self.brect.topleft)
        screen.blit(self.timg, self.trect.topleft)

player = Player(100, 50, 32, 32, [255, 0, 0])
player_hit = False
pipe = Pipe(3)

def player_just_hit() -> bool:
    if player.rect.colliderect(pipe.brect) or player.rect.colliderect(pipe.trect) or player.rect.y < 0 or player.rect.y > 480 - 32:
        return True
    else:
        return False

def draw_screen(background_color: list[int]):
    screen.fill(background_color)
    player.draw()
    pipe.draw()

def update_game():
    player.update()
    pipe.update()

def game_over():
    sleep(1)
    pipe.brect.x = 500
    player.rect.y = player.starty
    player.velocity_y = 0

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

    if player_just_hit() and not player_hit:
        game_over()
    
    draw_screen([0, 200, 255])
    update_game()

    clock.tick(framerate)
    pg.display.update()