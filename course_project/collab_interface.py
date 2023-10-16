"""Checkers User Interface File:
#
# 1. Build a board in Pygame
# 2. Build pieces
# 3. Linked to the backend
# 4. Add features (i.e. menu, score, difficulties (if applicable))
# 5. End game appropriately

"""
"""User interface for the checkers game. Includes the menu currently, but it could also include the game itself"""

import pygame
import random
import structures


# Initializing pygame
pygame.init()

# Defining colour variables

GREEN = (25, 225, 0)
YELLOW = (225, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 225)
RED = (225, 0, 0)
GREY = (75, 75, 75)
LIGHT_GREY = (150, 150, 150)
BROWN = (100, 50, 0)
PURPLE = (175, 0, 255)
ORANGE = (255, 100, 0)
LIGHT_RED = (229, 48, 36)
BLACK = (5, 5, 5)
SQUARE_SIZE = 75
ROWS, COLS = 8, 8
# Setting up pygame window and initializing score variable
info = pygame.display.Info()
width = 800
height = 800
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)

# Declaring the font variable for text
font = pygame.font.Font('font_files/Plexiglass.ttf', 125)
font_two = pygame.font.Font('font_files/Plexiglass.ttf', 30)

font_three = pygame.font.Font('font_files/Plexiglass.ttf', 75)
font_four = pygame.font.Font('font_files/Plexiglass.ttf', 20)
font_five = pygame.font.Font('font_files/Roboto-Medium.ttf', 30)

# def drawBoard(self):

#
# class Stone(pygame.sprite.Sprite):
#     """
#     A class representing a "stone" (pawn) in a Checkers Game.
#
#     Instance Attributes:
#     - id: a unique identifier for a stone
#     - state: whether a piece is alive or dead (captured); True for alive and False for dead
#     - position: the (x,y) position of the piece in the board matrix
#     - color: True for Red, False for Black
#     - is_king: Whether the stone is a king or not; True if king, false otherwise.
#     """
#
#     ID: int
#     state: bool
#     position: tuple[int, int]
#     color: bool
#     is_king: bool
#
#     def __init__(self, ID, position, colour):
#         """
#         Used to initialize a stone in the beginning of a game.
#         """
#         super().__init__()
#         self.ID = ID
#         self.position = position
#         self.colour = colour
#
#         # self.state and self.is_king are initialized to True and False, respectively
#         self.state = True
#         self.is_king = False
#
#         self.image = pygame.Surface((50, 50)) # replace with actual image
#         self.rect = self.image.get_rect()
#         self.update_position(position)
#
#     def update_position(self, new_position):
#         self.position = new_position
#         self.rect.x = new_position[0] * 50 # replace 50 with size of square
#         self.rect.y = new_position[1] * 50 # replace 50 with size of square
#
#
# class Board:
#     def __init__(self):
#         self.matrix = [[0, 1, 0, 1, 0, 1, 0, 1],
#                        [1, 0, 1, 0, 1, 0, 1, 0],
#                        [0, 1, 0, 1, 0, 1, 0, 1],
#                        [0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0],
#                        [2, 0, 2, 0, 2, 0, 2, 0],
#                        [0, 2, 0, 2, 0, 2, 0, 2],
#                        [2, 0, 2, 0, 2, 0, 2, 0]]
#         self.pieces = pygame.sprite.Group()  # create list to store Stone objects
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[i])):
#                 if self.matrix[i][j] != 0:
#                     position = (j, i) # swap i and j to convert to (x, y) format
#                     colour = True if self.matrix[i][j] == 1 else False
#                     stone = Stone(len(self.pieces), position, colour) # create new Stone object
#                     board.add_stone(stone)
#
#     def add_stone(self, stone):
#         """
#         Adds a stone to the board.
#         """
#         self.matrix[stone.position[1]][stone.position[0]] = stone.ID
#         self.pieces.add(stone)
#
#     def make_move(self, start_pos, end_pos):
#         x1, y1 = start_pos
#         x2, y2 = end_pos
#
#         # check if move is valid
#         # if not self.is_valid_move(start_pos, end_pos):  # if not in possible moves
#         #     return False
#
#         # update matrix
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[i])):
#                 if (j, i) == start_pos:
#                     self.matrix[i][j] = 0
#                 elif (j, i) == end_pos:
#                     piece_color = self.matrix[y1][x1]
#                     is_king = any([p.is_king for p in self.pieces if p.position == start_pos])
#                     self.matrix[i][j] = piece_color
#                     if piece_color == 1 and i == 0:
#                         is_king = True
#                     elif piece_color == 2 and i == 7:
#                         is_king = True
#                     if is_king:
#                         for piece in self.pieces:
#                             if piece.position == start_pos:
#                                 piece.is_king = True
#
#         # update pieces positions
#         for piece in self.pieces:
#             if piece.position == start_pos:
#                 piece.position = end_pos
#             elif piece.position == (x2, y2):
#                 captured_piece_pos = ((x1 + x2) // 2, (y1 + y2) // 2)
#                 for captured_piece in self.pieces:
#                     if captured_piece.position == captured_piece_pos:
#                         captured_piece.state = False
#
#         return True


