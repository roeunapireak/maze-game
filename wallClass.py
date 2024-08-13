from pygame import *

class Wall(sprite.Sprite):
    def __init__(self, RED, GREEN, BLUE, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.RED = RED
        self.GREEN = GREEN
        self.BLUE = BLUE
        self.width = wall_width
        self.height = wall_height

        # picture of the wall — a rectangle of the desired size and color
        self.image = Surface((self.width, self.height))
        self.image.fill((RED, GREEN, BLUE)) # RGB Color

        # each sprite must store a rect property
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self, screan):
        screan.blit(self.image, (self.rect.x, self.rect.y))