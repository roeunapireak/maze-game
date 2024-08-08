#create a Maze game!
from pygame import *

from spriteClass import GameSprite, Player, Enemy


window = display.set_mode((700, 500))
display.set_caption("Catch")
background = transform.scale(image.load("background.jpg"), (700, 500))

timer = time.Clock()


goal = GameSprite('treasure.png', 300, 250, 4)
player = Player('hero.png', 100, 100, 4)
monster = Enemy('cyborg.png', 100, 100, 4)


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

game = True 

while game:

    window.blit(background, (0,0))

    player.reset(window)
    player.controller()

    monster.reset(window)
    monster.movement()

    goal.reset(window)

    for e in event.get():
        if e.type == QUIT:
            game = False


    timer.tick(60)
    display.update()