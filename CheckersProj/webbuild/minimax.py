"""CSC111 Final Project: Checkers & Decision Trees

Module Description
==================
This module contains a collection of functions that are used to implement the Minimax search algorithm (both with and
without alpha beta pruning).

Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
"""

import math
import random
from typing import Optional
from structures import CheckersGame, Move, GameTree


def maximize(state: CheckersGame, d: int) -> tuple[Optional[Move], float]:
    """
    Returns a tuple (move, score), containing the move with the highest score (first element) and the score itself
    (second element), computed by a search with depth d.
    """
    # The base case; if we reach a terminal state, then we use our static evaluation fuction, 'utility'
    if d == 0 or (state.get_winner() is not None):
        return (None, utility(state))

    # The possible moves depend on which player's turn it is.
    if state.get_turn() == True:  # Black player's turn
        poss_moves = state.get_black_moves()
    else:  # Red Player's Turn
        poss_moves = state.get_red_moves()

    max_score = -math.inf

    # ---------------- SOS FIX -------------
    # For many round (in the beginning of a game), the scores of all children moves are the same (e.g. 0), and
    # since max_move is updated only if max_score < new_score, max_move never updated and it always moved 1 stone
    # for many consecutive rounds (this happened to be the stone with ID=1). How I improved this, is a made a list
    # that stores all moves that are tied at the max_score; i.e. all moves that have the greatest possible score.
    # The performance of the algorithm changed drastically.

    move_scores = []

    # Iterating over the children
    for move in poss_moves:
        # We use copy and record because our recursive function must not mutate the accumulator 'state'. We want
        # to see "what would happen" if we did the move without actually making the move.
        new_state = state.copy_and_record_move(move)

        # -------- MUTUALLY RECURSIVE CALL on minimize ---------
        new_score = minimize(new_state, d - 1)[1]

        move_scores.append((move, new_score))

        # updating if we found a better score
        if new_score > max_score:
            max_score = new_score

    # a list with all moves that are tied with the highest score
    ties = [move for (move, score) in move_scores if score == max_score]

    choice = random.choice(ties)

    return (choice, max_score)


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

    # ---------------- SOS FIX -------------
    # Same explanation as the corresponding block in the maximizer function. In this case, we do this because we assume
    # that the opponent makes the 'best' possible moves, by the nature of the minimax algorithm.
    move_scores = []

    for move in poss_moves:
        new_state = state.copy_and_record_move(move)
        new_score = maximize(new_state, d - 1)[1]

        move_scores.append((move, new_score))

        if new_score < min_score:
            min_score = new_score

    ties = [move for move, score in move_scores if score == min_score]

    choice = random.choice(ties)

    return (choice, min_score)


def maximize_with_tree(state: CheckersGame, d: int) -> tuple[Optional[Move], float, GameTree]:
    if d == 0 or state.get_winner() is not None:
        score = utility(state)
        gt = GameTree('L', score)
        return (None, score, gt)

    if state.get_turn() == True:  # Black Player's Turn
        poss_moves = state.get_black_moves()
    else:
        poss_moves = state.get_red_moves()

    subtrees = set()
    move_scores = []
    max_score = -math.inf

    for move in poss_moves:

        new_state = state.copy_and_record_move(move)
        _, score, subtree = minimize_with_tree(new_state, d - 1)
        move_scores.append((move, score))
        subtrees.add(subtree)

        if score > max_score:
            max_score = score

    ties = [move for move, score in move_scores if score == max_score]
    choice = random.choice(ties)

    gt = GameTree(choice, max_score)

    for subtree in subtrees:
        gt.add_subtree(subtree)

    return (choice, max_score, gt)


def minimize_with_tree(state: CheckersGame, d: int) -> tuple[Optional[Move], float, GameTree]:
    if d == 0 or state.get_winner() is not None:
        score = utility(state)
        gt = GameTree('L', score)
        return (None, score, gt)

    if state.get_turn() == True:  # Black Player's Turn
        poss_moves = state.get_black_moves()
    else:
        poss_moves = state.get_red_moves()

    subtrees = set()
    move_scores = []
    min_score = math.inf

    for move in poss_moves:
        new_state = state.copy_and_record_move(move)
        _, score, subtree = maximize_with_tree(new_state, d - 1)
        move_scores.append((move, score))
        subtrees.add(subtree)

        if score < min_score:
            min_score = score

    ties = [move for move, score in move_scores if score == min_score]
    choice = random.choice(ties)

    gt = GameTree(choice, min_score)

    for subtree in subtrees:
        gt.add_subtree(subtree)

    return (choice, min_score, gt)


