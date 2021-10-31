#importing library
import pygame, sys, random
from pygame.locals import *
pygame.init()

#setting up clcok
clock = pygame.time.Clock()

#setting up screen
screen = pygame.display.set_mode((900,550))
pygame.display.set_caption("Pong by Fdev")

#set players early socre
p1_score = 0
p2_score = 0

#defining font
font = pygame.font.SysFont(None, 100)

#defining drawing font function
def draw_text(msg, x, y):
    text = font.render(msg, True, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text, (x,y))

p2_vel = 5

#defining objects rect
ball_rect = pygame.Rect(450,275,50,50)
ball_rect.center = [450,275]

line_rect = pygame.Rect(450,0,10,550)

paddle1_rect = pygame.Rect(100,275,40,200)
paddle1_rect.center = [100,275]

paddle2_rect = pygame.Rect(800,275,40,200)
paddle2_rect.center = [800,275]

velocity_x = 5
velocity_y = 5

#main game loop
run = True
while run:
    ball_rect.x += velocity_x
    ball_rect.y += velocity_y

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if ball_rect.right > 900:
        velocity_x = 0 - velocity_x
        p1_score += 1
    if ball_rect.left < 0:
        velocity_x = 0 - velocity_x
        p2_score += 1
    if ball_rect.top < 0:
        velocity_y = 0 - velocity_y
    if ball_rect.bottom > 550:
        velocity_y = 0 - velocity_y
    if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
        velocity_x = 0 - velocity_x
        velocity_y = 0 - velocity_y

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and paddle1_rect.top > 0:
        paddle1_rect.y -= 10
    if key[pygame.K_DOWN] and paddle1_rect.bottom < 550:
        paddle1_rect.y += 10

    paddle2_rect.y += p2_vel
    if paddle2_rect.top > 0:
        p2_vel = 0 - p2_vel
    if paddle2_rect.bottom < 550:
        p2_vel = 0 - p2_vel
        

    draw_text(str(p1_score), 175, 50)

    draw_text(str(p2_score), 900-200, 50)

    pygame.draw.rect(screen, (255,255,255), line_rect)
    
    pygame.draw.rect(screen, (255,255,255), paddle1_rect)

    pygame.draw.rect(screen, (255,255,255), paddle2_rect)

    pygame.draw.ellipse(screen, (255,255,255), ball_rect)

    clock.tick(60)
    pygame.display.update()
