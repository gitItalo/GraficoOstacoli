import pygame
import math
        
width = 1000
height = 1000

pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Gioco!')
clock = pygame.time.Clock()

i = 360
z=360
#======================================
verticeSx1=[500,490]
verticeDx1=[200,20]
    
verticeSx2=[680,490]
verticeDx2=[150,20]
def grafica():
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
    global xcenter
    rad = math.radians(angle)
    xcenter = center[0]; ycenter = center[1]
    x = xcenter + radius * math.cos(rad)
    y = ycenter + radius * math.sin(rad)
    return [x,y]
def movimento():
    global z,i,c,p;
    z -= 1
    if z == 0:
        i -= 1
        z = 360
    p = XYCirconference([510,500],190,i)
    c =XYCirconference([p[0],p[1]],130,z)
def braccio1():
        z=360
        i = 360
        z -= 1
        if z == 0:
           i -= 1
           z = 360
        p = XYCirconference([510,500],190,i)
        c = XYCirconference([p[0],p[1]],130,z)
        #pygame.draw.circle(screen,(255,255,255),(490,500),10,2)
        pygame.draw.rect(screen,(255,55,44),(int(p[0]),int(p[1]),200,20),1)    
        
#======================================




u=0
done = False
try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((0,0,0))                      
        

        movimento()
        grafica()
        
        braccio1()
        ostacoli()
        pygame.display.update()
        clock.tick(300)
finally:
    pygame.quit()
