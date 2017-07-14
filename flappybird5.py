import pygame
import random

pygame.init()

black = (0,0,0)
white = (255,0,255)
green = (0,255,0)
red = (255,0,0)

size = (400,667)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock()
flappyBird = pygame.image.load('Flappy_Bird.png')
flappyBird = pygame.transform.scale(flappyBird,(25,25))
x = 70
y = 250
frameTracker = 0 
x_speed = 0
y_speed = 0
ground = 477
xloc=700
yloc = 0
xsize = 70
ysize = random.randint(0,350)
space = 150
obspeed = 2.5
#add global tracker of score
score = 0
gameOver = False
acc = 0.4

def obstacles(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])

def ball(x,y):
    
    screen.blit(flappyBird,(x,y))
    

def gameover():
    font = pygame.font.SysFont(None,75)
    text = font.render("Game Over ",True,red)
    screen.blit(text, [150,250])
    gameOver = True 

#function to write score being kept
def Score(score):
    font = pygame.font.SysFont(None,75)
    #we use str to convert score value to string for display
    text = font.render("Score: "+str(score),True,black)
    #top left corner coordinates
    screen.blit(text, [0,0])
 
  
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               y_speed = -7
                
        if (event.type == pygame.K_SPACE and gameOver):        
            restart();
            
    screen.fill(white)    
    obstacles(xloc,yloc,xsize,ysize)
    ball(x,y) 
    
    y_speed += acc
    y += y_speed
  


    
   
    #if the ball is between to obstacles 
    Score(score)
    
    
    xloc -= obspeed
    
    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0
    
    #if we hit obstacles in the top block
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 0
        
    #if we hit obstacles in the top block
    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 0
    
    #if obstacle location X is 
    if xloc < -80:
        xloc = 700
        ysize = random.randint(0,350)
    
    #check if obstacle was passed adding to score
    if x > xloc and x < xloc+3:
        score = (score + 1)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
    
    