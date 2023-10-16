"""
Classes representing a simulation of a Checkers game.
"""
from players import Player, PrunefulMinimaxer, PrunelessMinimaxerWithTree, Randomizer, PrunelessMinimaxer, \
    SimpleAggressor, AdvancedAggressor
from structures import CheckersGame
from minimax import show_board
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def run_game(black_player: Player, red_player: Player) -> (CheckersGame, str):
    """
    Simulating a Checkers game between the black_player and the red_player.

    Preconditions:
    - (black_player.color == 'R' and black_player.color == 'Y') or (black_player.color == 'R' and black_player.color == 'Y')
    """
    game = CheckersGame()

    while game.get_winner() is None:
        if game.get_turn() == True:  # It is the black player's turn
            move = black_player.play(game)
            # print(f'black - move: {move}')
        else:
            move = red_player.play(game)
            # print(f'red - move: {move}')

        # print(move.stone_to_move.ID, move.new_position)

        game.record_move(move)

        # print(move.stone_to_move.ID, move.new_position)
        # show_board(game)
        # print('---------')

    winner = game.get_winner()

    return (game, winner)


def test_maximizer_no_pruning_BLACK(depth: int, num_games: int):

    b, r = 0, 0
    for _ in range(num_games):
        other_game, winner = run_game(PrunelessMinimaxer(depth), Randomizer())

        if winner == 'B':
            b += 1
        else:
            r += 1

    black = b/num_games

    print(f'black: {black}')

def test_maximizer_no_pruning_RED(depth: int, num_games: int):
    b, r = 0, 0
    for _ in range(num_games):
        other_game, winner = run_game(Randomizer(), PrunelessMinimaxer(depth))

        if winner == 'B':
            b += 1
        elif winner == 'R':
            r += 1
        else:
            raise AssertionError

    red = r/num_games

    print(f'red: {red}')


def test_maximizer_with_pruning_BLACK(depth: int, num_games: int):

    b, r = 0, 0
    for _ in range(num_games):
        other_game, winner = run_game(PrunefulMinimaxer(depth), Randomizer())

        if winner == 'B':
            b += 1
        else:
            r += 1

    black = b/num_games

    print(f'black: {black}')

def test_maximizer_with_pruning_RED(depth: int, num_games: int):

    b, r = 0, 0
    for _ in range(num_games):
        other_game, winner = run_game(Randomizer(), PrunefulMinimaxer(depth))

        if winner == 'B':
            b += 1
        else:
            r += 1

    red = r/num_games

    print(f'red: {red}')





def test():
    b, r = 0, 0
    n = 1500
    for _ in range(n):
        # game, winner = run_game(PrunelessMinimaxer('B', 3), Randomizer('R'))
        # game, winner = run_game(Randomizer('B'), PrunelessMinimaxer('R', 3))

        # ----- depth 1 -----
        # other_game, winner = run_game(PrunelessMinimaxer('B', 1), Randomizer('R'))
        # other_game, winner = run_game(Randomizer('B'), PrunelessMinimaxer('R', 1))

        ##----- depth 2 -----
        # other_game, winner = run_game(PrunelessMinimaxer('B', 2), Randomizer('R'))
        # other_game, winner = run_game(Randomizer('B'), PrunelessMinimaxer('R', 2))

        # ----- depth 3 -----
        # other_game, winner = run_game(PrunelessMinimaxer(3), Randomizer())
        # other_game, winner = run_game(Randomizer(), PrunelessMinimaxer(3))

        # ----- depth 3 TREE-----
        # other_game, winner = run_game(PrunelessMinimaxerWithTree(3), Randomizer())
        # other_game, winner = run_game(Randomizer(), PrunelessMinimaxerWithTree(3))


        other_game, winner = run_game(Randomizer(), Randomizer())

        show_board(other_game)
        if winner == 'B':
            b += 1
        else:
            r += 1

    print(b/n)


