import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('หมากฮอส')

def main():
    """รันเกม"""
    run = True
    #ช่วยคงที่ FPS ถ้าไม่ทำมันจะเร็วตามเครื่อง(ปิงปองความเร็วแสง)
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #เอาไว้ออกเกม
            #เมื่อกด
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WIN)
        pygame.display.update()
        
    pygame.quit()
    
main()