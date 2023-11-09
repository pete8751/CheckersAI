"""CSC111 Final Project: Checkers & Decision Trees

Module Description
==================
This module contains all constants and functions required for showing the game and all the visual representations
regarding progression of a game. The game is our main visualization and shows how well the AI perform against a
Random player.

Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
"""

import pygame
from structures import CheckersGame, Move, Stone
from simulation import run_game
from players import PrunelessMinimaxer, Randomizer, PrunefulMinimaxer, AdvancedAggressor

pygame.init()

# Constants
BLACK = (0, 0, 0)
RED = (225, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (150, 150, 150)
GREEN = (25, 225, 0)
YELLOW = (225, 255, 0)
BLUE = (0, 100, 225)
GREY = (75, 75, 75)
ORANGE = (255, 165, 0)
LIGHT_RED = (229, 48, 36)
TEAL = (0, 255, 255)

SQUARE_SIZE = 100
ROWS, COLS = 8, 8

# Generate pygame window data
width = 800
height = 800
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)

info = pygame.display.Info()

# Generating fonts
font = pygame.font.Font('font_files/Plexiglass.ttf', 125)
font_two = pygame.font.Font('font_files/Plexiglass.ttf', 30)
font_three = pygame.font.Font('font_files/Plexiglass.ttf', 75)
font_four = pygame.font.Font('font_files/Plexiglass.ttf', 50)
font_five = pygame.font.Font('font_files/Roboto-Medium.ttf', 30)
font_six = pygame.font.Font('font_files/Star Trek_future.ttf', 45)

class Piece:
    """Class for drawing each individual stone. This class has been separated to divide the backend from the front end;
    stone is a class used for the algorithms that generate a gameboard, however Piece is used to transfer the stone
    data to the front end so that it can be drawn. It takes in the row, column and colour of the stone it retrieves
    by accessing the CheckersGame.stones dictionary with the id from the CheckersGame.board. It uses this data to
    calculate where the piece should be drawn on the screen, using the calculate_position method, and the colour it
    should be, which is done in the drawPiece function. This class and its methods are integral to drawing each
    board."""

    def __init__(self, row, column, colour):
        self.row = row
        self.column = column
        self.colour = colour
        self.xco = 0
        self.yco = 0
        self.calculate_position()

    def calculate_position(self):
        """Calculate the x and y coordinates of a piece given its stone position."""
        self.xco = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.yco = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def drawPiece(self, screen: pygame.Surface) -> None:
        """Draw the piece based on the stone data and its calculated position. Use a small grey outline to make the
        pieces look smoother."""
        radius = SQUARE_SIZE // 2 - 15
        pygame.draw.circle(screen, GREY, (self.xco, self.yco), radius + 2)
        pygame.draw.circle(screen, self.colour, (self.xco, self.yco), radius)


# Draw functions - for the menu, how to play screen and end screen

def draw_menu() -> None:
    """A function that draws the menu/user interface."""
    pygame.draw.rect(screen, BLACK, (0, 0, width, height))

    title = font.render('Checkers', True, LIGHT_RED)
    screen.blit(title, pygame.Rect(80, 100, 50, 100))
    subheading = font_two.render('     WATCH', True, YELLOW)
    screen.blit(subheading, pygame.Rect(100, 200, 50, 20))
    subheading2 = font_two.render('              OUR', True, YELLOW)
    screen.blit(subheading2, pygame.Rect(200, 200, 50, 20))
    subheading3 = font_two.render('        NEW', True, YELLOW)
    screen.blit(subheading3, pygame.Rect(383, 200, 50, 20))
    subheading4 = font_two.render('       AI', True, YELLOW)
    screen.blit(subheading4, pygame.Rect(538, 200, 50, 20))

    # Drawing the rectangles for buttons in the menu
    pygame.draw.rect(screen, WHITE, (185, 300, 400, 100))
    pygame.draw.rect(screen, BLACK, (190, 305, 390, 90))
    play = font_three.render('PLAY', True, GREEN)
    screen.blit(play, pygame.Rect(298, 320, 50, 20))

    pygame.draw.rect(screen, WHITE, (185, 425, 400, 100))
    pygame.draw.rect(screen, BLACK, (190, 430, 390, 90))
    guide = font_three.render('GUIDE', True, WHITE)
    screen.blit(guide, pygame.Rect(280, 445, 50, 20))

    pygame.draw.rect(screen, WHITE, (185, 550, 400, 100))
    pygame.draw.rect(screen, BLACK, (190, 555, 390, 90))
    exit_button = font_three.render('EXIT', True, RED)
    screen.blit(exit_button, pygame.Rect(310, 570, 50, 20))

    pygame.display.flip()