def maximize_with_pruning(state: CheckersGame, d: int, alpha: float, beta: float) -> tuple[Optional[Move], float]:
    """
    Returns a tuple (move, score), containing the move with the highest score (first element) and the score itself
    (second element), computed by a search with depth d.
    """

    if d == 0 or (state.get_winner() is not None):
        return (None, utility(state))

    ## -------------------- NOTE -----------------
    # Technically, here we do not need an if statement, because the maximizer function is ONLY meant
    # to be called when it is the black player's turn. The reason for this is that, in our utility function, higher
    # scores favor the black player and lower scores favor the red player. So if you call the maximizer, you are
    # essentially trying to 'maximize' the utility function (assuming best play from the opponent), so you must
    # be the black player.
    if state.get_turn() == True:  # Black player's turn
        poss_moves = state.get_black_moves()
    else:
        poss_moves = state.get_red_moves()

    max_score = -math.inf

    # ---------------- SOS FIX -------------
    # For many round (in the beginning of a game), the scores of all children moves are the same (e.g. 0), and
    # since max_move is updated only if max_score < new_score, max_move never updated and it always moved 1 stone
    # for many consecutive rounds (this happened to be the stone with ID=1). How I improved this, is a made a list
    # that stores all moves that are tied at the max_score; i.e. all moves that have the greatest possible score.
    # The performance of the algorithm changed drastically.

    move_scores = []

    for move in poss_moves:
        new_state = state.copy_and_record_move(move)

        new_score = minimize_with_pruning(new_state, d - 1, alpha, beta)[1]

        ## Pruning can take place!
        if new_score > beta:
            return move, new_score

        # This has to be inside the for loop in order so that 'subtrees' of this node can utilize it and potentially
        # prune.
        if new_score > alpha:
            alpha = new_score

        move_scores.append((move, new_score))

        if new_score > max_score:
            max_score = new_score

    ties = [move for move, score in move_scores if score == max_score]

    choice = random.choice(ties)

    return (choice, max_score)


def minimize_with_pruning(state: CheckersGame, d: int, alpha: float, beta: float) -> tuple[Optional[Move], float]:
    """
    Returns a tuple (move, score), containing the move with the lowest score (i.e. that yields the lowest score)
    and the score itself (second element), computed by a search with depth d; -- uses alpha beta pruning.
    """
    if d == 0 or (state.get_winner() is not None):
        return (None, utility(state))

    ## -------------------- NOTE -----------------
    # Again, here technically we do not need an if statement, because the minimizer function is ONLY meant
    # to be called when it is the red player's turn. The reason for this is that, in our utility function, higher
    # scores favor the black player and lower scores favor the red player. So if you call the minimizer, you are
    # essentially trying to 'minimize' the utility function (i.e. the likelihood of the black player to win), so you
    # must be the red player.
    if state.get_turn() == True:  # Black player's turn
        poss_moves = state.get_black_moves()
    else:
        poss_moves = state.get_red_moves()

    min_score = math.inf

    # ---------------- SOS FIX -------------
    # Same explanation as the corresponding block in the maximizer function. In this case, we do this because we assume
    # that the opponent makes the 'best' possible moves, by the nature of the minimax algorithm.
    move_scores = []

    for move in poss_moves:
        new_state = state.copy_and_record_move(move)
        new_score = maximize_with_pruning(new_state, d - 1, alpha, beta)[1]

        ## Pruning can take place!
        if new_score < alpha:
            return move, new_score

        # This has to be inside the for loop in order so that 'subtrees' of this node can utilize it and potentially
        # prune.
        if new_score < beta:
            beta = new_score

        move_scores.append((move, new_score))

        if new_score < min_score:
            min_score = new_score

    ties = [move for move, score in move_scores if score == min_score]

    choice = random.choice(ties)

    return (choice, min_score)


def show_board(state: CheckersGame) -> None:
    """
    Print a visual of the board based on the passed state.
    """
    for col in state.board:
        print(col)


def utility(state: CheckersGame) -> float:
    """
    The static evaluation function for the Minimax algorithm.

    Higher return values suggest that the passed state is better for the Black player, while lower return values
    suggest that the passed state is worse for the Black player --  so better for the Red player.

    Thus, a Red player using the minimax algorithm should seek to maximize this score (i.e. choose the move that will
    yield the state with the highest utility, of course looking ahead as much as possible), and a Black player should
    seek to minimize this score.
    """

    if state.get_winner() == 'B':
        win = math.inf
    elif state.get_winner() == 'R':
        win = -math.inf
    else:
        win = 0

    black = state.black_survivors
    red = state.red_survivors

    diff = (len(black) - len(red))

    if len(black) > 0:
        avg_dist = sum([state.stones[i].position[1] for i in black]) / (len(black))
    else:
        avg_dist = 0

    final_score = diff + win + avg_dist

    return final_score
