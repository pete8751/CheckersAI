"""CSC111 Final Project: Checkers & Decision Trees

Module Description
==================
This module contains a collection of Python classes and functions used to represent games of (our modified version of)
Checkers. In other words, this module contains our Checkers interface.

Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
"""

from __future__ import annotations
from typing import Optional
import copy
from game_tree import GameTree


class Stone:
    """
    A class representing a "stone" (pawn) in a Checkers Game.

    Instance Attributes:
    - ID: a unique identifier for a stone
    - state: whether a piece is alive or dead (captured); True for alive and False for dead
    - position: the (x,y) position of the piece in the board matrix. In the CheckersGame class, a board is represented
        by a nested list, where each list at depth 1 is a column and each element of the inner list specified the
        particular row. For our implementation, position[0] (that is, x) is the column of the board/matrix and
        position[1] (that is, y) is the row of the board/matrix.
    - color: "B" for Black, "R" for Red

    Representation Invariants:
    - self.color in {'R', 'B'}
    - ID >= 0
    - (0 <= position[0] < 8) and (0 <= position[1] < 8)
    """

    ID: int
    state: bool
    position: tuple[int, int]
    color: str
    is_king: bool

    def __init__(self, ID, position, color):
        """
        Used to initialize a stone in the beginning of a game.
        """
        self.ID = ID
        self.position = position
        self.color = color

        # self.state is initialized to True
        self.state = True

    def kill(self) -> None:
        """
        Changes the state of this stone to False, which means that it is dead/captured.
        This stone must be alive in order to call this method.

        Preconditions:
        - self.state = True
        """
        self.state = False

    def get_poss_moves(self, state: CheckersGame) -> list[Move]:
        """
        Return the possible moves that self can make based on the passed game state.
        """

        if self.color == 'B':
            return self._get_black_poss_moves(state)
        else:
            return self._get_red_poss_moves(state)

    def _get_black_poss_moves(self, state: CheckersGame):
        poss_moves = []

        # ------- Getting the upper right and the upper left cells -------
        # up_right = (self.position[0] + 1, self.position[1] + 1)
        # up_left = (self.position[0] - 1, self.position[1] + 1)

        # if _within_range(up_right, 8) and _within_range(up_left, 8):
        #     if state.board[up_right[0]][up_right[1]] == -1 and state.board[up_left[0]][up_left[1]] == -1:
        #         poss_moves.append(Move(self, up_right))
        #         poss_moves.append(Move(self, up_left))
        #     elif state.board[up_right[0]][up_right[1]] == -1:
        #         poss_moves.append(Move(self, up_right))
        #     elif state.board[up_left[0]][up_left[1]] == -1:
        #         poss_moves.append(Move(self, up_left))

        # --------------- Getting the upper right and the upper left cells -----------------
        up_right = (self.position[0] + 1, self.position[1] + 1)
        up_left = (self.position[0] - 1, self.position[1] + 1)
        if (_within_range(up_right, 8) and state.empty_at(up_right)) and \
                (_within_range(up_left, 8) and state.empty_at(up_left)):
            poss_moves.append(Move(self, up_right))
            poss_moves.append(Move(self, up_left))
        elif _within_range(up_right, 8) and state.empty_at(up_right):
            # print("ONLY UP RIGHT: ", self.ID)
            poss_moves.append(Move(self, up_right))
        elif _within_range(up_left, 8) and state.empty_at(up_left):
            # print("ONLY UP LEFT: ", self.ID)
            poss_moves.append(Move(self, up_left))

        # ------- Getting the potential right capturing moves -------
        curr_jump_right = (self.position[0] + 2, self.position[1] + 2)
        curr_just_right = (self.position[0] + 1, self.position[1] + 1)

        while _within_range(curr_jump_right, 8) and _within_range(curr_just_right, 8) and \
                state.empty_at(curr_jump_right) and not state.empty_at(curr_just_right) and \
                state.board[curr_just_right[0]][curr_just_right[1]] >= 12:
            curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] + 2)
            curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] + 2)

        if curr_jump_right != (self.position[0] + 2, self.position[1] + 2):  # i.e. what it is initialized to
            poss_jump = (curr_jump_right[0] - 2, curr_jump_right[1] - 2)
            move = Move(self, poss_jump)
            poss_moves.append(move)

        # ------- Getting the potential left capturing moves -------
        curr_jump_left = (self.position[0] - 2, self.position[1] + 2)
        curr_just_left = (self.position[0] - 1, self.position[1] + 1)

        while _within_range(curr_jump_left, 8) and _within_range(curr_just_left, 8) and \
                state.empty_at(curr_jump_left) and not state.empty_at(curr_just_left) and \
                state.board[curr_just_left[0]][curr_just_left[1]] >= 12:
            # print(111, curr_jump_left, curr_just_left)
            curr_jump_left = (curr_jump_left[0] - 2, curr_jump_left[1] + 2)
            curr_just_left = (curr_just_left[0] - 2, curr_just_left[1] + 2)
            # print(222, curr_jump_left, curr_just_left)
            # print('-------------------------------')

        if curr_jump_left != (self.position[0] - 2, self.position[1] + 2):  # i.e. what it is initialized to
            poss_jump = (curr_jump_left[0] + 2, curr_jump_left[1] - 2)
            move = Move(self, poss_jump)
            poss_moves.append(move)

        return poss_moves

    def _get_red_poss_moves(self, state: CheckersGame):
        poss_moves = []

        # ------- Getting the lower right and the lower left cells -------
        # down_right = (self.position[0] + 1, self.position[1] - 1)
        # down_left = (self.position[0] - 1, self.position[1] - 1)
        #
        # if _within_range(down_right, 8) and _within_range(down_left, 8):
        #     if state.empty_at(down_right) and state.empty_at(down_left):
        #         poss_moves.append(Move(self, down_right))
        #         poss_moves.append(Move(self, down_left))
        #     elif state.empty_at(down_right):
        #         poss_moves.append(Move(self, down_right))
        #     elif state.empty_at(down_left):
        #         poss_moves.append(Move(self, down_left))

        # ------- Getting the lower right and the lower left cells -------
        down_right = (self.position[0] + 1, self.position[1] - 1)
        down_left = (self.position[0] - 1, self.position[1] - 1)
        if (_within_range(down_right, 8) and state.empty_at(down_right)) and \
                (_within_range(down_left, 8) and state.empty_at(down_left)):
            poss_moves.append(Move(self, down_right))
            poss_moves.append(Move(self, down_left))
        elif _within_range(down_right, 8) and state.empty_at(down_right):
            poss_moves.append(Move(self, down_right))
        elif _within_range(down_left, 8) and state.empty_at(down_left):
            poss_moves.append(Move(self, down_left))

        # ------- Getting the potential right capturing moves -------
        curr_jump_right = (self.position[0] + 2, self.position[1] - 2)
        curr_just_right = (self.position[0] + 1, self.position[1] - 1)

        while _within_range(curr_jump_right, 8) and _within_range(curr_just_right, 8) and \
                state.empty_at(curr_jump_right) and not state.empty_at(curr_just_right) and \
                state.board[curr_just_right[0]][curr_just_right[1]] < 12:
            curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] - 2)
            curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] - 2)

        if curr_jump_right != (self.position[0] + 2, self.position[1] - 2):  # i.e. what it is initialized to
            poss_jump = (curr_jump_right[0] - 2, curr_jump_right[1] + 2)  # reversing the last effect on poss_jump
            move = Move(self, poss_jump)
            poss_moves.append(move)

        # ------- Getting the potential left capturing moves -------
        curr_jump_left = (self.position[0] - 2, self.position[1] - 2)
        curr_just_left = (self.position[0] - 1, self.position[1] - 1)

        while _within_range(curr_jump_left, 8) and _within_range(curr_just_left, 8) and \
                state.empty_at(curr_jump_left) and not state.empty_at(curr_just_left) and \
                state.board[curr_just_left[0]][curr_just_left[1]] < 12:
            # print(111, curr_jump_left, curr_just_left)
            curr_jump_left = (curr_jump_left[0] - 2, curr_jump_left[1] - 2)
            curr_just_left = (curr_just_left[0] - 2, curr_just_left[1] - 2)
            # print(222, curr_jump_left, curr_just_left)
            # print('-------------------------------')

        if curr_jump_left != (self.position[0] - 2, self.position[1] - 2):  # i.e. what it is initialized to
            poss_jump = (curr_jump_left[0] + 2, curr_jump_left[1] + 2)
            move = Move(self, poss_jump)
            poss_moves.append(move)

        return poss_moves


