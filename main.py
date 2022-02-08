import pygame
import os
import random


WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong Game!")

RETRO_BLUE = (44,78,114)

BORDER = pygame.Rect(WIDTH/2 - 2,0,4,HEIGHT)
FPS = 60
VEL = 6

AI_VEL = 6


RECTANGLE_WIDTH,RECTANGLE_HEIGHT = 5,60


RECTANGLE_IMAGE = pygame.image.load(os.path.join('Assets','red_rectangle.png'))
RECTANGLE = pygame.transform.scale(RECTANGLE_IMAGE,(RECTANGLE_WIDTH,RECTANGLE_HEIGHT))
BALL = pygame.Rect(WIDTH/2-7.5,HEIGHT/2-7.5,15,15)

def draw_window(P1,P2):
    WIN.fill(RETRO_BLUE)
    pygame.draw.rect(WIN, (255,255,255),BORDER)
    pygame.draw.ellipse(WIN, (255,255,255),BALL)
    WIN.blit(RECTANGLE, (P1.x,P1.y))
    WIN.blit(RECTANGLE,(P2.x,P2.y))
    pygame.display.update()

def P1_handle_movement(keys_pressed, P1):
    if keys_pressed[pygame.K_w]: #P1 UP
             if P1.y > 10:
                 P1.y -= VEL

    if keys_pressed[pygame.K_s]: #P1 DOWN
             if P1.y < HEIGHT - 10-RECTANGLE_HEIGHT:
                 P1.y += VEL


def BALL_restart(ball_vel_x,ball_vel_y):
    BALL.center = (WIDTH/2,HEIGHT/2)
    ball_vel_y *= random.choice((1,-1))
    ball_vel_x *= random.choice((1,-1))
    

def main():
    
    
    ball_vel_y = 7
    ball_vel_x = 7
    P1 = pygame.Rect(40,250,RECTANGLE_WIDTH,RECTANGLE_HEIGHT)
    P2 = pygame.Rect(860,250,RECTANGLE_WIDTH,RECTANGLE_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        P1_handle_movement(keys_pressed,P1)
        #BALL MOVEMENT
        BALL.x += ball_vel_x
        BALL.y += ball_vel_y
        if BALL.top <= 0 or BALL.bottom >= HEIGHT:
            ball_vel_y *= -1
        if BALL.left <= 0 or BALL.right >= WIDTH:
            BALL_restart(ball_vel_x,ball_vel_y)
        
        if BALL.colliderect(P1) or BALL.colliderect(P2):
            ball_vel_x *= -1
        
        #AI MOVEMENT
    
        if P2.top < BALL.y:
            P2.top += AI_VEL
        if P2.bottom > BALL.y:
            P2.bottom -= AI_VEL
        
         
        

                              


        draw_window(P1,P2)
        

    pygame.quit()

if __name__ == "__main__":
    main()
