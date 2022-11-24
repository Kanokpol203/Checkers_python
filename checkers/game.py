import pygame
from .constants import *
from checkers.board import Board

class game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board,draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.select = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False

    def move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_trun()
        else:
            return False
        
        return True
    
    def change_trun(slif):
        if slif.turn == RED:
            slif.turn == WHITE
        else:
            slif.turn == RED
            