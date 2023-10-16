"""
Classes representing different possible players.
"""
import math
from typing import Optional

from course_project.game_tree import GameTree
from structures import Move, CheckersGame
from minimax import maximize, minimize, maximize_with_tree, minimize_with_tree, maximize_with_pruning, minimize_with_pruning
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


# class ExploringPlayer(Player):
#     """A Exploring player that sometimes plays maxmin and sometimes plays randomly.
#
#     Representation Invariants:
#         - 0.0 <= self._exploration_probability <= 1.0
#     """
#     # Private Instance Attributes:
#     #   - _game_tree:
#     #       The GameTree that this player uses to make its moves. If None, then this
#     #       player just makes random moves.
#     #   - _exploration_probability:
#     #       The probability that this player ignores its game tree and makes a random move.
#     _game_tree: Optional[a2_game_tree.GameTree]
#     _exploration_probability: float

    # def __init__(self, game_tree: a2_game_tree.GameTree, exploration_probability: float) -> None:
    #     """Initialize this player."""
    #     self._game_tree = game_tree
    #     self._exploration_probability = exploration_probability
    #
    # def make_move(self, game: CheckersGame) -> str:
    #     """Make a move given the current game.
    #
    #     Preconditions:
    #         - game.is_guesser_turn()
    #     """
    #     p = self._exploration_probability
    #     if not game.guesses:
    #         if self._game_tree.moves == []:
    #             move = Randomizer().play()
    #             self._game_tree = None
    #             return move
    #         else:
    #             x = random.uniform(0.0, 1.0)
    #             if x < p:
    #                 possible_moves = game.get_black_moves()
    #                 move = random.choice(list(possible_moves))
    #                 self._game_tree = self._game_tree.find_subtree_by_move(move)
    #                 return move
    #             else:
    #                 movetrees = self._game_tree.get_subtrees()
    #                 bestval = max([tree.guesser_win_probability for tree in movetrees])
    #                 bestrees = [tree for tree in movetrees if tree.guesser_win_probability == bestval]
    #                 movetree = random.choice(bestrees)
    #                 self._game_tree = movetree
    #                 return movetree.move
    #
    #     else:
    #         if self._game_tree is not None:
    #             status = game.statuses.pop()
    #             game.statuses.append(status)
    #             self._game_tree = self._game_tree.find_subtree_by_move(status)
    #         if self._game_tree is None or self._game_tree.get_subtrees() == []:
    #             move = aw.RandomGuesser().make_move(game)
    #             self._game_tree = None
    #             return move
    #         else:
    #             x = random.uniform(0.0, 1.0)
    #             if x < p:
    #                 possible_answers = game.get_possible_answers()
    #                 move = random.choice(list(possible_answers))
    #                 self._game_tree = self._game_tree.find_subtree_by_move(move)
    #                 return move
    #             else:
    #                 movetrees = self._game_tree.get_subtrees()
    #                 bestval = max([tree.guesser_win_probability for tree in movetrees])
    #                 bestrees = [tree for tree in movetrees if tree.guesser_win_probability == bestval]
    #                 movetree = random.choice(bestrees)
    #                 self._game_tree = movetree
    #                 return movetree.move


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
    A Checkers player that makes a move based on the Minimax search algorithm, **without** alpha-beta pruning.

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
    A Checkers player that makes a move based on the Minimax search algorithm, **with** alpha-beta pruning.

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
            move, score = maximize_with_pruning(state, self.depth, -math.inf, math.inf)
            # print(f'score: {score}')
        else:
            move, score = minimize_with_pruning(state, self.depth, -math.inf, math.inf)
            # print(f'score: {score}')

        return move


class PrunelessMinimaxerWithTree(Minimaxer):
    """
    A Checkers player that makes a move based on the Minimax search algorithm, **without** alpha-beta pruning.

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
            move, score, gametree = maximize_with_tree(state, self.depth)
        else:
            move, score, gametree = minimize_with_tree(state, self.depth)

        return move


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
            if state.get_winner() is not None and not state.get_turn():
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
            if state.get_winner() is not None and state.get_turn():
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
        self.game = newgame
        self.game_tree = self.game.gametreewithdepth(self.depth)

    def getmove(self) -> list[float]:
        gametree = self.game_tree
        gametrees = gametree.get_subtrees()
        # games = [self.game.copy_and_record_move(tree.move) for tree in gametrees]
        games = [subtree.game for subtree in gametrees]
        aggroscorelist = [gametrees[i].getaggroscore(self.depth - 1, self.color) for i in range(0, len(gametrees))]
        minscore = min(aggroscorelist)
        aggrmoves = []
        return scorelist

    def play(self, state: CheckersGame) -> Move:
        """
        Return a move given the current state of the game.
        """
        self.update(state)
        if self.color == 'B':
            poss_moves = state.get_black_moves()
            advaggroscores = self.getscores()
            minscore = min(advaggroscores)
            aggrmoves = [poss_moves[i] for i in range(0, len(advaggroscores)) if advaggroscores[i] == minscore]
            move = random.choice(aggrmoves)
        else:
            poss_moves = state.get_red_moves()
            advaggroscores = self.getscores()
            minscore = min(advaggroscores)
            aggrmoves = [poss_moves[i] for i in range(0, len(advaggroscores)) if advaggroscores[i] == minscore]
            move = random.choice(aggrmoves)
        return move