def draw_choose_AI() -> None:
    """A function that draws the screen after someone presses play. It includes buttons for each AI combination"""
    pygame.draw.rect(screen, BLACK, (0, 0, width, height))

    title = font.render('Choose AI', True, GREEN)
    screen.blit(title, pygame.Rect(80, 100, 50, 100))

    # Drawing the rectangles for buttons in the menu
    button_width = 350
    button_height = 100
    spacing = 30

    x_start = 45
    y_start = 250

    for i in range(4):
        y = y_start + (button_height + spacing) * i
        pygame.draw.rect(screen, WHITE, (x_start, y, button_width, button_height))
        pygame.draw.rect(screen, BLACK, (x_start + 5, y + 5, button_width - 10, button_height - 10))

    ai_1 = font_six.render('Pruneless V Random', True, ORANGE)
    screen.blit(ai_1, pygame.Rect(x_start + 45, y_start + 20, 50, 20))

    ai_2 = font_six.render('Pruneful V Random', True, ORANGE)
    screen.blit(ai_2, pygame.Rect(x_start + 46, y_start + 150, 50, 20))

    ai_3 = font_six.render('Pruneful V Pruneless', True, ORANGE)
    screen.blit(ai_3, pygame.Rect(x_start + 32, y_start + 280, 50, 20))

    ai_4 = font_six.render('Pruneful V Aggressor', True, ORANGE)
    screen.blit(ai_4, pygame.Rect(x_start + 30, y_start + 410, 50, 20))

    x_start = 400

    for i in range(4):
        y = y_start + (button_height + spacing) * i
        pygame.draw.rect(screen, WHITE, (x_start, y, button_width, button_height))
        pygame.draw.rect(screen, BLACK, (x_start + 5, y + 5, button_width - 10, button_height - 10))

    ai_5 = font_six.render('Random V Pruneless', True, ORANGE)
    screen.blit(ai_5, pygame.Rect(x_start + 45, y_start + 20, 50, 20))

    ai_6 = font_six.render('Random V Pruneful', True, ORANGE)
    screen.blit(ai_6, pygame.Rect(x_start + 46, y_start + 150, 50, 20))

    ai_7 = font_six.render('Pruneless V Pruneful', True, ORANGE)
    screen.blit(ai_7, pygame.Rect(x_start + 32, y_start + 280, 50, 20))

    ai_8 = font_six.render('Aggressor V Pruneful', True, ORANGE)
    screen.blit(ai_8, pygame.Rect(x_start + 30, y_start + 410, 50, 20))

    pygame.display.flip()


