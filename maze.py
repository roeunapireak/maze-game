#create a Maze game!
from pygame import *

from spriteClass import GameSprite, Player, Enemy

window = display.set_mode((700, 500))
display.set_caption("Catch")
background = transform.scale(image.load("background.jpg"), (700, 500))

timer = time.Clock()

width = 600
heigth = 500

player = Player('hero.png', 100, 100, 4)
enemy = Enemy('cyborg.png', 300, 200, 4)
goal = GameSprite('treasure.png', 300, 250, 2)

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

game = True 

while game:
    window.blit(background, (0,0))

    player.reset(window)
    player.controller()

    enemy.reset(window)
    enemy.auto_move()

    goal.reset(window)

    for e in event.get():
        if e.type == QUIT:
            game = False


    timer.tick(60) 
    display.update()