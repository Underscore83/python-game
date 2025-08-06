import pygame
import time
pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Birthday Card")

White=(255,255,255)
Pink=(255,192,203)

Font=pygame.font.Font(None, 50)

Cake=pygame.image.load("Cake2.png")
Cake=pygame.transform.scale(Cake,(100,100))

def draw (text, y):
    message=Font.render(text,True,Pink)
    screen.blit(message,(100,y))


running=True

start=time.time()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    screen.fill(White)
    screen.blit(Cake,(250,50))#showcake
    
    #countdown
    
    seconds=int(time.time()-start)
    
    if seconds < 3:
        draw("Get Ready", 200)
        
    elif seconds < 6:
        draw("3... 2... 1", 200)
        
    else:
        draw("Happy Birthday!", 200)
        
    pygame.display.flip()
    
pygame.quit()