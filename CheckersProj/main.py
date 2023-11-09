"""CSC111 Final Project: Checkers & Decision Trees

Module Description
==================
This is the main module of the project.

Copyright and Usage Information
===============================
This file is Copyright (c) 2023 Samarth Sharma, Lakshman Nair, Peter James, and Mimis Chlympatsos.
"""
from visual import *
from simulation import run_games_plot

if __name__ == "__main__":
    wants_to_play_game = input("Do you want to see our game? (Y/N): ")

    if wants_to_play_game == 'Y':
        games()
        quit()

    else:
        option_string = "Choose the game comnfiguration for which you want statistics to be generated: \n" \
                        + "   1. PrunelessMinimaxer VS Randomizer \n" + \
                        "   2. PrunefulMinimaxer VS Randomizer \n" + \
                        "   3. PrunefulMinimaxer VS PrunefulMinimaxer \n" + \
                        "   4. PrunefulMinimaxer VS AdvancedAggressor \n" + \
                        "   5. AdvancedAggressor VS PrunefulMinimaxer  \n" + \
                        "   6. Customize your own game plot generation  \n" + \
                        "(---type the number of your choice---)"

        choice_of_stats = input(option_string)

        if choice_of_stats.isnumeric():
            choice_of_stats = int(choice_of_stats)
        else:
            raise Exception("Invalid Input!")

        depth = 2
        n = 25
        if choice_of_stats == 1:
            print("Please wait for results...")
            dictionary = run_games_plot(PrunelessMinimaxer(depth), Randomizer(), n, True)[1]
            black = dictionary["Blackwin%"]
            red = dictionary["Redwin%"]
            print('***************************************************')
            print(f'Black Win Percentage: {black}')
            print(f'Red Win Percentage: {red}')
            print('***************************************************')
        elif choice_of_stats == 2:
            print("Please wait for results...")
            dictionary = run_games_plot(PrunefulMinimaxer(depth), Randomizer(), n, True)[1]
            black = dictionary["Blackwin%"]
            red = dictionary["Redwin%"]
            print('***************************************************')
            print(f'Black Win Percentage: {black}')
            print(f'Red Win Percentage: {red}')
            print('***************************************************')
        elif choice_of_stats == 3:
            print("Please wait for results...")
            dictionary = run_games_plot(PrunefulMinimaxer(depth), PrunefulMinimaxer(depth), n, True)[1]
            black = dictionary["Blackwin%"]
            red = dictionary["Redwin%"]
            print('***************************************************')
            print(f'Black Win Percentage: {black}')
            print(f'Red Win Percentage: {red}')
            print('***************************************************')
        elif choice_of_stats == 4:
            print("Please wait for results...")
            dictionary = run_games_plot(PrunefulMinimaxer(depth), AdvancedAggressor('R', depth), n, True)[1]
            black = dictionary["Blackwin%"]
            red = dictionary["Redwin%"]
            print('***************************************************')
            print(f'Black Win Percentage: {black}')
            print(f'Red Win Percentage: {red}')
            print('***************************************************')
        elif choice_of_stats == 5:
            print("Please wait for results...")
            dictionary = run_games_plot(AdvancedAggressor('B', depth), PrunefulMinimaxer(depth), n, True)[1]
            black = dictionary["Blackwin%"]
            red = dictionary["Redwin%"]
            print('***************************************************')
            print(f'Black Win Percentage: {black}')
            print(f'Red Win Percentage: {red}')
            print('***************************************************')
        elif choice_of_stats == 6:
            # ---------- INSTRUCTIONS ----------
            # You will be able to customize the depth and number of games for a configuration where the black player
            # is the PrunefulMinimaxer and the red player is the Randomizer.
            # 1. Choose depth d (depths greater than 4 will take a long time to run, due to the branching factor)
            # 2. Choose number of games (if d is more than 2, this should not be more than 100 since it will take a
            #    considerably long time to run)

            choice_of_depth = input("Enter the depth (note that depth > 4 takes a long time to run): ")
            num_games = input("Enter the number of games: ")

            print("Please be patient for results...")

            d = int(choice_of_depth)
            n = int(num_games)
            black_player = PrunefulMinimaxer(d)
            red_player = Randomizer()

            dictionary = run_games_plot(black_player, red_player, n, True)[1]
            black = dictionary["Blackwin%"]
            red = dictionary["Redwin%"]
            print('***************************************************')
            print(f'Black Win Percentage: {black}')
            print(f'Red Win Percentage: {red}')
            print('***************************************************')
        else:
            raise Exception("Invalid Input!")
