import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('หมากฮอส')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    """รันเกม"""
    run = True
    #ช่วยคงที่ FPS ถ้าไม่ทำมันจะเร็วตามเครื่อง(ปิงปองความเร็วแสง)
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #เอาไว้ออกเกม
            #เมื่อกด
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos =  pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
    
        game.update()
        
    pygame.quit()
    
main()