"""CSC111 Final Project: Checkers & Decision Trees

Module Description
==================
This module contains a collection of Python classes that represent possible players for our Checkers game.

They all inherit the Player interface, which has the abstract method 'play' that all subclasses must implement.

Classes included: Stone, Move, CheckersGame

Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
"""
import math
from typing import Optional

from structures import Move, CheckersGame, GameTree
from minimax import maximize, minimize, maximize_with_tree, minimize_with_tree, maximize_with_pruning, \
    minimize_with_pruning
import random


class Player:
    """
    An abstract class represneting a player in Checkers.

    Instance Attributes:
    - color: the color of the player

    Representation Invariants:
    - self.color in {'R', 'B'}
    """

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        raise NotImplementedError


class Randomizer(Player):
    """
    A Checkers player that makes a move randomly (choosing randomly across all possible moves they can make).
    """

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        if state.get_turn() == True:
            poss_moves = state.get_black_moves()
        else:
            poss_moves = state.get_red_moves()

        move = random.choice(poss_moves)
        return move


class Minimaxer(Player):
    """
    An abstract class representing a Checkers player that makes a move based on the Minimax search algorithm.

    Instance Attributes:
    - depth: the maximum search depth for the Minimax algorithm
    """

    depth: int

    def __init__(self, d: int):
        self.depth = d

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        raise NotImplementedError


class PrunelessMinimaxer(Minimaxer):
    """
    A Checkers player that makes a move based on the Minimax search algorithm, **WITHOUT** alpha-beta pruning.

    Instance Attributes:
    - depth: the maximum search depth for the Minimax algorithm
    """

    def __init__(self, d: int):
        Minimaxer.__init__(self, d)

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        if state.get_turn() == True:
            move, score = maximize(state, self.depth)
            # print(f'score: {score}')
        else:
            move, score = minimize(state, self.depth)
            # print(f'score: {score}')

        return move


class PrunefulMinimaxer(Minimaxer):
    """
    A Checkers player that makes a move based on the Minimax search algorithm, **WITH** alpha-beta pruning.

    Instance Attributes:
    - depth: the maximum search depth for the Minimax algorithm
    """

    def __init__(self, d: int):
        Minimaxer.__init__(self, d)

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        # The _ reprents a score (because the return value is a tuple), which is not used here.
        if state.get_turn() == True:
            move, _ = maximize_with_pruning(state, self.depth, -math.inf, math.inf)
        else:
            move, _ = minimize_with_pruning(state, self.depth, -math.inf, math.inf)

        return move


class PrunelessMinimaxerWithTree(Minimaxer):
    """
    A Checkers player that makes a move based on the Minimax search algorithm, and creates the
    corresponding decision tree filled with the valid scores.

    Instance Attributes:
    - depth: the maximum search depth for the Minimax algorithm
    """

    def __init__(self, d: int):
        Minimaxer.__init__(self, d)

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """

        # The first '_' represents the score and the second '_' represents the produced GameTree, none of which are
        # useful here.
        if state.get_turn() == True:
            move, _, _ = maximize_with_tree(state, self.depth)
        else:
            move, _, _ = minimize_with_tree(state, self.depth)

        return move


# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
class SimpleAggressor(Player):
    """
    A Checkers player that makes the most aggressive move that they can play next
    """
    def __init__(self, color):
        self.color = color

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        if self.color == 'B':
            poss_moves = state.get_black_moves()
            difflist = []
            for move in poss_moves:
                rednumber = state.red_survivors
                new_state = state.copy_and_record_move(move)
                diff = rednumber - new_state.red_survivors
                difflist.append(diff)
            diffmax = max(difflist)
            aggmoves = [poss_moves[i] for i in range(0, len(poss_moves)) if difflist[i] == diffmax]
            move = random.choice(aggmoves)
        else:
            poss_moves = state.get_red_moves()
            difflist = []
            for move in poss_moves:
                blknumber = state.black_survivors
                new_state = state.copy_and_record_move(move)
                diff = blknumber - new_state.black_survivors
                difflist.append(diff)
            diffmax = max(difflist)
            aggmoves = [poss_moves[i] for i in range(0, len(poss_moves)) if difflist[i] == diffmax]
            move = random.choice(aggmoves)
        return move


class AdvancedAggressor(Player):
    """
    A Checkers player that prioritizes aggressive strategies

    - game_tree: the decision tree based on which this player performs
    - game: the CheckersGame based on which this player has to make a move
    - game: the depth of the GameTree
    """
    game_tree: Optional[GameTree]
    game: Optional[CheckersGame]
    depth: int

    def __init__(self, color, depth):
        self.color = color
        self.depth = depth
        self.game = CheckersGame()
        self.game_tree = self.game.gametreewithdepth(depth)

    def update(self, newgame: CheckersGame) -> None:
        """ This method updates the player after it has made a move"""
        gametree, self.game = self.game_tree, newgame
        subtrees = gametree.get_subtrees()
        newtree = [gametree for gametree in subtrees if gametree.game == newgame]
        if newtree:
            newtree1 = newtree[0]
            newtree1.increasedepth(self.depth - 1)
        else:
            newtree1 = self.game.gametreewithdepth(self.depth)
        self.game_tree = newtree1

    def getmove(self) -> Move:
        gametree = self.game_tree
        gametrees = gametree.get_subtrees()
        poss_moves = [gametree.move for gametree in gametrees]
        aggroscorelist = [gametrees[i].getaggroscore(self.depth - 1, self.color) for i in range(0, len(gametrees))]
        minscore = max(aggroscorelist)
        aggromoves = [poss_moves[i] for i in range(0, len(poss_moves)) if aggroscorelist[i] == minscore]
        move = random.choice(aggromoves)
        return move

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        self.update(state)
        move = self.getmove()
        newstate = state.copy_and_record_move(move)
        self.update(newstate)
        return move
