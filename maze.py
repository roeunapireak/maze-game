#create a Maze game!
from pygame import *

from spriteClass import GameSprite

window = display.set_mode((700, 500))
display.set_caption("Catch")
background = transform.scale(image.load("background.jpg"), (700, 500))

timer = time.Clock()

cyborg = GameSprite('cyborg.png',100, 100, 2)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

game = True 

while game:
    window.blit(background, (0,0))
    # window.blit(cyborg, (cyborg_x, cyborg_y))
    # window.blit(hero, (hero_x, hero_y))

    cyborg.reset(window)

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()
    # if keys_pressed[K_LEFT]:
    #     cyborg_x -= 2
    # if keys_pressed[K_RIGHT]:
    #     cyborg_x += 2
    # if keys_pressed[K_UP]:
    #     cyborg_y -= 2
    # if keys_pressed[K_DOWN]:
    #     cyborg_y += 2

    # if keys_pressed[K_a]:
    #     hero_x -= 2
    # if keys_pressed[K_d]:
    #     hero_x += 2
    # if keys_pressed[K_w]:
    #     hero_y -= 2
    # if keys_pressed[K_s]:
    #     hero_y += 2


    timer.tick(60)
    display.update()