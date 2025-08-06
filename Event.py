import pygame
from pygame.locals import *
pygame.init()

width=400
height=600


screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("ROCKET in SPACE")
Black=(0,0,0)
Red=(255,0,0)
clock=pygame.time.Clock()
fps=60

#rocket class

class rocket (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,30))
        self.image.fill(Red)
        self.rect=self.image.get_rect()
        self.rect.center=(width//2,height//2)
        self.speed=5
        
    def update(self,keys):
        if keys[K_LEFT]:
            self.rect.x-=self.speed
        if keys[K_RIGHT]:
            self.rect.x+=self.speed
        if keys[K_UP]:
            self.rect.y-=self.speed
        if keys[K_DOWN]:
            self.rect.y+=self.speed


#create rocket object

Rocket=rocket()

all_sprites=pygame.sprite.Group()
all_sprites.add(Rocket)

#gameloop

running=True

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        
    key=pygame.key.get_pressed()
    Rocket.update(key)
    
    screen.fill(Black)
    all_sprites.draw(screen)
    
    pygame.display.flip()    
pygame.quit()