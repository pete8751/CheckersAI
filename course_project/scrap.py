# def get_poss_moves(self, state: CheckersGame) -> list[Move]:
    #     """
    #     Return the possible moves that self can make based on the passed game state.
    #     """
    #     poss_moves = []
    #
    #     # ------- Getting the upper right and the upper left cells -------
    #     up_right = (self.position[0] + 1, self.position[1] + 1)
    #     up_left = (self.position[0] - 1, self.position[1] + 1)
    #
    #     if _within_range(up_right, 8) and _within_range(up_left, 8):
    #         if state.board[up_right[0]][up_right[1]] == -1 and state.board[up_left[0]][up_left[1]] == -1:
    #             poss_moves.append(Move(self, up_right))
    #             poss_moves.append(Move(self, up_left))
    #         elif state.board[up_right[0]][up_right[1]] == -1:
    #             poss_moves.append(Move(self, up_right))
    #         elif state.board[up_left[0]][up_left[1]] == -1:
    #             poss_moves.append(Move(self, up_left))
    #
    #     # ------- Getting the potential right capturing moves -------
    #     curr_jump_right = (self.position[0] + 2, self.position[1] + 2)
    #     curr_just_right = (self.position[0] + 1, self.position[1] + 1)
    #
    #     while _within_range(curr_jump_right, 8) and _within_range(curr_just_right, 8) and \
    #             state.empty_at(curr_jump_right) and not state.empty_at(curr_just_right) and \
    #             state.board[curr_just_right[0]][curr_just_right[1]] >= 12:
    #         curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] + 2)
    #         curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] + 2)
    #
    #     # while (curr_jump_right[0] < 8 and curr_jump_right[1] < 8) and \
    #     #         (curr_just_right[0] < 8 and curr_just_right[1] < 8) and \
    #     #         (state.board[curr_just_right[0]][curr_just_right[1]] != -1) and \
    #     #         (state.board[curr_jump_right[0]][curr_jump_right[1]] == -1):
    #     #     print(111, curr_jump_right, curr_just_right)
    #     #     curr_jump_right = (curr_jump_right[0] + 2, curr_jump_right[1] + 2)
    #     #     curr_just_right = (curr_just_right[0] + 2, curr_just_right[1] + 2)
    #     #     print(222, curr_jump_right, curr_just_right)
    #     #     print('----------------')
    #
    #     if curr_jump_right != (self.position[0] + 2, self.position[1] + 2):  # i.e. what it is initialized to
    #         poss_jump = (curr_jump_right[0] - 2, curr_jump_right[1] - 2)
    #         move = Move(self, poss_jump)
    #         poss_moves.append(move)
    #
    #     return poss_moves
