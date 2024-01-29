"""CSC111 Final Project: Checkers & Decision Trees

Module Description
==================
This module contains classes representing used to simulate a Checkers game and evaluate the performance of the AI
decision tree algorithms.

Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
"""

from players import Player
from structures import CheckersGame

def run_game(black_player: Player, red_player: Player) -> (CheckersGame, str):
    """
    Simulating a Checkers game between the black_player and the red_player.

    Preconditions:
    - (black_player.color == 'R' and black_player.color == 'Y') or \
        (black_player.color == 'R' and black_player.color == 'Y')
    """
    print("entered")
    game = CheckersGame()

    while game.get_winner() is None:
        if game.get_turn() == True:  # It is the black player's turn
            move = black_player.play(game)
        else:
            move = red_player.play(game)

        game.record_move(move)
        print("mode made")
    winner = game.get_winner()

    return (game, winner)
