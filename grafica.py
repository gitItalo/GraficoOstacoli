import pygame
import math
        
width = 1000
height = 1000

pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Gioco!')
clock = pygame.time.Clock()
#======================================
verticeSx1=[500,490]
verticeDx1=[200,20]
    
verticeSx2=[680,490]
verticeDx2=[150,20]
def grafica(p,c):
    global verticeSx1, verticeDx2,verticeDx1,verticeSx2
    
    pygame.draw.rect(screen,(255,255,0),(verticeSx1[0],verticeSx1[1],verticeDx1[0],verticeDx1[1]),2)
    pygame.draw.rect(screen,(255,0,255),(verticeSx2[0],verticeSx2[1],verticeDx2[0],verticeDx2[1]),2)
    pygame.draw.circle(screen,(255,255,255),(510,500),190,2)
    pygame.draw.circle(screen,(255,255,255),(510,500),320,2)
    pygame.draw.circle(screen,(255,255,255),(510,500),2,2)
    
def ostacoli():
    pygame.draw.polygon(screen,(0,255,255),[[400,300],[400,350],[350,325]],2)
    pygame.draw.polygon(screen,(0,255,255),[[200,800],[200,850],[150,825]],2)
    pygame.draw.rect(screen,(255,232,76),(800,0,200,1000),2)
    
def XYCirconference(center, radius, angle):
    
    rad = math.radians(angle)
    xcenter = center[0]; ycenter = center[1]
    x = xcenter + radius * math.cos(rad)
    y = ycenter + radius * math.sin(rad)
    return [x,y]
def movimento():
    pass
        
#======================================



done = False
try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        for i in range(361):
            p = XYCirconference([500,500],190,i)
            for z in range(361):
                c = XYCirconference([p[0],p[1]],140,z)
                pygame.draw.circle(screen,(255,25,25),(int(c[0]),int(c[1])),50)
           
        grafica(p,c)
        movimento()
        ostacoli()
        pygame.display.update()
        screen.fill((0,0,0))
        clock.tick(60)
finally:
    pygame.quit()
