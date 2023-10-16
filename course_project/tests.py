"""
Testing the methods.
"""
from course_project.structures import CheckersGame, Move, Stone


def test_stone_get_poss_moves_BLACK():
    # TEST 1
    game = CheckersGame()
    game.board[3][3] = 17
    ID = game.board[2][2]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(1, 3), (4,4)}

    # TEST 2
    game = CheckersGame()
    game.board[1][3] = 15
    game.board[2][4] = -1
    game.board[3][5] = 16
    game.board[4][6] = -1
    ID = game.board[0][2]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(4, 6)}

    # TEST 3
    game = CheckersGame()
    ID = game.board[4][2]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(3, 3), (5, 3)}

    # TEST 4
    game = CheckersGame()
    game.board[5][3] = 18
    ID = game.board[4][2]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(3, 3), (6, 4)}

    # TEST 5
    game = CheckersGame()
    game.board[3][3] = 18
    ID = game.board[4][2]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(5, 3), (2, 4)}

    # TEST 5
    game = CheckersGame()
    game.board[3][3] = 18
    game.board[1][5] = 19
    game.board[0][6] = -1
    game.board[5][3] = 20
    ID = game.board[4][2]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(0, 6), (6, 4)}

    # TEST 6
    game = CheckersGame()
    ID1, ID2, ID3 = game.board[0][0], game.board[2][0], game.board[4][0]
    stone1, stone2, stone3 = game.stones[ID1], game.stones[ID2], game.stones[ID3]
    pm1, pm2, pm3 = stone1.get_poss_moves(game), stone2.get_poss_moves(game), stone3.get_poss_moves(game)
    assert {len(pm1), len(pm2), len(pm3)} == {0}

    # for row in game.board:
    #     print(row)
    # print([m.new_position for m in poss_moves])


def test_stone_get_poss_moves_RED():
    # TEST 1
    game = CheckersGame()
    ID = game.board[5][5]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(6, 4), (4, 4)}

    # TEST 2
    game = CheckersGame()
    game.board[6][4] = 3
    ID = game.board[5][5]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(7, 3), (4, 4)}

    # TEST 3
    game = CheckersGame()
    game.board[6][4] = 3
    game.board[4][4] = 2
    ID = game.board[5][5]
    stone = game.stones[ID]
    poss_moves = stone.get_poss_moves(game)
    assert {m.new_position for m in poss_moves} == {(7, 3), (3, 3)}




# test_stone_get_poss_moves_BLACK()

# test_stone_get_poss_moves_RED()

def test_checkersgame_record_move():
    # TEST 1
    game = CheckersGame()
    ID = game.board[5][5]
    stone = game.stones[ID]
    move = Move(stone, (4, 4))
    game.record_move(move)
    #Test a (id change)
    assert game.board[5][5] == -1
    assert game.board[4][4] == ID
    #Test b (position change)
    assert stone.position == (4, 4)
    #Test c (history update)
    assert game.red_history == [move]

    # TEST 2
    game = CheckersGame()
    game.board[6][4] = 3
    ID = game.board[5][5]
    stone = game.stones[ID]
    killed_stone = game.stones[game.board[6][4]]
    move = Move(stone, (7, 3))
    game.record_move(move)
    # Test a (id change)
    assert game.board[5][5] == -1
    assert game.board[7][3] == ID
    assert game.board[6][4] == -1
    # Test b (position change)
    assert stone.position == (7, 3)
    # Test c (history update)
    assert game.red_history == [move]
    # Test d (state update)
    assert not killed_stone.state

    #TEST 3
    game = CheckersGame()
    game.board[6][4] = 3
    game.board[4][4] = 2
    ID = game.board[5][5]
    stone = game.stones[ID]
    killed_stone = game.stones[game.board[4][4]]
    move = Move(stone, (3, 3))
    game.record_move(move)
    # Test a (id change)
    assert game.board[5][5] == -1
    assert game.board[3][3] == ID
    assert game.board[4][4] == -1
    # Test b (position change)
    assert stone.position == (3, 3)
    # Test c (history update)
    assert game.red_history == [move]
    # Test d (state update)
    assert not killed_stone.state

    #TEST 4
    game = CheckersGame()
    ID = game.board[4][2]
    stone = game.stones[ID]
    move = Move(stone, (5, 3))
    game.record_move(move)
    #Test a (id change)
    assert game.board[4][2] == -1
    assert game.board[5][3] == ID
    #Test b (position change)
    assert stone.position == (5, 3)
    #Test c (history update)
    assert game.black_history == [move]

    # TEST 5
    game = CheckersGame()
    game.board[5][3] = 14
    ID = game.board[4][2]
    stone = game.stones[ID]
    killed_stone = game.stones[game.board[5][3]]
    move = Move(stone, (6, 4))
    game.record_move(move)
    # Test a (id change)
    assert game.board[4][2] == -1
    assert game.board[6][4] == ID
    assert game.board[5][3] == -1
    # Test b (position change)
    assert stone.position == (6, 4)
    # Test c (history update)
    assert game.black_history == [move]
    # Test d (state update)
    assert not killed_stone.state

    # TEST 5
    game = CheckersGame()
    game.board[3][3] = 14
    ID = game.board[4][2]
    stone = game.stones[ID]
    killed_stone = game.stones[game.board[3][3]]
    move = Move(stone, (2, 4))
    game.record_move(move)
    # Test a (id change)
    assert game.board[4][2] == -1
    assert game.board[2][4] == ID
    assert game.board[3][3] == -1
    # Test b (position change)
    assert stone.position == (2, 4)
    # Test c (history update)
    assert game.black_history == [move]
    # Test d (state update)
    assert not killed_stone.state


# test_checkersgame_record_move()

from minimax import show_board

# def test_game(game: CheckersGame, ID):
#     show_board(game)
#     print(f'stones[ID].position: {game.stones[ID].position}')
#     print(f'stones[ID].state: {game.stones[ID].state}')
#     print(f'game.black_history: {[(m.stone_to_move.ID, m.new_position) for m in game.black_history]}')
#     print(f'game.red_history: {[(m.stone_to_move.ID, m.new_position) for m in game.red_history]}')
#     print(f'game.black_survivors: {game.black_survivors}')
#     print(f'game.red_survivors: {game.red_survivors}')
