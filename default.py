#create a Maze game!
from pygame import *


window = display.set_mode((700, 500))
display.set_caption("Catch")
background = transform.scale(image.load("background.jpg"), (700, 500))

cyborg = transform.scale(image.load('cyborg.png'), (100, 100))
cyborg_x = 100
cyborg_y = 100

game = True 

while game:
    window.blit(background, (0,0))
    window.blit(cyborg, (cyborg_x, cyborg_y))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT]:
        cyborg_x -= 2


    display.update()
