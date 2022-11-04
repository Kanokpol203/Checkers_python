import pygame
from checkers.constants import WIDTH, HEIGHT

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('หมากฮอส')

def main():
    """รันเกม"""
    run = True
    #ช่วยคงที่ FPS
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #เอาไว้ออกเกม
            #เมื่อกด
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
main()