# def button(xco, yco, w, h, inactive, active, action=None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#
#     if xco + w > mouse[0] > xco and yco + h > mouse[1] > yco:
#         screen.blit(active, (xco, yco))
#         if click[0] == 1 and action is not None:
#             action()
#     else:
#         screen.blit(inactive, (xco, yco))
from structures import CheckersGame
#
# game = CheckersGame()
# stones, matrix = structures.initialize_stones_and_matrix(8)

# Defining functions that draw the menu, how to play screen, quitting, background, the character, and the trash

# Function for drawing the menu
def drawMenu():
    pygame.draw.rect(screen, BLACK, (0, 0, width, height))

    title = font.render('Checkers', True, LIGHT_RED)
    screen.blit(title, pygame.Rect(80, 100, 50, 100))
    # title_two = font.render('text', True, LIGHT_GREY)
    # screen.blit(title_two, pygame.Rect(100, 100, 50, 100))
    subHeading = font_two.render('     BEAT', True, YELLOW)
    screen.blit(subHeading, pygame.Rect(100, 200, 50, 20))
    subHeading_two = font_two.render('            OUR', True, YELLOW)
    screen.blit(subHeading_two, pygame.Rect(200, 200, 50, 20))
    subHeading_three = font_two.render('       NEW', True, YELLOW)
    screen.blit(subHeading_three, pygame.Rect(383, 200, 50, 20))
    subHeading_four = font_two.render('       AI', True, YELLOW)
    screen.blit(subHeading_four, pygame.Rect(538, 200, 50, 20))

    pygame.draw.rect(screen, WHITE, (185, 300, 400, 100))
    pygame.draw.rect(screen, BLACK, (190, 305, 390, 90))
    playButton = font_three.render('PLAY', True, GREEN)
    screen.blit(playButton, pygame.Rect(298, 320, 50, 20))

    pygame.draw.rect(screen, WHITE, (185, 425, 400, 100))
    pygame.draw.rect(screen, BLACK, (190, 430, 390, 90))
    howToPlayButton = font_three.render('GUIDE', True, WHITE)
    screen.blit(howToPlayButton, pygame.Rect(280, 445, 50, 20))

    pygame.draw.rect(screen, WHITE, (185, 550, 400, 100))
    pygame.draw.rect(screen, BLACK, (190, 555, 390, 90))
    terminateButton = font_three.render('EXIT', True, RED)
    screen.blit(terminateButton, pygame.Rect(310, 570, 50, 20))
    #
    # creatorText = font_four.render('SAM, MIMIS, LAKSHMAN AND PETER !!', True, WHITE)
    # screen.blit(creatorText, pygame.Rect(215, 700, 50, 100))

    pygame.display.flip()

