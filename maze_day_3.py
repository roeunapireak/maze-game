#create a Maze game!
from pygame import *

from spriteClass import GameSprite, Player, Enemy
from wallClass import Wall


window = display.set_mode((700, 500))
display.set_caption("Catch")
background = transform.scale(image.load("background.jpg"), (700, 500))

timer = time.Clock()


goal = GameSprite('treasure.png', 550, 400, 4)
player = Player('hero.png', 5, 5, 4)
monster = Enemy('cyborg.png', 300, 300, 4)

# surface with parameters
wall_1 = Wall(RED=154, GREEN=205, BLUE=50, wall_x=100, wall_y=20 , wall_width=450, wall_height=10)
wall_2 = Wall(RED=154, GREEN=205, BLUE=50, wall_x=100, wall_y=480 , wall_width=350, wall_height=10)
wall_3 = Wall(RED=154, GREEN=205, BLUE=50, wall_x=100, wall_y=20 , wall_width=10, wall_height=300)


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
money = mixer.Sound('money.ogg')
lose = font.render('YOU LOSE!', True, (180, 0, 0))
kick = mixer.Sound('kick.ogg')

game = True 

finish = True

while game:
    if finish == True:
        window.blit(background, (0,0))

        player.reset(window)
        player.controller()

        monster.reset(window)
        monster.auto_move()

        goal.reset(window)

        wall_1.draw_wall(window)
        wall_2.draw_wall(window)
        wall_3.draw_wall(window)

    for e in event.get():
        if e.type == QUIT:
            game = False

    lose_1 = sprite.collide_rect(player, monster)
    lose_2 = sprite.collide_rect(player, wall_1)
    lose_3 = sprite.collide_rect(player, wall_2)
    lose_4 = sprite.collide_rect(player, wall_3)

    win_1 = sprite.collide_rect(player, goal)

    if lose_1 or lose_2 or lose_3 or lose_4:
        window.blit(lose, (200, 200))
        finish = False
        kick.play()
    
    if win_1:
        window.blit(win, (200, 200))
        finish = False
        money.play()

    timer.tick(60)
    display.update()