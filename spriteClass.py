from pygame import *

class GameSprite(sprite.Sprite):
    ''' constructor ''' 
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # self.image = transform.scale(image.load(player_image), (player_x, player_y))
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.speed = player_speed

    '''  method '''
    def reset(self, screen_oject):
        self.screen_oject = screen_oject
        screen_oject.blit(self.image, (self.rect.x, self.rect.y))



# chill class of GameSprite
class Player(GameSprite):
    
    def controller(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

# chill class of GameSprite
class Enemy(GameSprite):

    direction = 'left'
    right_rect = 600

    def auto_move(self):
        if self.rect.x <= self.right_rect - 200:
            self.direction = 'right'
        if self.rect.x >= self.right_rect:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__()
        self.image = Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color)
    
    def draw(self, screen_obj):
        screen_obj.blit(self.image, (self.rect.x, self.rect.y))