def _within_range(coords: tuple[int, int], n: int):
    return 0 <= coords[0] < n and 0 <= coords[1] < n


class Move:
    """
    A class that represents a move in a checkers Game
    """

    stone_to_move: Stone
    new_position: tuple[int, int]

    def __init__(self, stone: Stone, new_pos):
        """
        Preconditions:
        - self.new_position is a valid new position relative to self.stone_to_move.position
        """
        self.stone_to_move = stone
        self.new_position = new_pos

    def positions_captured(self) -> Optional[list[tuple[int, int]]]:

        """ Return all the positions captured by a move, Return an empty list if no positions are captured"""
        #if implementing king will need to change
        pos = self.stone_to_move.position
        new_pos = self.new_position

        if self.stone_to_move.color == "B":
            if new_pos[0] > 1 + pos[0] and new_pos[1] > 1 + pos[1]:
                lst = []
                j = 1 + pos[1]
                for i in range(1 + pos[0], new_pos[0], 2):
                    tup = (i, j)
                    lst.append(tup)
                    j += 2

                return lst

            elif new_pos[0] < pos[0] - 1 and new_pos[1] > 1 + pos[1]:
                lst = []
                i = pos[0] - 1
                for j in range(1 + pos[1], new_pos[1], 2):
                    tup = (i, j)
                    lst.append(tup)
                    i -= 2

                return lst

            else:
                return []

        else:

            if new_pos[0] < pos[0] - 1 and new_pos[1] < pos[1] - 1:
                lst = []
                j = pos[1] - 1
                for i in range(pos[0] - 1, new_pos[0], -2):
                    tup = (i, j)
                    lst.append(tup)
                    j -= 2

                return lst

            elif new_pos[0] > pos[0] + 1 and new_pos[1] < pos[1] - 1:
                lst = []
                j = pos[1] - 1
                for i in range(pos[0] + 1, new_pos[0], 2):
                    tup = (i, j)
                    lst.append(tup)
                    j -= 2

                return lst

            else:
                return []


