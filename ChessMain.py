import pygame as p
import ChessEngine

"""
This file is responsible for user input, loading graphics.
It's using the GameENgine script to print the current state of the game
"""

# Global variables used for drawing the window
W_HEIGHT = 640
W_WIDTH = 512
HEIGHT = 512
WIDTH = 512
BOARD_SIZE = 8
SQ_SIZE = HEIGHT // BOARD_SIZE
FPS = 15  # frameRate for the animation
colors = [p.Color("white"), p.Color(54, 131, 31, 200)]
IMG = {}  # dictionary containing the images
highlight_colors = [p.Color(244, 241, 174, 155), p.Color(173, 227, 156, 155)]

def loadIMG():
    pieces = ('bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wP')
    # we store the pictures in the IMG dictionary in order to access them later
    for i in range(len(pieces)):
        IMG[pieces[i]] = p.transform.scale(p.image.load("images/" + pieces[i] + ".png"), (SQ_SIZE,SQ_SIZE))


def main():
    p.init()
    window = p.display.set_mode((W_WIDTH, W_HEIGHT))
    time = p.time.Clock()
    window.fill(p.Color("black"))
    gamestate = ChessEngine.Game()
    validMoves = gamestate.getValidMoves()
    move_made = False
    loadIMG()
    loop = True
    squareSelected = ()  # this tuple holds the last click that was made (col,row)
    clicks = []  # two tuples meaning click 1 -> piece selected and click 2-> piece moved
    highlight = False
    row = -1
    col = -1
    while(loop):
        for e in p.event.get():
            if e.type == p.QUIT:  # quit the game
                loop = False
            elif e.type == p.MOUSEBUTTONDOWN:  # player selected a square
                cursorposition = p.mouse.get_pos()
                # map the cursor position to dimensions needed for the board
                row = cursorposition[1] // SQ_SIZE
                col = cursorposition[0] // SQ_SIZE
                if squareSelected == (row-1, col):  # player clicked the same sq twice
                    # clears the clicks
                    highlight = False
                    squareSelected = ()
                    clicks = []
                else:
                    squareSelected = (row-1, col)
                    clicks.append(squareSelected)  # adds the last click
                if len(clicks) == 1:  # player selected a piece, so highlight it
                    if row == 0 or row == 9:
                        highlight = False
                        squareSelected = ()
                        clicks = []
                    elif gamestate.board[row-1][col] != "**":
                        highlight = True
                    else:
                        highlight = False
                        squareSelected = ()
                        clicks = []
                if len(clicks) == 2:
                    move = ChessEngine.Move(clicks[0], clicks[1], gamestate.board)
                    if move in validMoves:
                        gamestate.makeMove(move)
                        move_made = True
                    highlight = False
                    clicks = []
                    squareSelected = []
            elif e.type == p.KEYDOWN and e.key == p.K_z:
                gamestate.moveBack()
                highlight = False
                clicks = []
                squareSelected = []

        if move_made:
            validMoves = gamestate.getValidMoves()
        drawBoard(window, gamestate, highlight, col, row-1)
        time.tick(FPS)
        p.display.flip()


def drawBoard(window, gamestate, highlight, highlight_col, highlight_row):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if highlight_row == i and highlight_col == j and highlight and gamestate.board[i][j] != "**":
                if (i+j) % 2 == 1:
                    p.draw.rect(window, highlight_colors[1], p.Rect(j*SQ_SIZE, (i+1)*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    p.draw.rect(window, highlight_colors[0], p.Rect(j*SQ_SIZE, (i+1)*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                if (i+j) % 2 == 1:
                    p.draw.rect(window, colors[1], p.Rect(j*SQ_SIZE, (i+1)*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    p.draw.rect(window, colors[0], p.Rect(j*SQ_SIZE, (i+1)*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if gamestate.board[i][j] != "**":
                window.blit(IMG[gamestate.board[i][j]], p.Rect(j*SQ_SIZE, (i+1)*SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == '__main__':
    main()