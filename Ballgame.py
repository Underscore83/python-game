import pygame
from pygame.locals import *
pygame.init()


screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("GAME")
Blue=(173, 216, 230)
Red=(255,0,0)
ball=pygame.image.load("ball.gif")
rect=ball.get_rect()
speed=[3,3]
running=True


while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
    rect=rect.move(speed)
    if rect.left < 0 or rect.right > 500:
        speed[0]= - speed[0]
    if rect.top < 0 or rect.bottom > 500:
        speed[1]= - speed[1]
    
    
    screen.fill(Blue)
    pygame.draw.rect(screen, Blue, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()
pygame.quit()