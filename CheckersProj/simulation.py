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
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def run_game(black_player: Player, red_player: Player) -> (CheckersGame, str):
    """
    Simulating a Checkers game between the black_player and the red_player.

    Preconditions:
    - (black_player.color == 'R' and black_player.color == 'Y') or \
        (black_player.color == 'R' and black_player.color == 'Y')
    """
    game = CheckersGame()

    while game.get_winner() is None:
        if game.get_turn() == True:  # It is the black player's turn
            move = black_player.play(game)
        else:
            move = red_player.play(game)

        game.record_move(move)

    winner = game.get_winner()

    return (game, winner)


def run_games_plot(black_player: Player, red_player: Player, num_games: int, plot: bool = False) -> \
        (list[(CheckersGame, str)], dict[str, float]):
    """
    Runs num_games games with the black_player against the red_player at once.

    Plots graph of relevant statistics if plot == True.
    """
    stats = {'TotalGames': 0, 'Blackwin%': 0, 'Redwin%': 0, 'Blackwins': 0, 'Redwins': 0, 'BlackScore': 0, 'RedScore': 0}
    lst = []
    k = 0

    while k < num_games:
        outcome = run_game(black_player, red_player)
        lst.append(outcome)
        if outcome[1] is not None:  # cannot be None since a game must have a winner to end.
            if outcome[1] == 'B':
                stats['Blackwins'] += 1
                survivors = len(outcome[0].black_survivors)
                stats['BlackScore'] += survivors
                stats['Blackwin%'] = 100 * (stats['Blackwins'] / (k + 1))
                stats['Redwin%'] = 100 - stats['Blackwin%']
            else:
                stats['Redwins'] += 1
                survivors = len(outcome[0].red_survivors)
                stats['RedScore'] += survivors
                stats['Redwin%'] = 100 * (stats['Redwins'] / (k + 1))
                stats['Blackwin%'] = 100 - stats['Redwin%']
        k += 1
        stats['TotalGames'] += 1
    results = [pair[1] for pair in lst]
    if plot:
        _plot_stats(results)
    return lst, stats


def _plot_stats(results: list[str]) -> None:
    """
    Plot the outcomes and win probabilities for a given list of Checkers game results.

    Preconditions:
        - all(r in {'Guesser', 'Adversary'} for r in results)
    """
    results = [1 if result == 'B' else 0 for result in results]

    black_win_percentage = [sum(results[0:i]) / i for i in range(1, len(results) + 1)]
    red_win_percentage = [1 - i for i in black_win_percentage]

    recent_black_win_percentage = \
        [sum(results[max(i - 50, 0):i]) / min(50, i) for i in range(1, len(results) + 1)]
    recent_red_win_percentage = [1 - i for i in recent_black_win_percentage]

    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Scatter(y=results, mode='markers',
                             name='Outcome (1 = Black win, 0 = Red win)'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(y=black_win_percentage, mode='lines',
                             name='Black win percentage (cumulative)'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=recent_black_win_percentage, mode='lines',
                             name='Black win percentage (most recent 50 games)'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=red_win_percentage, mode='lines',
                            name='Red win percentage (cumulative)'),
                 row=2, col=1)
    fig.add_trace(go.Scatter(y=recent_red_win_percentage, mode='lines',
                             name='Red win percentage (most recent 50 games)'),
                  row=2, col=1)
    fig.update_yaxes(range=[0.0, 1.0], row=2, col=1)

    fig.update_layout(title='Checkers Game Results', xaxis_title='Game')
    fig.show()