#THE FUNCTION BELOW RUNS MULTIPLE GAMES AND PLOTS THE RESULTS USING PLOTLY - PETER

def run_gameaggressive(Black: AdvancedAggressor, red_player: Player) -> (CheckersGame, str):
    """
    Simulating a Checkers game between the black_player and the red_player.

    Preconditions:
    - (black_player.color == 'R' and black_player.color == 'Y') or (black_player.color == 'R' and black_player.color == 'Y')
    """
    game = CheckersGame()
    Black

    while game.get_winner() is None:
        if game.get_turn() == True:  # It is the black player's turn
            move = Black.play(game)

            # print(f'black - move: {move}')
        else:
            move = red_player.play(game)
            # print(f'red - move: {move}')
        game.record_move(move)
        Black.update(game)
        # print(move.stone_to_move.ID, move.new_position)

        print(move.stone_to_move.ID, move.new_position)
        show_board(game)
        print('---------')

    winner = game.get_winner()

    return (game, winner)

def testAggress():
    b, r = 0, 0
    n = 10
    for _ in range(n):
        # game, winner = run_game(PrunelessMinimaxer('B', 3), Randomizer('R'))
        # game, winner = run_game(Randomizer('B'), PrunelessMinimaxer('R', 3))

        # ----- depth 1 -----
        # other_game, winner = run_game(PrunelessMinimaxer('B', 1), Randomizer('R'))
        # other_game, winner = run_game(Randomizer('B'), PrunelessMinimaxer('R', 1))

        ##----- depth 2 -----
        # other_game, winner = run_game(PrunelessMinimaxer('B', 2), Randomizer('R'))
        # other_game, winner = run_game(Randomizer('B'), PrunelessMinimaxer('R', 2))

        # ----- depth 3 -----
        # other_game, winner = run_game(PrunelessMinimaxer(3), Randomizer())
        # other_game, winner = run_game(Randomizer(), PrunelessMinimaxer(3))

        # ----- depth 3 TREE-----
        other_game, winner = run_gameaggressive(AdvancedAggressor('B', 3), Randomizer())
        # other_game, winner = run_game(Randomizer(), PrunelessMinimaxerWithTree(3))

        #other_game, winner = run_game(Randomizer('B'), PrunelessMinimaxer('R', 2))

        # other_game, winner = run_game(Randomizer('B'), Randomizer('R'))

        show_board(other_game)
        if winner == 'B':
            b += 1
        else:
            r += 1

    print(b/n)


def run_games_plot(black_player: Player, red_player: Player, num_games: int, plot: bool = False) -> \
        list[(CheckersGame, str)]:
    """Runs multiple games at once. Plots graph of relevant statistics if plot == True."""
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
        plot_game_statistics(results)
    return lst


def plot_game_statistics(results: list[str]) -> None:
    """Plot the outcomes and win probabilities for a given list of Checkers game results.

    Preconditions:
        - all(r in {'Guesser', 'Adversary'} for r in results)
    """
    outcomes = [1 if result == 'B' else 0 for result in results]

    cumulative_win_percentage = [sum(outcomes[0:i]) / i for i in range(1, len(outcomes) + 1)]
    cumulativered_win_percentage = [1 - i for i in cumulative_win_percentage]
    rolling_win_percentage = \
        [sum(outcomes[max(i - 50, 0):i]) / min(50, i) for i in range(1, len(outcomes) + 1)]
    rollingred_win_percentage = [1 - i for i in rolling_win_percentage]

    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Scatter(y=outcomes, mode='markers',
                             name='Outcome (1 = Black win, 0 = Red win)'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(y=cumulative_win_percentage, mode='lines',
                             name='Black win percentage (cumulative)'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=rolling_win_percentage, mode='lines',
                             name='Black win percentage (most recent 50 games)'),
                  row=2, col=1)
    fig.add_trace(go.Scatter(y=cumulativered_win_percentage, mode='lines',
                            name='Red win percentage (cumulative)'),
                 row=2, col=1)
    fig.add_trace(go.Scatter(y=rollingred_win_percentage, mode='lines',
                             name='Red win percentage (most recent 50 games)'),
                  row=2, col=1)
    fig.update_yaxes(range=[0.0, 1.0], row=2, col=1)

    fig.update_layout(title='Checkers Game Results', xaxis_title='Game')
    fig.show()



