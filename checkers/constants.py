"""ที่เก็บตัวแปรของเกม"""
import pygame

#ความสูง, ความกว้าง, จำนวนคอลลั่มถ้าอยากปรับ
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#สีที่พิกัส RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
BROWN_DARK = (133, 94, 66)
BROWN_WHITE = (191,153,114)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))

