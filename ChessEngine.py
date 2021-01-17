import numpy as np


class Game:
    def __init__(self):
        self.board = np.array([
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['**', '**', '**', '**', '**', '**', '**', '**'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ])
        self.whiteTurn = True  # white has to move
        self.moveLog = []  # list of moves that were made

    def makeMove(self, move):
        # checks if the right piece was selected (white while white's turn or black while black's turn)
        if (self.whiteTurn and move.moved_piece[0] == 'w') or (not self.whiteTurn and move.moved_piece[0] == 'b'):
            self.board[move.end_row][move.end_col] = move.moved_piece
            self.board[move.start_row][move.start_col] = "**"
            self.whiteTurn = not self.whiteTurn  # change player's turn
            self.moveLog.append(move)
        # else does nothing

    def moveBack(self):  # undoes the last move
        if len(self.moveLog) != 0:  # checks to see if a move has been made
            move = self.moveLog.pop()
            self.board[move.start_row][move.start_col] = move.moved_piece
            self.board[move.end_row][move.end_col] = move.captured_piece  # if no piece captured restores blank
            self.whiteTurn = not self.whiteTurn  # changes player's turn

    def moveForward(selfself):  # maybe add later
        pass


"""
This will be made by Antonia
This class should allow the ChessMain script to move pieces
and it should also change the game.board array
"""
class Move:
    def __init__(self, start, end, board):
        self.start_col = start[0]
        self.start_row = start[1] - 1  # always subtract 1 from row
        self.end_col = end[0]
        self.end_row = end[1] - 1
        self.moved_piece = board[self.start_row][self.start_col]  # remember what piece has to be moved
        self.captured_piece = board[self.end_row][self.start_row]  # in case a piece has been captured