from structures import Stone

#TODO
# 1. get stone id from board attribute in checkers class
# 2. get stone class object from the dictionary by indexing with ID
# 3. convert stone object to piece class object so the draw method can be called on it


class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, row, col, color, stone: Stone):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def drawPiece(self, screen):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(screen, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)


def draw_squares(screen):
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(screen, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw(game: CheckersGame, screen):
    draw_squares(screen)
    for row in game.board:
        for id in row:
            if id != -1:
                stone = stones[id]
                if stone.color == 'R':
                    stone.color = (255, 0, 0)
                else:
                    stone.color = (128, 128, 128)
                newpiece = Piece(stone.position[0], stone.position[1], stone.color, stone)
                newpiece.drawPiece(screen)


def create_board(game: CheckersGame, stone: Stone):
    pieceboard = []
    for row in range(ROWS):
        pieceboard.append([])
        for col in range(COLS):
            if col % 2 == ((row + 1) % 2):
                if row < 3:
                    pieceboard.append(Piece(row, col, WHITE, stone))
                elif row > 4:
                    pieceboard[row].append(Piece(row, col, RED, stone))
                else:
                    pieceboard[row].append(0)
            else:
                pieceboard[row].append(0)



# Function for drawing the how to play screen
def drawHowToPlay():
    screen.fill(LIGHT_RED)
    howToText = font_five.render('HOW TO PLAY:', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 50, 50, 20))
    howToText = font_five.render('Black moves first red', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 75, 50, 20))
    howToText = font_five.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 100, 50, 20))
    howToText = font_five.render('', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 125, 50, 20))
    howToText = font_five.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 150, 50, 20))
    howToText = font_five.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 175, 50, 20))
    howToText = font_five.render(',', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 200, 50, 20))
    howToText = font_five.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(50, 225, 50, 20))
    howToText = font_five.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(100, 350, 50, 20))
    howToText = font_four.render(',', True, BLACK)
    screen.blit(howToText, pygame.Rect(25, 380, 50, 20))
    howToText = font_four.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(75, 400, 50, 20))
    howToText = font_five.render('.:', True, BLACK)
    screen.blit(howToText, pygame.Rect(480, 350, 50, 20))
    howToText = font_four.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(425, 380, 50, 20))
    howToText = font_four.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(420, 400, 50, 20))
    howToText = font_four.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(423, 420, 50, 20))
    howToText = font_four.render('.', True, BLACK)
    screen.blit(howToText, pygame.Rect(415, 440, 50, 20))
    howToText = font_five.render('Click anywhere to return to start game', True, BLACK)
    screen.blit(howToText, pygame.Rect(140, 550, 50, 20))
    pygame.display.flip()


# Function for quitting the game
def executeQuitGame():
    quit()


def drawWin():
    screen.fill(BLACK)
    winText = font.render('GAME OVER', True, YELLOW)
    screen.blit(winText, pygame.Rect(100, 240, 50, 20))
    screen.blit(winText, pygame.Rect(90, 360, 50, 20))
    pygame.display.flip()

