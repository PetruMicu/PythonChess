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

    '''
    This method checks if a move is valid. It calls another method
    that generates all possible moves considering the rules for each piece
    '''
    def getValidMoves(self):
        return self.generateMoves()

    def generateMoves(self):
        movelist = []  # list containing the possible moves
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                piece_color = self.board[i][j][0]  # 'w' or 'b'
                if (piece_color == 'w' and self.whiteTurn) or (piece_color == 'b' and not self.whiteTurn):
                    piece = self.board[i][j][1]  # P, R, N, B, K, Q
                    if piece == 'P':  # the piece is a pawn
                        self.generatePawnMoves(i, j, movelist)
                    elif piece == 'R':
                        self.generateRookMoves(i, j, movelist)
                    elif piece == 'N':
                        self.generateKnightMoves(i, j, movelist)
                    elif piece == 'B':
                        self.generateBishopMoves(i, j, movelist)
                    elif piece == 'Q':
                        self.generateQueenMoves(i, j, movelist)
                    elif piece == 'K':
                        self.generateKingMoves(i, j, movelist)
        return movelist
    '''
    These methods generate valid moved for a certain piece and stores them in the movelist variable
    The methods are to be called by self.generateMoves()
    '''

    def generatePawnMoves(self, row, col, movelist):
        piece_color = self.board[row][col][0]
        value = 0
        if piece_color == 'w':
            if row == 6 and self.board[row - 2][col] == '**':
                movelist.append(Move((row, col), (row-2, col), self.board))
            value = -1
        elif piece_color == 'b':
            if row == 1 and self.board[row + 2][col] == '**':
                movelist.append(Move((row, col), (row + 2, col), self.board))
            value = 1
        if self.board[row + value][col] == '**':  # square in front of pawn is empty
            movelist.append(Move((row, col), (row + value, col), self.board))
        if col != 0:
            if self.board[row + value][col - 1] != '**':  # pawn can capture a piece to it's left
                movelist.append(Move((row, col), (row + value, col - 1), self.board))
        if col != 7:
            if self.board[row + value][col + 1] != '**':  # pawn can capture a piece to it's right
                movelist.append(Move((row, col), (row + value, col + 1), self.board))
            # do en passant move later if there's time left

    def generateRookMoves(self, row, col, movelist):
        pass

    def generateKnightMoves(self, row, col, movelist):
        pass

    def generateBishopMoves(self, row, col, movelist):
        pass

    def generateQueenMoves(self, row, col, movelist):
        pass

    def generateKingMoves(self, row, col, movelist):
        pass


"""
This will be made by Antonia
This class should allow the ChessMain script to move pieces
and it should also change the game.board array
"""
class Move:
    def __init__(self, start, end, board):
        self.start_col = start[1]
        self.start_row = start[0]
        self.end_col = end[1]
        self.end_row = end[0]
        self.moved_piece = board[self.start_row][self.start_col]  # remember what piece has to be moved
        self.captured_piece = board[self.end_row][self.end_col]  # in case a piece has been captured#

    def __eq__(self, other):  # allows comparing two moves
        if isinstance(other, Move):  # makes sure that other is an instance of the class Move
            return (self.start_row == other.start_row and self.start_col == other.start_col and
                    self.end_row == other.end_row and self.end_col == other.end_col)
        return False