def draw_squares(screen: pygame.Surface) -> None:
    """A function that draws the gameboard by filling the screen with red and drawing black squares in every other
    position in each row and column."""
    screen.fill(RED)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(screen, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# changed input to list from game.board
def draw(game: CheckersGame, screen: pygame.Surface) -> None:
    """Given a game_state, using the board attribute of that game_state, draw the state of the checkers board.
    draw_sqaures draws the red and black squares and drawPiece draws the pieces on the correct squares."""
    draw_squares(screen)
    for row in game.board:
        for id in row:
            if id != -1:
                stone = game.stones[id]
                if stone.color == 'R':
                    colour = (255, 0, 0)
                else:
                    colour = (128, 128, 128)
                newpiece = Piece(stone.position[0], stone.position[1], colour)
                newpiece.drawPiece(screen)


def draw_boards(game_states: list[CheckersGame]) -> None:
    for game_state in game_states:
        pygame.time.wait(500)  # time delay between moves
        draw_squares(screen)
        draw(game_state, screen)
        screen.blit(pygame.transform.rotate(screen, 90), (0, 0))  # rotate the screen so the board is horizontal
        pygame.display.flip()


# Function for drawing the how to play screen
def draw_guide() -> None:
    """Draw the screen the pops up after guide is selected."""
    screen.fill(BLACK)
    howtotext = font_six.render('Welcome to our final project for CSC111!!', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(75, 50, 50, 20))
    howtotext = font_six.render(
        'This screen explains the rules and assumptions made', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 90, 50, 20))
    howtotext = font_six.render('in this simulation of a checkers game. The game of', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 130, 50, 20))
    howtotext = font_six.render('checkers is played with 12 red and 12 black pieces.', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 170, 50, 20))
    howtotext = font_six.render('These pieces begin, and can only move between black', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 210, 50, 20))
    howtotext = font_six.render('squares. As a simplifying assumption stones cannot', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 250, 50, 20))
    howtotext = font_six.render('become kings and are useless once they reach their', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 290, 50, 20))
    howtotext = font_six.render('respective furthest row. Additionally, pieces', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 330, 50, 20))
    howtotext = font_six.render('cannot change direction in the case of capturing', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 370, 50, 20))
    howtotext = font_six.render('more than one stone at once. We have eight', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 410, 50, 20))
    howtotext = font_six.render('total options on different AI combinations you can', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 450, 50, 20))
    howtotext = font_six.render('run. The option on the left side of the button is', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 490, 50, 20))
    howtotext = font_six.render('the black side for that simulation. Please double', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 530, 50, 20))
    howtotext = font_six.render('click every button in the menu. We hope you', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 570, 50, 20))
    howtotext = font_six.render('enjoy watching the ways the different AIs behave!', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 610, 50, 20))
    howtotext = font_six.render('Note* you may need to force quit the window.', True, LIGHT_RED)
    screen.blit(howtotext, pygame.Rect(30, 650, 50, 20))
    howtotext = font_six.render('Click here to return to the menu.', True, WHITE)
    screen.blit(howtotext, pygame.Rect(150, 690, 50, 20))
    pygame.display.flip()


def draw_win(game: CheckersGame) -> None:
    """Draw the screen the pops up when the game ends. It will slightly differ based on who wins."""
    screen.fill(BLACK)
    winText = font.render('GAME OVER', True, YELLOW)
    screen.blit(winText, pygame.Rect(50, 100, 50, 20))
    if game.get_winner() == 'R':
        text = font_three.render('RED WINS!', True, RED)
        screen.blit(text, pygame.Rect(199, 250, 50, 20))
    else:
        text = font_three.render('BLACK WINS!', True, WHITE)
        screen.blit(text, pygame.Rect(175, 250, 50, 20))

    win_caption = font_two.render('Hope you found this simulation '
                                  'interesting!', True, YELLOW)
    screen.blit(win_caption, pygame.Rect(55, 350, 50, 20))
    win_caption_2 = font_two.render('We encourage you to run through each AI!', True, YELLOW)
    screen.blit(win_caption_2, pygame.Rect(50, 450, 50, 20))
    win_caption3 = font_two.render('You may close this window whenever you', True, YELLOW)
    screen.blit(win_caption3, pygame.Rect(60, 550, 50, 20))
    win_caption4 = font_two.render('are ready.', True, YELLOW)
    screen.blit(win_caption4, pygame.Rect(325, 650, 50, 20))