#
# def run_games(black_player: Player, red_player: Player, num_games: int) -> list[(CheckersGame, str)]:
#     lst = []
#     i = 0
#     while i < num_games:
#         list.append(run_game(black_player, red_player))
#
#
#
# black = PrunelessMinimaxer('B', 4)
# red = Randomizer('R')
# run_game(black, red)
#
# #A3 REFERENCE:
# def run_learning_algorithm(
#         word_set_file: str,
#         max_guesses: int,
#         exploration_probabilities: list[float],
#         show_stats: bool = True) -> a2_game_tree.GameTree:
#     """Play a sequence of AdversarialWordle games using an ExploringGuesser and RandomAdversary.
#
#     This algorithm first initializes an empty GameTree. All ExploringGuessers will use this
#     SAME GameTree object, which will be mutated over the course of the algorithm!
#     Return this object.
#
#     There are len(exploration_probabilities) games played, where at game i (starting at 0):
#         - The Guesser is an ExploringGuesser (using the game tree) whose exploration probability
#             is equal to exploration_probabilities[i].
#         - The Adversary is a RandomAdversary.
#         - AFTER the game, the move sequence from the game is inserted into the game tree,
#           with a guesser win probability of 1.0 if the Guesser won the game, and 0.0 otherwise.
#
#     Preconditions:
#         - word_set_file and max_guesses satisfy the preconditions of aw.run_game
#         - all(0.0 <= p <= 1.0 for p in exploration_probabilities)
#         - exploration_probabilities != []
#
#     Implementation notes:
#         - A NEW ExploringGuesser instance should be created for each loop iteration.
#           However, each one should use the SAME GameTree object.
#         - You should call aw.run_game, NOT aw.run_games. This is because you need more control
#           over what happens after each game runs, which you can get by writing your own loop
#           that calls run_game. However, you can base your loop on the implementation of run_games.
#         - Note that aw.run_game returns the AdversarialWordle game instance. You may need to review
#           the documentation for that class to figure out what methods are useful here.
#         - You may call print in this function to report progress made in each game.
#         - This function must return the final GameTree object. You can inspect the
#           guesser_win_probability of its nodes, calculate its size, or use it in a
#           RandomTreeGuesser or GreedyTreeGuesser to see how they do with it.
#     """
#     stats = {'Guesser': 0, 'Adversary': 0}
#     results = []
#     game_tree = a2_game_tree.GameTree()
#     for i in range(0, len(exploration_probabilities)):
#         guesser = ExploringGuesser(game_tree, exploration_probabilities[i])
#
#         game = aw.run_game(guesser, aw.RandomAdversary(), word_set_file, max_guesses)
#         winner = game.get_winner()
#         stats[winner] += 1
#         results.append(winner)
#         if game.get_winner() == 'Guesser':
#             game_tree.insert_move_sequence(game.get_move_sequence(), 1.0)
#         else:
#             game_tree.insert_move_sequence(game.get_move_sequence(), 0.0)
#
#         print(f'Game {i} winner: {winner}. Moves: {game.get_move_sequence()}')
#
#     for outcome in stats:
#         print(
#             f'{outcome}: {stats[outcome]}/{len(exploration_probabilities)} '
#             f'({100.0 * stats[outcome] / len(exploration_probabilities):.2f}%)')
#
#     if show_stats:
#         aw.plot_game_statistics(results)
#
#     return game_tree
