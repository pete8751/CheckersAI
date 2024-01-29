"""CSC111 Final Project: Checkers & Decision Trees

Module Description
==================
This module contains a collection of Python classes and functions used to represent games of (our modified version of)
Checkers. In other words, this module contains our Checkers interface.

Classes included: Stone, Move, CheckersGame, GameTree

Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
"""

from __future__ import annotations
from typing import Optional
import copy

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

        # If statement that invokes the appropriate helper function.
        if self.color == 'B':
            return self._get_black_poss_moves(state)
        else:  # self.color == 'R'
            return self._get_red_poss_moves(state)

    def _get_black_poss_moves(self, state: CheckersGame) -> list[Move]:
        """
        Returns a list with all possible moves that can be performed using this (black) stone.

        Preconditions:
        - self.color == 'B'
        """
        poss_moves = []

        ##### ---------- Getting (potential) moves for the "upper right" and the "upper left" cells ----------
        up_right = (self.position[0] + 1, self.position[1] + 1)
        up_left = (self.position[0] - 1, self.position[1] + 1)

        # if both 'up_right' and 'up_left' cells are valid and empty, then both of these are plausible moves.
        if (_within_range(up_right) and state.empty_at(up_right)) and \
                (_within_range(up_left) and state.empty_at(up_left)):
            poss_moves.append(Move(self, up_right))
            poss_moves.append(Move(self, up_left))
        # only 'up_right' is valid and empty
        elif _within_range(up_right) and state.empty_at(up_right):
            poss_moves.append(Move(self, up_right))
        # only 'up_left' is valid and empty
        elif _within_range(up_left) and state.empty_at(up_left):
            poss_moves.append(Move(self, up_left))

        ##### ---------- Getting the potential right capturing moves ----------
        # curr_jump_right represents a potential cell that this stone (self) can "jump" to by capturing another stone.
        curr_jump_right = (self.position[0] + 2, self.position[1] + 2)
        # curr_just_right represents a potential cell that will be "jumped" by self during a capture.
        curr_just_right = (self.position[0] + 1, self.position[1] + 1)

        # while the jump [e.g. from (1,1) to (3,3)] is valid, check if another jump (on top of the previous) one is
        # valid. This allows for double and triple captures at once (which is allowed by the official Checkers rules).
        while _within_range(curr_jump_right) and _within_range(curr_just_right) and \
                state.empty_at(curr_jump_right) and not state.empty_at(curr_just_right) and \
                state.board[curr_just_right[0]][curr_just_right[1]] >= 12:
            curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] + 2)
            curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] + 2)

        # If 'curr_jump_right' is different from what it was initially, it means that the loop condition evaluate to
        # True at least once, so there exists a valid capturing move.
        if curr_jump_right != (self.position[0] + 2, self.position[1] + 2):
            # NOTE: the loop terminates once 'curr_jump_right' and 'curr_just_right' are an invalid capture. Thus,
            # we are interested in capturing move in exactly the previous iteration of the loop, hence the next line.
            poss_jump = (curr_jump_right[0] - 2, curr_jump_right[1] - 2)
            move = Move(self, poss_jump)
            poss_moves.append(move)

        ###### ---------- Getting the potential left capturing moves ----------
        # (same logic as getting the "right capturing moves")
        curr_jump_left = (self.position[0] - 2, self.position[1] + 2)
        curr_just_left = (self.position[0] - 1, self.position[1] + 1)

        while _within_range(curr_jump_left) and _within_range(curr_just_left) and \
                state.empty_at(curr_jump_left) and not state.empty_at(curr_just_left) and \
                state.board[curr_just_left[0]][curr_just_left[1]] >= 12:
            curr_jump_left = (curr_jump_left[0] - 2, curr_jump_left[1] + 2)
            curr_just_left = (curr_just_left[0] - 2, curr_just_left[1] + 2)

        if curr_jump_left != (self.position[0] - 2, self.position[1] + 2):  # i.e. what it is initialized to
            poss_jump = (curr_jump_left[0] + 2, curr_jump_left[1] - 2)
            move = Move(self, poss_jump)
            poss_moves.append(move)

        return poss_moves

    def _get_red_poss_moves(self, state: CheckersGame):
        """
        Returns a list with all possible moves that can be performed using this (red) stone.

        Preconditions:
        - self.color == 'R'
        """
        # This function has exactly the same implementation logic as '_get_black_poss_moves', with the only thing
        # differing is that the cells that self can move to are computed differently (since now we are going in the
        # opposite direction). For instance, instead of upper_right and upper_left, we now have down_right, down_left.

        poss_moves = []

        ##### ---------- Getting the lower right and the lower left cells ----------
        down_right = (self.position[0] + 1, self.position[1] - 1)
        down_left = (self.position[0] - 1, self.position[1] - 1)
        if (_within_range(down_right) and state.empty_at(down_right)) and \
                (_within_range(down_left) and state.empty_at(down_left)):
            poss_moves.append(Move(self, down_right))
            poss_moves.append(Move(self, down_left))
        elif _within_range(down_right) and state.empty_at(down_right):
            poss_moves.append(Move(self, down_right))
        elif _within_range(down_left) and state.empty_at(down_left):
            poss_moves.append(Move(self, down_left))

        ##### ---------- Getting the potential right capturing moves ----------
        curr_jump_right = (self.position[0] + 2, self.position[1] - 2)
        curr_just_right = (self.position[0] + 1, self.position[1] - 1)

        while _within_range(curr_jump_right) and _within_range(curr_just_right) and \
                state.empty_at(curr_jump_right) and not state.empty_at(curr_just_right) and \
                state.board[curr_just_right[0]][curr_just_right[1]] < 12:
            curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] - 2)
            curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] - 2)

        if curr_jump_right != (self.position[0] + 2, self.position[1] - 2):  # i.e. what it is initialized to
            poss_jump = (curr_jump_right[0] - 2, curr_jump_right[1] + 2)  # reversing the last effect on poss_jump
            move = Move(self, poss_jump)
            poss_moves.append(move)

        ##### ---------- Getting the potential left capturing moves ----------
        curr_jump_left = (self.position[0] - 2, self.position[1] - 2)
        curr_just_left = (self.position[0] - 1, self.position[1] - 1)

        while _within_range(curr_jump_left) and _within_range(curr_just_left) and \
                state.empty_at(curr_jump_left) and not state.empty_at(curr_just_left) and \
                state.board[curr_just_left[0]][curr_just_left[1]] < 12:
            curr_jump_left = (curr_jump_left[0] - 2, curr_jump_left[1] - 2)
            curr_just_left = (curr_just_left[0] - 2, curr_just_left[1] - 2)

        if curr_jump_left != (self.position[0] - 2, self.position[1] - 2):  # i.e. what it is initialized to
            poss_jump = (curr_jump_left[0] + 2, curr_jump_left[1] + 2)
            move = Move(self, poss_jump)
            poss_moves.append(move)

        return poss_moves


