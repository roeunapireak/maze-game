from pygame import *

class GameSprite(sprite.Sprite):
    ''' constructor ''' 
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_x, player_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    '''  method '''
    def reset(self, screen_oject):
        self.screen_oject = screen_oject
        screen_oject.blit(self.image, (self.rect.x, self.rect.y))

