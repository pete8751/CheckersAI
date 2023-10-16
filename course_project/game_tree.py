"""
GameTree class and helper functions
"""
from __future__ import annotations

import math

from structures import *


class GameTree:
    """
    A decision tree for a Checkers Game.
    """

    move: Move | str
    game: Optional[CheckersGame]

    _subtrees: list[GameTree]

    def __init__(self, move: Move | str, score=None):
        """
        Initializes a GameTree with only one node.
        The GameTree is initialized without subtrees.
        """
        self.move = move
        self.score = score
        self._subtrees = []

    def add_subtree(self, gt: GameTree):
        """
        Add a new subtree (by adding it to the self._subtrees set)
        """
        self._subtrees += [gt]

    def show_root(self):
        if isinstance(self.move, str):
            return f'(L, {round(self.score, 3)})'
        else:
            return f'({self.move.stone_to_move.ID}, {self.move.new_position}), {round(self.score, 3)}'
    ## ------ Does Not Work ------
    # def __str__(self):
    #     string = ''
    #
    #     string += self.show_root() + '\n'
    #
    #     for subtree in self._subtrees:
    #         string += '      ' + subtree.__str__() + '\n'
    #
    #     return string

    def getaggroscore(self, depth: int, color: str) -> float:
        """
        Assign aggro score for a game tree up to a certain depth, depending on if player is Red or Black
        Preconditions: self is a GameTree of depth at least equal to depth.
            """
        game = self.game
        if color == 'B':
            if self.move is None:
                return 0
            elif depth == 0 or game.get_winner() is not None:
                return 12 - len(game.red_survivors)
            else:
                poss_trees = [tree for tree in self._subtrees]
                # poss_moves = [tree.move for tree in poss_trees]
                nextgame = [tree.game for tree in poss_trees]
                return sum([poss_trees[i].getaggroscore(depth - 1, color)
                            for i in range(0, len(poss_trees))]) / len(poss_trees)
        else:
            if self.move is None:
                return 0
            elif depth == 0 or game.get_winner() is not None:
                return 12 - len(game.red_survivors)
            else:
                poss_trees = [tree for tree in self._subtrees]
                # poss_moves = [tree.move for tree in poss_trees]
                # nextgame = [game.copy_and_record_move(move) for move in poss_moves]
                nextgame = [tree.game for tree in poss_trees]
                # return sum([poss_trees[i].getaggroscore(nextgame[i], depth - 1, color) for i in range(0, len(poss_trees))]) \
                #     / len(poss_trees)
                return sum([poss_trees[i].getaggroscore(depth - 1, color)
                            for i in range(0, len(poss_trees))]) / len(poss_trees)

    def get_subtrees(self):
        return self._subtrees

    def __str__(self):
        return self._str_indented(0)

    def _str_indented(self, i: int):
        string = '       ' * i + self.show_root() + '\n'
        for subtree in self._subtrees:
            string += subtree._str_indented(i + 1)
        return string