class Move:
    """
    A class that represents a move in a checkers Game. A move consists of the Stone object that is to be moved, and
    new position that this Stone will go to.

    Representation Invariants:
    - self.new_position is a valid new position relative to self.stone_to_move.position
    """

    stone_to_move: Stone
    new_position: tuple[int, int]

    def __init__(self, stone: Stone, new_pos):
        """
        Preconditions:
        - _within_range(new_position) == True
        """
        self.stone_to_move = stone
        self.new_position = new_pos

    def positions_captured(self) -> list[tuple[int, int]]:
        """
        Return all the positions captured by a move (or an empty list if no positions are captured).
        """
        pos = self.stone_to_move.position
        new_pos = self.new_position

        if self.stone_to_move.color == "B":
            # since black is at the bottom of the screen, it can only move up
            if new_pos[0] > 1 + pos[0] and new_pos[1] > 1 + pos[1]:
                # checking if the move has jumped up and right by more than one square
                lst = []
                j = 1 + pos[1]
                for i in range(1 + pos[0], new_pos[0], 2):
                    tup = (i, j)
                    lst.append(tup)
                    j += 2

                return lst

            elif new_pos[0] < pos[0] - 1 and new_pos[1] > 1 + pos[1]:
                # checking if the move has jumped up and left by more than one square
                lst = []
                i = pos[0] - 1
                for j in range(1 + pos[1], new_pos[1], 2):
                    tup = (i, j)
                    lst.append(tup)
                    i -= 2

                return lst

            else:  # return an empty list if no positions have been captured
                return []

        else:  # self.stone_to_move.color == 'R'
            # since red is at the top of the screen, it can only move down
            if new_pos[0] < pos[0] - 1 and new_pos[1] < pos[1] - 1:
                # checking if the move has jumped down and left by more than one square
                lst = []
                j = pos[1] - 1
                for i in range(pos[0] - 1, new_pos[0], -2):
                    tup = (i, j)
                    lst.append(tup)
                    j -= 2

                return lst

            elif new_pos[0] > pos[0] + 1 and new_pos[1] < pos[1] - 1:
                # checking if the move has jumped down and right by more than one square
                lst = []
                j = pos[1] - 1
                for i in range(pos[0] + 1, new_pos[0], 2):
                    tup = (i, j)
                    lst.append(tup)
                    j -= 2

                return lst

            else:  # return an empty list if no positions have been captured
                return []