#
# def drawScreen(character_x, character_y):
#     pygame.draw.rect(screen, GREEN, (0, 0, width, height))
#
#     pygame.draw.rect(screen, ROAD, (0, 575, width, 75))
#     pygame.draw.rect(screen, YELLOW, (0, 610, width, 4))
#
#     pygame.draw.rect(screen, ROAD, (0, 375, width, 75))
#     pygame.draw.rect(screen, ROAD, (0, 450, width, 75))
#     pygame.draw.rect(screen, YELLOW, (0, 450, width, 4))
#     pygame.draw.rect(screen, WHITE, (0, 410, width, 1))
#     pygame.draw.rect(screen, WHITE, (0, 490, width, 1))
#
#     pygame.draw.rect(screen, BROWN, (0, 275, width, 75))
#     pygame.draw.rect(screen, BLACK, (0, 310, width, 3))
#     pygame.draw.rect(screen, GREY, (0, 284, width, 3))
#     pygame.draw.rect(screen, GREY, (0, 297, width, 3))
#     pygame.draw.rect(screen, GREY, (0, 324, width, 3))
#     pygame.draw.rect(screen, GREY, (0, 337, width, 3))
#
#     pygame.draw.rect(screen, ROAD, (0, 100, width, 75))
#     pygame.draw.rect(screen, ROAD, (0, 175, width, 75))
#     pygame.draw.rect(screen, YELLOW, (0, 175, width, 4))
#     pygame.draw.rect(screen, WHITE, (0, 135, width, 1))
#     pygame.draw.rect(screen, WHITE, (0, 215, width, 1))
#
#     pygame.draw.rect(screen, BROWN, (0, 65, width, 35))
#     pygame.draw.rect(screen, GREY, (0, 74, width, 3))
#     pygame.draw.rect(screen, GREY, (0, 87, width, 3))
#
#     pygame.draw.circle(screen, PLAYER, (character_x, character_y), 10)
#     pygame.display.flip()


# Defining time, and location of character varaibles
myClock = pygame.time.Clock()
running = True
character_x = width // 2
character_y = 675

# Defining the game toggle variable
menu = True
playGame = False
howToPlay = False
quitGame = False
win = False

# Main game loop
while running:

    for evnt in pygame.event.get():  # Code for checking all events
        if evnt.type == pygame.QUIT:
            running = False

        # Checking for the menu screen toggle
        if menu:
            drawMenu()
            character_x = width // 2
            character_y = 675
            pygame.display.flip()

            # Checking for mouse clicks on button
            if evnt.type == pygame.MOUSEBUTTONUP:
                mx, my = evnt.pos
                if mx > 185 and mx < 185 + 400 and my > 305 and my < 305 + 90:
                    playGame = True
                    menu = False
            if evnt.type == pygame.MOUSEBUTTONUP:
                mx, my = evnt.pos
                if mx > 155 and mx < 155 + 390 and my > 430 and my < 430 + 90:
                    howToPlay = True
                    menu = False
            if evnt.type == pygame.MOUSEBUTTONUP:
                mx, my = evnt.pos
                if mx > 155 and mx < 155 + 390 and my > 555 and my < 555 + 90:
                    quitGame = True

    # Checking for start game
    if playGame == True:
        game = CheckersGame()
        stones = game.stones
        matrix = game.board

        draw_squares(screen)
        # draw(game, screen)
        # create_board(game, stone)

        # Update the screen
        pygame.display.update()

        # ##ACTUALLY PLAY GAME AT THIS POINT

        ## BACK TO MENU BUTTON FROM BOARD DISPLAY


        for evnt in pygame.event.get():  # Code for checking all events
            if evnt.type == pygame.QUIT:
                running = False

            # Checking for mouse clicks on button
            if evnt.type == pygame.MOUSEBUTTONUP:
                mx, my = evnt.pos
                if mx > 700 and mx < 800 and my > 0 and my < 100:
                    menu = True
                    playGame = False
                    # THIS WORKS BUT HAVE TO WAIT AFTER FIRST CLICK (TAKES A COUPLE SECONDS)


        ## BACK TO MENU BUTTON FROM BOARD DISPLAY END



        pygame.display.flip()  # Updating or refreshing the frames of pygame
        myClock.tick(60)  # Makes pygame run smoother through FPS, using this code

        #     # Checking for end result
        # if no pieces left / no moves left:
        #     win = True
        #     pygame.display.flip()

    # Checking for player win
    if win == True:
        drawWin()
    # Checking for how to play screen toggle
    if howToPlay == True:
        drawHowToPlay()
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            howToPlay = False
            menu = True
            pygame.display.flip()

    # Checking to quit the game
    if quitGame == True:
        executeQuitGame()

# Exiting pygame
quit()
