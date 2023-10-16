"""
Functions implementing the Minimax search algorithm.
"""
import math
import random
from typing import Optional

from structures import CheckersGame, utility, Move

def AggressiveBlack(state: CheckersGame, d: int) -> Move:
    """
    Returnss the most aggressive move, containing the move with the highest score (first element) and the score itself
    (second element), computed by a search with depth d.
    """
    if state.get_winner() is not None and state.get_turn():
        poss_moves = state.get_black_moves()
        difflist = []
        for move in poss_moves:
            rednumber = state.red_survivors
            new_state = state.copy_and_record_move(move)
            diff = rednumber - new_state.red_survivors
            difflist.append(diff)
        diffmax = max(difflist)
        aggmoves = [poss_moves[i] for i in range(0, len(poss_moves)) if difflist[i] == diffmax]
        return random.choice(aggmoves)


def AggressiveRed(state: CheckersGame, d: int) -> Move:
    """
    Returnss the most aggressive move, containing the move with the highest score (first element) and the score itself
    (second element), computed by a search with depth d.
    """
    if state.get_winner() is not None and state.get_turn():
        poss_moves = state.get_black_moves()
        difflist = []
        for move in poss_moves:
            rednumber = state.red_survivors
            new_state = state.copy_and_record_move(move)
            diff = rednumber - new_state.red_survivors
            difflist.append(diff)
        diffmax = max(difflist)
        aggmoves = [poss_moves[i] for i in range(0, len(poss_moves)) if difflist[i] == diffmax]
        return random.choice(aggmoves)


def maximize(state: CheckersGame, d: int) -> tuple[Optional[Move], float]:
    """
    Returns a tuple (move, score), containing the move with the highest score (first element) and the score itself
    (second element), computed by a search with depth d.
    """
    if d == 0 or (state.get_winner() is not None):
        return (None, utility(state))

    if state.get_turn() == True:  # Black player's turn
        poss_moves = state.get_black_moves()
    else:
        poss_moves = state.get_red_moves()

    max_score = -math.inf
    max_move = None

    for move in poss_moves:
        # print(f'move: {move.stone_to_move.ID, move.new_position}')
        new_state = state.copy_and_record_move(move)

        new_score = minimize(new_state, d-1)[1]

        # print('maximizer new_score: ', new_score)

        if new_score > max_score:
            max_score = new_score
            max_move = move

    return (max_move, max_score)


def minimize(state: CheckersGame, d: int) -> tuple[Optional[Move], float]:
    """
    Returns a tuple (move, score), containing the move with the lower score (i.e. that yields the lowest score)
    and the score itself (second element), computed by a search with depth d.
    """
    if d == 0 or (state.get_winner() is not None):
        return (None, utility(state))

    if state.get_turn() == True:  # Black player's turn
        poss_moves = state.get_black_moves()
    else:
        poss_moves = state.get_red_moves()

    min_score = math.inf
    min_move = None

    for move in poss_moves:
        new_state = state.copy_and_record_move(move)
        new_score = maximize(new_state, d-1)[1]

        # print('minimizer new_score: ', new_score)

        if new_score < min_score:
            min_score = new_score
            min_move = move

    return (min_move, min_score)


def show_board(state: CheckersGame) -> None:
    """
    Print a visual of the board based on the passed state.
    """
    for col in state.board:
        print(col)
