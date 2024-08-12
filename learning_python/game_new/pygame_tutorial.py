from time import sleep
import pygame
from sys import exit

pygame.init()
screen  = pygame.display.set_mode((800,400))#width, height
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

score_surf = font.render("My game", False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))
score_rect.inflate_ip()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

c = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos): print("collision")
    
    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0,300))
    c += 1

    pygame.draw.rect(screen,"#c0e8ec",score_rect)
    screen.blit(score_surf,score_rect)
    
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    
    #if player_rect.colliderect(snail_rect):
    #    print("colllision")
    
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse_pos)):
    #    print( "collision")

    pygame.display.update()
    clock.tick(60)