import pygame
WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.ellipse(self.image, self.color,[0,0, self.width, self.height])

        self.rect = self.image.get_rect()

    def moveDown(self, speed):
        self.rect.y += self.speed* speed / 20

    def repaint(self, color):
        self.color = color
        #pygame.draw.ellipse(self.image, self.color, [0,0, self.width, self.height])
            
        

        