class CheckersGame:
    """
    A class representing the state of a game in Checkers.

    Each node in the tree stores an Adversarial Wordle move.

    Instance Attributes:
    - black_survivors: the id's of the black stones that are still alive
    - red_survivors: the id's of the red stones that are still alive

    Representation Invariants:
    - (self.black_survivors == 0 and self.red_survivors > 0)

    # Represents board of checkers. Each cell stores id of the piece on that spot, or -1 for
    # for spots that don't have a stone on them.
    """
    board: list[list[int]]
    stones: dict[int, Stone]
    # turn: bool  # if turn == True then it is black player's turn
    black_history: list[Move]  # List of all moves played by the player in chronological order
    red_history: list[Move]  # list of all moves played by red in chronological order.

    black_survivors: set[int]
    red_survivors: set[int]

    # Private Instance Attributes:
    #  - _subtrees:
    #      the subtrees of this tree, which represent the game trees after a possible
    #      move by the current player. Unlike the Tree representation in lecture,
    #      this collection is a MAPPING where the values are GameTrees, and associated
    #      keys are the moves at the root of each subtree. See the last representation
    #      invariant above.
    def __init__(self) -> None:
        """Initialize a new CheckersGame.
        """
        self.stones, self.board = initialize_stones_and_matrix(8)
        # self.turn = True
        self.black_history = []
        self.red_history = []

        # in the beginning all stones are alive
        self.black_survivors = set(ID for ID in self.stones.keys() if self.stones[ID].color == 'B')
        self.red_survivors = set(ID for ID in self.stones.keys() if self.stones[ID].color == 'R')

    def record_move(self, move: Move) -> None:
        """
        Records a move. The following must be updated:
        1. self.board, to absorb the changes brought by this move into the board.
        2. self.turn
        3. self.black_moves or self.red_moves, depending on what player's stone is represented by the move parameter.
        4a. self.stones, to update the position of the stone corresponding to this move
        4b. self.stones, to update the states of stones (of the opponent) that may become captured as a result of this
            move. NOTE: this can be done by invoking the Stone.kill method.
        5. self.black_survivors or self.red_survivors, to update this list depending on if a killing move has been made
        by a black or red player

        Preconditions:
        - Must have valid turn for the stone represented in Move
        """
        pos = move.stone_to_move.position
        new_pos = move.new_position
        self.board[pos[0]][pos[1]], self.board[new_pos[0]][new_pos[1]] = -1, move.stone_to_move.ID

        if move.positions_captured() != []:  # updating the state of the board to account for captures
            for position in move.positions_captured():
                id, self.board[position[0]][position[1]] = self.board[position[0]][position[1]], -1
                stone = self.stones[id]
                if stone.color == "B":
                    self.black_survivors.remove(id)
                else:
                    self.red_survivors.remove(id)
                stone.kill()

        # move.stone_to_move.position = new_pos
        self.stones[move.stone_to_move.ID].position = new_pos  # updating the dictionary to show the change

        if move.stone_to_move.color == "R":  # red is the stone to move
            self.red_history.append(move)
            # self.turn = True
            # self.turn = not self.turn

        else:
            self.black_history.append(move)
            # self.turn = False

    def copy_and_record_move(self, move: Move) -> CheckersGame:
        """
        Records the given move like CheckersGame.record_move, but everything is done on a copy of self (i.e. a copy
        of the current state, the current CheckersGame object).

        Returns a CheckersGame object with all the required changes absorbed.

        Preconditions:
        - Must have valid turn for the stone represented in Move
        """
        copied_state = self._copy()
        copied_state.record_move(move)
        return copied_state

    def get_winner(self) -> Optional[str]:
        """
        Returns "B" if Black is the winner, "R" is Red is the winner, and None if there is no winner yet.
        """

        if len(self.red_survivors) == 0 or \
                (len(self.get_black_moves()) == 0 and len(self.red_survivors) < len(self.black_survivors)) or \
                (len(self.get_red_moves()) == 0 and len(self.red_survivors) < len(self.black_survivors)):
            return 'B'
        elif len(self.black_survivors) == 0 or \
                (len(self.get_red_moves()) == 0 and len(self.red_survivors) >= len(self.black_survivors)) or \
                (len(self.get_black_moves()) == 0 and len(self.red_survivors) >= len(self.black_survivors)):
            return 'R'
        else:
            return None

    def get_black_moves(self) -> list[Move]:
        """
        Returns all possible Moves that can be made by the Red player, given the self.board -- which is the current
        state of the game.
        """
        poss_moves = []
        for ID in self.black_survivors:
            new_moves = self.stones[ID].get_poss_moves(self)
            poss_moves.extend(new_moves)
        return poss_moves

    def get_red_moves(self) -> list[Move]:
        """
        Returns all possible Moves that can be made by the Black player, given the self.board -- which is the current
        state of the game.
        """
        poss_moves = []
        for ID in self.red_survivors:
            new_moves = self.stones[ID].get_poss_moves(self)
            poss_moves.extend(new_moves)
        return poss_moves

    def get_turn(self) -> bool:
        """
        Returns True if it is the Black player's turn and False if it is the Red player's turn.
        """
        if len(self.black_history) == len(self.red_history):
            return True
        else:  # len(self.black_history) == len(self.red_history) + 1
            return False

    def _copy(self):
        """
        Return a copy of this game state (useful in recursion when you do not want to mutate the accumulator).
        """
        new_game = CheckersGame()

        # ------------------- SOS: no copying VS shallow copying VS deep copying -------------------
        # Deep Copying
        new_game.stones = copy.deepcopy(self.stones)
        new_game.board = copy.deepcopy(self.board)
        # Shallow Copying (here we can use shallow copying because the elements of the following lists are integers,
        # so they are immutable and there is no fear for a change appearing in both the original list and the shallow
        # copy of that list (beause no change is possible!)
        new_game.black_history = copy.copy(self.black_history)
        new_game.red_history = copy.copy(self.red_history)

        return new_game

    def empty_at(self, position: tuple[int, int]):
        """Return if the cell/square corresponding to the passed position is unoccupied"""
        return self.board[position[0]][position[1]] == -1

    def gametreewithdepth(self, depth: int) -> GameTree:
        """
                Create a new gametree of depth d from Checkersgame, with rootnode being the previous played move.
                """
        game = self
        if depth == 0 or game.get_winner() is not None:
            if game.get_turn():
                redrecent = game.red_history
                if not redrecent:
                    newgame = GameTree('*')
                else:
                    newgame = GameTree(redrecent[-1])
            else:
                blackrecent = game.black_history
                newgame = GameTree(blackrecent[-1])
            newgame.game = game
            return newgame
        else:
            if game.get_turn():
                redrecent = game.red_history
                poss_moves = game.get_black_moves()
                gamecopies = [game.copy_and_record_move(move) for move in poss_moves]
                if not redrecent:
                    newgame = GameTree('*')
                    newgame._subtrees = [copy.gametreewithdepth(depth - 1) for copy in gamecopies]
                else:
                    newgame = GameTree(redrecent[-1])
                    newgame._subtrees = [copy.gametreewithdepth(depth - 1) for copy in gamecopies]
            else:
                blackrecent = game.black_history
                poss_moves = game.get_red_moves()
                gamecopies = [game.copy_and_record_move(move) for move in poss_moves]
                newgame = GameTree(blackrecent[-1])
                newgame._subtrees = [copy.gametreewithdepth(depth - 1) for copy in gamecopies]
            newgame.game = game
            return newgame