class CheckersGame:
    """
    A class representing the state of a game in Checkers.

    Instance Attributes:
    - board: the matrix on which this game takes place. Each cell stored the ID of the piece on that spot, or -1 if
        for spots that are unoccupied. A board is represented by a nested list, where each list at depth 1 is a column
        and each element of the inner list specifies a particular row.
    - stones: a dictionary with all stones in this game, mapping ID's of stones to the corresponding stone objects
    - black_history: a list with all the moves that have taken place by the black player up to this point in the game,
        in chronological order.
    - red_history: a list with all the moves that have taken place by the red player up to this point in the game
        in chronological order.
    - black_survivors: the ID's of the black stones that are still alive
    - red_survivors: the ID's of the red stones that are still alive

    Representation Invariants:
    - all(ID == self.stones[ID].ID for ID in self.stones)
    - len(self.black_history) in {len(self.red_history), len(self.red_history) + 1}
    - (not (self.black_survivors == 0) or self.red_survivors > 0)
    - (not (self.red_survivors == 0) or self.black_survivors > 0)
    """
    board: list[list[int]]
    stones: dict[int, Stone]
    black_history: list[Move]
    red_history: list[Move]
    black_survivors: set[int]
    red_survivors: set[int]

    def __init__(self) -> None:
        """
        Initialize a new CheckersGame.
        """
        self.stones, self.board = _initialize_stones_and_matrix()
        self.black_history = []
        self.red_history = []

        # in the beginning all stones are alive
        self.black_survivors = set(ID for ID in self.stones.keys() if self.stones[ID].color == 'B')
        self.red_survivors = set(ID for ID in self.stones.keys() if self.stones[ID].color == 'R')

    def record_move(self, move: Move) -> None:
        """
        Records a move. The following are updated:
        1. self.board, to absorb the changes brought by this move into the board.
        2. self.turn
        3. self.black_moves or self.red_moves, depending on what player's stone is represented by the move parameter.
        4a. self.stones, to update the position of the stone corresponding to this move
        4b. self.stones, to update the states of stones (of the opponent) that may become captured as a result of this
            move (NOTE: this can be done by invoking the Stone.kill method).
        5. self.black_survivors or self.red_survivors, to update this list depending on if a killing move has been made
            by a black or red player.

        Preconditions:
        - The turn (self.get_turn()) must be valid for the stone represented in Move
        """
        pos = move.stone_to_move.position
        new_pos = move.new_position
        # updating the board to absorb the move
        self.board[pos[0]][pos[1]], self.board[new_pos[0]][new_pos[1]] = -1, move.stone_to_move.ID

        if move.positions_captured() != []:  # updating the state of the board to account for captures
            for position in move.positions_captured():
                ID, self.board[position[0]][position[1]] = self.board[position[0]][position[1]], -1
                stone = self.stones[ID]
                if stone.color == "B":
                    self.black_survivors.remove(ID)
                else:
                    self.red_survivors.remove(ID)
                stone.kill()

        #                                           --------- SOS -----------
        # If we do not deep-copy the moves before adding them to 'black_history' and 'red_history', then since Move
        # has a Stone attribute, and the Stone.position gets mutated through the game, we could end up with the first
        # black move represent an irrational/impossible move [e.g. from (5,7) to (2,2)] because the Stone.position ended
        # up with the last position of that stone (being (5,7)) before the end of the game.
        copied_move = copy.deepcopy(move)

        if move.stone_to_move.color == "R":  # red is the stone to move
            self.red_history.append(copied_move)
        else:
            self.black_history.append(copied_move)

        self.stones[move.stone_to_move.ID].position = new_pos  # updating the dictionary to show the change

    def copy_and_record_move(self, move: Move) -> CheckersGame:
        """
        Records the given move like CheckersGame.record_move, but everything is done on a **DEEP** copy of self
        (a copy of the current state, i.e. the current CheckersGame object).

        Returns a CheckersGame object with all the required changes (caused by the move) absorbed.

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

        # --- Implementation of the rules states in the Project handout ---
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
        Returns all possible moves that can be made by the Red player, given self.board -- which is the current
        state of the game.
        """
        # Works by calling Stone.get_poss_moves() for each black survivor.
        poss_moves = []
        for ID in self.black_survivors:
            new_moves = self.stones[ID].get_poss_moves(self)  # self is this CheckersGame object
            poss_moves.extend(new_moves)
        return poss_moves

    def get_red_moves(self) -> list[Move]:
        """
        Returns all possible Moves that can be made by the Black player, given self.board -- which is the current
        state of the game.
        """
        # Works by calling Stone.get_poss_moves() for each black survivor.
        poss_moves = []
        for ID in self.red_survivors:
            new_moves = self.stones[ID].get_poss_moves(self)
            poss_moves.extend(new_moves)
        return poss_moves

    def get_turn(self) -> bool:
        """
        Returns True if it is the Black player's turn and False if it is the Red player's turn.
        """
        # this means that Black has played as many times as Red, so it is Black's Turn
        if len(self.black_history) == len(self.red_history):
            return True
        else:
            assert len(self.black_history) == len(self.red_history) + 1
            # It is Red's Turn
            return False

    def _copy(self):
        """
        Return a copy of this game state (useful in recursion when you do not want to mutate the accumulator).
        """
        new_game = CheckersGame()

        # ------------------- SOS: no copying VS shallow copying VS deep copying -------------------
        # ~~~ Deep Copying ~~~ (since we do NOT want to have two different CheckersGame objects that refer to the same
        # attribute objects
        new_game.stones = copy.deepcopy(self.stones)
        new_game.board = copy.deepcopy(self.board)
        # ~~~ Shallow Copying ~~~ (here we can use shallow copying because the elements of the following lists are
        # integers, so they are immutable and there is no fear for a change appearing in both the original list and the
        # shallow copy of that list (beause no change is possible!)
        new_game.black_history = copy.copy(self.black_history)
        new_game.red_history = copy.copy(self.red_history)
        new_game.black_survivors = copy.copy(self.black_survivors)
        new_game.red_survivors = copy.copy(self.red_survivors)

        return new_game

    def empty_at(self, position: tuple[int, int]):
        """Returns if the cell/square corresponding to the passed position is unoccupied"""
        return self.board[position[0]][position[1]] == -1

    def gametreewithdepth(self, depth: int) -> GameTree:
        """
        Create a new gametree of depth d from Checkersgame, with root node being the previous played move.
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
                    subtrees = [copy.gametreewithdepth(depth - 1) for copy in gamecopies]
                    newgame._subtrees = subtrees
                else:
                    newgame = GameTree(redrecent[-1])
                    subtrees = [copy.gametreewithdepth(depth - 1) for copy in gamecopies]
                    newgame._subtrees = subtrees
            else:
                blackrecent = game.black_history
                poss_moves = game.get_red_moves()
                gamecopies = [game.copy_and_record_move(move) for move in poss_moves]
                newgame = GameTree(blackrecent[-1])
                subtrees = [copy.gametreewithdepth(depth - 1) for copy in gamecopies]
                newgame._subtrees = subtrees
            newgame.game = game
            return newgame

    # Sam's helper
    def get_moves(self) -> list[Move]:
        """
        Return the list of moves played in a game in the order they were played by combining self.black_history
        and self.red_history.
        """
        j = 0
        moves = []
        for i in range(0, len(self.red_history)):
            moves.append(self.black_history[j])
            moves.append(self.red_history[i])
            j += 1

        if len(self.black_history) > len(self.red_history):
            moves.append(self.black_history[len(self.black_history) - 1])

        return moves


### HELPERs ###

def _initialize_stones_and_matrix() -> tuple[dict[int, Stone], list[list[int]]]:
    """
    Initialize the stones and the board matrix for an 8-by-8 checkers configuration.

    Returns a tuple (stones, matrix), where the first element is a dictionary mapping Stone ID's to corresponding
    Stone objects, and the latter element is the n-by-n matrix, where an empty square/cell is represented with -1,
    and an occupied square/cell is represented by the ID of the Stone object that occupies it
    (so matrix[i][j] is stores an integer as described above).
    """

    stones = {}  # dict()

    # Initializing the black pieces (with the correct positions)
    i = 0
    curr_row = 0  # actually this represents a COLUMN, but this is not important
    while curr_row < 8:
        if curr_row % 2 == 0:  # in even columns we put to pieces
            stones[i] = Stone(i, (curr_row, 0), "B")
            stones[i + 1] = Stone(i + 1, (curr_row, 2), "B")
            i, curr_row = i + 2, curr_row + 1

        else:  # in odd columns we put one piece
            stones[i] = Stone(i, (curr_row, 1), "B")
            i, curr_row = i + 1, curr_row + 1

    # Initializing the red pieces (with the correct positions)
    i = 12
    curr_row = 0
    while curr_row < 8:
        if curr_row % 2 == 0:  # the order switches here; in even columns we put one piece
            stones[i] = Stone(i, (curr_row, 7 - 1), "R")
            i, curr_row = i + 1, curr_row + 1
        else:  # in odd columns we put two pieces
            stones[i] = Stone(i, (curr_row, 7), "R")
            stones[i + 1] = Stone(i + 1, (curr_row, 7 - 2), "R")
            i, curr_row = i + 2, curr_row + 1

    # Initializing an empty board, filled with -1's.
    board = []
    for i in range(8):
        board.append([])
        for _ in range(8):
            board[i].append(-1)

    # Adding all the (previously) intialized stones.
    for stone in stones.values():
        board[stone.position[0]][stone.position[1]] = stone.ID

    return (stones, board)


def _within_range(coords: tuple[int, int]):
    """
    Helper function that returns whether the passed coordinates (which represent a potential cell) are within the valid
    range for an 8-by-8 Checkers board.

    >>> _within_range((-1,0))
    False
    >>> _within_range((0,8))
    False
    >>> _within_range((0,7))
    True
    """
    return (0 <= coords[0] < 8) and (0 <= coords[1] < 8)


class GameTree:
    """
    A decision tree for a Checkers Game.
    """

    move: Move | str
    score: Optional[float]
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

    def getaggroscore(self, depth: int, color: str) -> float:
        """
        Assign aggro score for a game tree up to a certain depth, depending on if player is Red or Black
        """
        game = self.game
        subtrees = self.get_subtrees()
        if color == 'B':
            if self.move is None:
                return 0
            elif depth == 0 or game.get_winner() is not None:
                return 12 - len(game.red_survivors)
            else:
                return sum([subtrees[i].getaggroscore(depth - 1, color)
                            for i in range(0, len(subtrees))]) / len(subtrees)
        else:
            if self.move is None:
                return 0
            elif depth == 0 or game.get_winner() is not None:
                return 12 - len(game.black_survivors)
            else:
                return sum([subtrees[i].getaggroscore(depth - 1, color)
                            for i in range(0, len(subtrees))]) / len(subtrees)

    def increasedepth(self, depth: int) -> GameTree:
        """
        Increase depth of gamteree (self) by 1; mutates self
        """
        game = self.game
        if depth == 0:
            return game.gametreewithdepth(1)
        else:
            subtrees = self.get_subtrees()
            self._subtrees = [subtree.increasedepth(depth - 1) for subtree in subtrees]
        return self

    def get_subtrees(self) -> list[GameTree]:
        """
        Return self._subtrees.
        """
        return self._subtrees

    def __str__(self):
        return self._str_indented(0)

    def _str_indented(self, i: int):
        string = '       ' * i + self.show_root() + '\n'
        for subtree in self._subtrees:
            string += subtree._str_indented(i + 1)
        return string