# Main game loop function
def games() -> None:
    # Define a clock and run it at 60 FPS so that the game runs smoothly
    # global evnt, evnt
    myClock = pygame.time.Clock()
    myClock.tick(60)

    # Defining variables to trigger different actions
    menu = True
    play_game = False
    is_guide = False
    quitGame = False
    running = True

    a1 = False
    a2 = False
    a3 = False
    a4 = False
    a5 = False
    a6 = False
    a7 = False
    a8 = False

    while running:

        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                running = False

            # Triggering the menu screen
            if menu:
                draw_menu()
                pygame.display.flip()

                # Check if mouse clicks on button positions
                if evnt.type == pygame.MOUSEBUTTONUP:
                    mx, my = evnt.pos
                    if mx > 185 and mx < 185 + 400 and my > 305 and my < 305 + 90:
                        play_game = True
                        menu = False
                    if mx > 155 and mx < 155 + 390 and my > 430 and my < 430 + 90:
                        is_guide = True
                        menu = False
                    if mx > 155 and mx < 155 + 390 and my > 555 and my < 555 + 90:
                        quitGame = True

        # If the play button is clicked run the game.
        if play_game:
            draw_choose_AI()
            pygame.display.flip()

            for eve in pygame.event.get():
                if eve.type == pygame.MOUSEBUTTONUP:
                    m_x, m_y = eve.pos

                    if 45 < m_x < 395:
                        if 250 < m_y < 350:
                            a1 = True
                        if 380 < m_y < 480:
                            a2 = True
                        if 510 < m_y < 610:
                            a3 = True
                        if 640 < m_y < 740:
                            a4 = True
                    if 400 < m_x < 750:

                        if 250 < m_y < 350:
                            a5 = True
                        if 380 < m_y < 480:
                            a6 = True
                        if 510 < m_y < 610:
                            a7 = True
                        if 640 < m_y < 740:
                            a8 = True

            if a1:
                prun = PrunelessMinimaxer(3)
                rando = Randomizer()
                existing_game, winner = run_game(prun, rando)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                pygame.time.delay(2000)
                play_game = False
                draw_win(existing_game)

            if a2:
                prun = PrunefulMinimaxer(3)
                random1 = Randomizer()
                existing_game, winner = run_game(prun, random1)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                play_game = False
                draw_win(existing_game)

            if a3:
                prunful = PrunefulMinimaxer(3)
                prunless = PrunelessMinimaxer(3)
                existing_game, winner = run_game(prunful, prunless)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                play_game = False
                draw_win(existing_game)

            if a4:
                prunful = PrunefulMinimaxer(3)
                agress = AdvancedAggressor('R', 3)
                existing_game, winner = run_game(prunful, agress)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                play_game = False
                draw_win(existing_game)

            if a5:
                prun = PrunelessMinimaxer(3)
                rando = Randomizer()
                existing_game, winner = run_game(rando, prun)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                play_game = False
                draw_win(existing_game)

            if a6:
                print('**********************************************')
                prun = PrunefulMinimaxer(3)
                random1 = Randomizer()
                existing_game, winner = run_game(random1, prun)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                play_game = False
                draw_win(existing_game)

            if a7:
                prunful = PrunefulMinimaxer(3)
                prunless = PrunelessMinimaxer(3)
                existing_game, winner = run_game(prunless, prunful)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                play_game = False
                draw_win(existing_game)

            if a8:
                prunful = PrunefulMinimaxer(3)
                agress = AdvancedAggressor('B', 3)
                existing_game, winner = run_game(agress, prunful)
                create_game = CheckersGame()
                moves = existing_game.get_moves()
                game_states = game_state_generator(moves, create_game)
                draw_boards(game_states)
                play_game = False
                draw_win(existing_game)

            pygame.display.flip()

        # Triggering guide button
        if is_guide:
            draw_guide()
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                is_guide = False
                menu = True
                pygame.display.flip()

        # Triggering exit button
        if quitGame:
            quit()


# Helper: We need this function to get a list of gamestates based on which visual of the game works, by calling
# the draw_boards function.
def game_state_generator(lst_moves: list[Move], game: CheckersGame) -> list[CheckersGame]:
    """
    Given a list of moves, this function returns a list of sequentially updated game state (i.e. CheckersGame objects)
    by utilizing the CheckersGame.copy_and_record method.
    """
    lst = [game]
    for move in lst_moves:
        new_game = game.copy_and_record_move(move)
        lst.append(new_game)
        game = new_game

    return lst


# If you run this main file, the game runs.
if __name__ == '__main__':
    games()
    quit()