def initialize_stones_and_matrix(n: int) -> tuple[dict[int, Stone], list[list[int]]]:
    """
    Initialize the stones and the board matrix for an n-by-n checkers configuration.

    Returns a tuple (stones, matrix), where the first element is a dictionary mapping Stone ID's to corresponding
    Stone objects, and the latter element is the n-by-n matrix, where an empty square/cell is represented with -1,
    and an occupied square/cell is represented by the ID of the Stone object that occupies it
    (so matrix[i][j] is stores an integer as described above).
    """

    stones = {}  # dict()

    i = 0
    curr_row = 0
    while curr_row < 8:
        if curr_row % 2 == 0:
            stones[i] = Stone(i, (curr_row, 0), "B")
            stones[i + 1] = Stone(i + 1, (curr_row, 2), "B")
            i, curr_row = i + 2, curr_row + 1

        else:
            stones[i] = Stone(i, (curr_row, 1), "B")
            i, curr_row = i + 1, curr_row + 1

    i = 12
    curr_row = 0
    while curr_row < 8:
        if curr_row % 2 == 0:
            stones[i] = Stone(i, (curr_row, 7 - 1), "R")
            i, curr_row = i + 1, curr_row + 1
        else:
            stones[i] = Stone(i, (curr_row, 7), "R")
            stones[i + 1] = Stone(i + 1, (curr_row, 7 - 2), "R")
            i, curr_row = i + 2, curr_row + 1

    board = []
    for i in range(8):
        board.append([])
        for _ in range(8):
            board[i].append(-1)

    for stone in stones.values():
        board[stone.position[0]][stone.position[1]] = stone.ID

    return (stones, board)
