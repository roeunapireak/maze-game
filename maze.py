#create a Maze game!
from pygame import *

from spriteClass import GameSprite, Player, Enemy, Wall


window = display.set_mode((700, 500))
display.set_caption("Catch")
background = transform.scale(image.load("background.jpg"), (700, 500))

timer = time.Clock()


goal = GameSprite('treasure.png', 550, 400, 4)
player = Player('hero.png', 5, 5, 4)
monster = Enemy('cyborg.png', 300, 300, 4)

wall1 = Wall((102, 255, 51), 100, 30, 15, 350)
wall2 = Wall ((102, 255, 51), 100, 470, 400, 15)
wall3 = Wall((102, 255, 51), 200, 130, 15, 350)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()
font = font.Font(None, 70)
win = font.render("You Won!", 1, (255, 240, 0))

game = True 
finish = False

while game:
    if not finish:
        window.blit(background, (0,0))
        wall1.draw(window)
        wall2.draw(window)
        wall3.draw(window)

        player.reset(window)
        player.controller()

        monster.reset(window)
        monster.auto_move()

        goal.reset(window)

        if sprite.collide_rect(player, goal):
            finish = True
            window.blit(win, (300, 230))

    for e in event.get():
        if e.type == QUIT:
            game = False


    timer.tick(60)
    display.update()