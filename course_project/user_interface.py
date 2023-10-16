# """User interface for the checkers game. Includes the menu currently, but it could also include the game itself"""
#
# import pygame
# import random
# import structures
#
# # Initializing pygame
# pygame.init()
#
# # Defining colour variables
#
# GREEN = (25, 225, 0)
# YELLOW = (225, 255, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 100, 225)
# RED = (225, 0, 0)
# GREY = (75, 75, 75)
# LIGHT_GREY = (150, 150, 150)
# BROWN = (100, 50, 0)
# PURPLE = (175, 0, 255)
# ORANGE = (255, 100, 0)
# LIGHT_RED = (229, 48, 36)
# BLACK = (5, 5, 5)
#
# # Setting up pygame window and initializing score variable
# info = pygame.display.Info()
# width = 800
# height = 800
# SIZE = (width, height)
# screen = pygame.display.set_mode(SIZE)
#
# # Declaring the font variable for text
# font = pygame.font.Font('font_files/Plexiglass.ttf', 125)
# font_two = pygame.font.Font('font_files/Plexiglass.ttf', 30)
#
# font_three = pygame.font.Font('font_files/Plexiglass.ttf', 75)
# font_four = pygame.font.Font('font_files/Plexiglass.ttf', 20)
# font_five = pygame.font.Font('font_files/Roboto-Medium.ttf', 30)
#
# # def button(xco, yco, w, h, inactive, active, action=None):
# #     mouse = pygame.mouse.get_pos()
# #     click = pygame.mouse.get_pressed()
# #
# #     if xco + w > mouse[0] > xco and yco + h > mouse[1] > yco:
# #         screen.blit(active, (xco, yco))
# #         if click[0] == 1 and action is not None:
# #             action()
# #     else:
# #         screen.blit(inactive, (xco, yco))
#
#
# # Defining functions that draw the menu, how to play screen, quitting, background, the character, and the trash
#
# # Function for drawing the menu
# def drawMenu():
#     pygame.draw.rect(screen, BLACK, (0, 0, width, height))
#
#     title = font.render('Checkers', True, LIGHT_RED)
#     screen.blit(title, pygame.Rect(80, 100, 50, 100))
#     # title_two = font.render('text', True, LIGHT_GREY)
#     # screen.blit(title_two, pygame.Rect(100, 100, 50, 100))
#     subHeading = font_two.render('     BEAT', True, YELLOW)
#     screen.blit(subHeading, pygame.Rect(100, 200, 50, 20))
#     subHeading_two = font_two.render('            OUR', True, YELLOW)
#     screen.blit(subHeading_two, pygame.Rect(200, 200, 50, 20))
#     subHeading_three = font_two.render('       NEW', True, YELLOW)
#     screen.blit(subHeading_three, pygame.Rect(383, 200, 50, 20))
#     subHeading_four = font_two.render('       AI', True, YELLOW)
#     screen.blit(subHeading_four, pygame.Rect(538, 200, 50, 20))
#
#     pygame.draw.rect(screen, WHITE, (185, 300, 400, 100))
#     pygame.draw.rect(screen, BLACK, (190, 305, 390, 90))
#     playButton = font_three.render('PLAY', True, GREEN)
#     screen.blit(playButton, pygame.Rect(298, 320, 50, 20))
#
#     pygame.draw.rect(screen, WHITE, (185, 425, 400, 100))
#     pygame.draw.rect(screen, BLACK, (190, 430, 390, 90))
#     howToPlayButton = font_three.render('GUIDE', True, WHITE)
#     screen.blit(howToPlayButton, pygame.Rect(280, 445, 50, 20))
#
#     pygame.draw.rect(screen, WHITE, (185, 550, 400, 100))
#     pygame.draw.rect(screen, BLACK, (190, 555, 390, 90))
#     terminateButton = font_three.render('EXIT', True, RED)
#     screen.blit(terminateButton, pygame.Rect(310, 570, 50, 20))
#     #
#     # creatorText = font_four.render('SAM, MIMIS, LAKSHMAN AND PETER !!', True, WHITE)
#     # screen.blit(creatorText, pygame.Rect(215, 700, 50, 100))
#
#     pygame.display.flip()
#
#
# # Function for drawing the how to play screen
# def drawHowToPlay():
#     screen.fill(LIGHT_RED)
#     howToText = font_five.render('HOW TO PLAY:', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 50, 50, 20))
#     howToText = font_five.render('Black moves first red', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 75, 50, 20))
#     howToText = font_five.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 100, 50, 20))
#     howToText = font_five.render('', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 125, 50, 20))
#     howToText = font_five.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 150, 50, 20))
#     howToText = font_five.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 175, 50, 20))
#     howToText = font_five.render(',', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 200, 50, 20))
#     howToText = font_five.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(50, 225, 50, 20))
#     howToText = font_five.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(100, 350, 50, 20))
#     howToText = font_four.render(',', True, BLACK)
#     screen.blit(howToText, pygame.Rect(25, 380, 50, 20))
#     howToText = font_four.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(75, 400, 50, 20))
#     howToText = font_five.render('.:', True, BLACK)
#     screen.blit(howToText, pygame.Rect(480, 350, 50, 20))
#     howToText = font_four.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(425, 380, 50, 20))
#     howToText = font_four.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(420, 400, 50, 20))
#     howToText = font_four.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(423, 420, 50, 20))
#     howToText = font_four.render('.', True, BLACK)
#     screen.blit(howToText, pygame.Rect(415, 440, 50, 20))
#     howToText = font_five.render('Click anywhere to return to start game', True, BLACK)
#     screen.blit(howToText, pygame.Rect(140, 550, 50, 20))
#     pygame.display.flip()
#
#
# # Function for quitting the game
# def executeQuitGame():
#     quit()
#
#
# def drawWin():
#     screen.fill(BLACK)
#     winText = font.render('GAME OVER', True, YELLOW)
#     screen.blit(winText, pygame.Rect(100, 240, 50, 20))
#     screen.blit(winText, pygame.Rect(90, 360, 50, 20))
#     pygame.display.flip()
#
# #
# # def drawScreen(character_x, character_y):
# #     pygame.draw.rect(screen, GREEN, (0, 0, width, height))
# #
# #     pygame.draw.rect(screen, ROAD, (0, 575, width, 75))
# #     pygame.draw.rect(screen, YELLOW, (0, 610, width, 4))
# #
# #     pygame.draw.rect(screen, ROAD, (0, 375, width, 75))
# #     pygame.draw.rect(screen, ROAD, (0, 450, width, 75))
# #     pygame.draw.rect(screen, YELLOW, (0, 450, width, 4))
# #     pygame.draw.rect(screen, WHITE, (0, 410, width, 1))
# #     pygame.draw.rect(screen, WHITE, (0, 490, width, 1))
# #
# #     pygame.draw.rect(screen, BROWN, (0, 275, width, 75))
# #     pygame.draw.rect(screen, BLACK, (0, 310, width, 3))
# #     pygame.draw.rect(screen, GREY, (0, 284, width, 3))
# #     pygame.draw.rect(screen, GREY, (0, 297, width, 3))
# #     pygame.draw.rect(screen, GREY, (0, 324, width, 3))
# #     pygame.draw.rect(screen, GREY, (0, 337, width, 3))
# #
# #     pygame.draw.rect(screen, ROAD, (0, 100, width, 75))
# #     pygame.draw.rect(screen, ROAD, (0, 175, width, 75))
# #     pygame.draw.rect(screen, YELLOW, (0, 175, width, 4))
# #     pygame.draw.rect(screen, WHITE, (0, 135, width, 1))
# #     pygame.draw.rect(screen, WHITE, (0, 215, width, 1))
# #
# #     pygame.draw.rect(screen, BROWN, (0, 65, width, 35))
# #     pygame.draw.rect(screen, GREY, (0, 74, width, 3))
# #     pygame.draw.rect(screen, GREY, (0, 87, width, 3))
# #
# #     pygame.draw.circle(screen, PLAYER, (character_x, character_y), 10)
# #     pygame.display.flip()
#
#
# # Defining time, and location of character varaibles
# myClock = pygame.time.Clock()
# running = True
# character_x = width // 2
# character_y = 675
#
# # Defining the game toggle variable
# menu = True
# playGame = False
# howToPlay = False
# quitGame = False
# win = False
#
# # Main game loop
# while running:
#
#     for evnt in pygame.event.get():  # Code for checking all events
#         if evnt.type == pygame.QUIT:
#             running = False
#
#         # Checking for the menu screen toggle
#         if menu:
#             drawMenu()
#             character_x = width // 2
#             character_y = 675
#             pygame.display.flip()
#
#             # Checking for mouse clicks on button
#             if evnt.type == pygame.MOUSEBUTTONUP:
#                 mx, my = evnt.pos
#                 if mx > 185 and mx < 185 + 400 and my > 305 and my < 305 + 90:
#                     playGame = True
#                     menu = False
#             if evnt.type == pygame.MOUSEBUTTONUP:
#                 mx, my = evnt.pos
#                 if mx > 155 and mx < 155 + 390 and my > 430 and my < 430 + 90:
#                     howToPlay = True
#                     menu = False
#             if evnt.type == pygame.MOUSEBUTTONUP:
#                 mx, my = evnt.pos
#                 if mx > 155 and mx < 155 + 390 and my > 555 and my < 555 + 90:
#                     quitGame = True
#
#     # Checking for start game
#     # Checking for start game
#     if playGame == True:
#         pygame.draw.rect(screen, GREY, (0, 0, 800, 800))
#         square_size = 75
#
#         # set margin around board
#         margin = (800 - 8 * square_size) // 2
#
#         # create board surface
#         board = pygame.Surface((600, 600))
#         board.fill(BLACK)
#
#         # draw board squares
#         for row in range(8):
#             for col in range(8):
#                 x = col * square_size
#                 y = row * square_size
#                 if (row + col) % 2 == 0:
#                     pygame.draw.rect(board, RED, (x, y, square_size, square_size))
#
#         # blit board to center of screen
#         board_rect = board.get_rect()
#         board_rect.center = screen.get_rect().center
#         screen.blit(board, board_rect)
#
#         ## END OF GAME BOARD ##
#
#         # ADD PIECES
#         WINDOW_SIZE = (800, 800)
#         SQUARE_SIZE = 75
#         BOARD_SIZE = 8
#         board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
#         starting_pos = [(1, 0), (3, 0), (5, 0), (7, 0), (0, 1), (2, 1), (4, 1), (6, 1), (1, 2), (3, 2), (5, 2), (7, 2),
#                         (0, 5), (2, 5), (4, 5), (6, 5), (1, 6), (3, 6), (5, 6), (7, 6), (0, 7), (2, 7), (4, 7), (6, 7)]
#
#         PIECE_RADIUS = SQUARE_SIZE // 2 - 12
#
#         # Draw the board
#         for row in range(BOARD_SIZE):
#             for col in range(BOARD_SIZE):
#                 index = (row + col) % 2
#                 # color = board_colors[index]
#                 rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
#                 rect.move_ip(board_rect.x, board_rect.y)
#                 # pygame.draw.rect(screen, color, rect)
#
#         # Draw the pieces
#         # for pos in starting_pos:
#         #     x, y = pos
#         #     if y < 3:
#         #         color = GREY
#         #     elif y > 4:
#         #         color = RED
#         #     else:
#         #         continue
#         #     center = ((x + 0.5) * SQUARE_SIZE + board_rect.x, (y + 0.5) * SQUARE_SIZE + board_rect.y)
#         #     pygame.draw.circle(screen, color, center, PIECE_RADIUS)
#
#         # Update the screen
#         pygame.display.update()
#
#         # MAKE A 8 x 8 grid
#
#         ## END OF PIECES ##
#
#         ## BACK TO MENU BUTTON FROM BOARD DISPLAY
#         # button(700, 100, 100, 100, pygame.Surface((100, 100)), pygame.Surface((800, 800)), drawMenu())
#
#
#         for evnt in pygame.event.get():  # Code for checking all events
#             if evnt.type == pygame.QUIT:
#                 running = False
#
#             # Checking for mouse clicks on button
#             if evnt.type == pygame.MOUSEBUTTONUP:
#                 mx, my = evnt.pos
#                 if mx > 700 and mx < 800 and my > 0 and my < 100:
#                     menu = True
#                     playGame = False
#                     # THIS WORKS BUT HAVE TO WAIT AFTER FIRST CLICK (TAKES A COUPLE SECONDS)
#
#
#         ## BACK TO MENU BUTTON FROM BOARD DISPLAY END
#
#         # SO PLAY THE GAME NOW
#         from structures import CheckersGame
#         game = CheckersGame()
#         stones, matrix = structures.initialize_stones_and_matrix(8)
#
#         for row in game.board:
#             for id in row:
#                   if id <= 11:
#                       stone_colour = BLACK
#                   elif id >= 12:
#                       stone_colour = RED
#                   else:
#                       continue
#                   stone_position = stones[id].position
#
#                   stone_center = ((stone_position[0] + 0.5) * SQUARE_SIZE + board_rect.x, (stone_position[1] + 0.5) * SQUARE_SIZE + board_rect.y)
#
#                   pygame.draw.circle(screen, stone_colour, stone_center, PIECE_RADIUS)
#         #
#         #
#         #
#         #
#         #
#         #
#
#         # self.board = [[0, Stone(), 0, Stone(), 0, Stone(), 0, Stone()],
#         #                        [1, 0, 1, 0, 1, 0, 1, 0],
#         #                        [0, 1, 0, 1, 0, 1, 0, 1],
#         #                        [0, 0, 0, 0, 0, 0, 0, 0],
#         #                        [0, 0, 0, 0, 0, 0, 0, 0],
#         #                        [2, 0, 2, 0, 2, 0, 2, 0],
#         #                        [0, 2, 0, 2, 0, 2, 0, 2],
#         #                        [2, 0, 2, 0, 2, 0, 2, 0]]
#
#
#         # pygame.draw.rect(screen, YELLOW, (0, 0, 800, 800))
#
#         pygame.display.flip()  # Updating or refreshing the frames of pygame
#         myClock.tick(60)  # Makes pygame run smoother through FPS, using this code
#
#         #     # Checking for end result
#         # if no pieces left / no moves left:
#         #     win = True
#         #     pygame.display.flip()
#
#     # Checking for player win
#     if win == True:
#         drawWin()
#     # Checking for how to play screen toggle
#     if howToPlay == True:
#         drawHowToPlay()
#         if evnt.type == pygame.MOUSEBUTTONDOWN:
#             howToPlay = False
#             menu = True
#             pygame.display.flip()
#
#     # Checking to quit the game
#     if quitGame == True:
#         executeQuitGame()
#
# # Exiting pygame
# quit()
