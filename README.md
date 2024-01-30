# CheckersAI
<p align="center">
  <img src = "https://github.com/pete8751/CheckersAI/assets/142231087/9bb9f4c9-e7dd-4657-af5e-afbd8f72a38c" width = "200" height = "200" />
</p>


This project is a checkers simulator that allows users to choose between various automated Checkers algorithms, and to watch how their chosen strategy performs against others. The algorithms currently implemented include the MinMax algorithm (with and without pruning), The "Aggressive" Algorithm (optimizes for pieces captured), and the random algorithm. All of these are tree based AI algorithms apart from the random algorithm. The AI algorithm starts with an empty tree, but extends its tree the more games it plays, learning which moves end badly, and which are more favorable. 

I was apart of a team of four who created this project, and was in charge of coding the algorithms and ensuring they ran quickly and accurately.
I also ported this application to the web, using the pygbag python package.

You can play the simulation now! https://pete8751.github.io/CheckersAI/

For information about how the algorithms were implemented, and for data about which algorithms were the best after testing,
please see the project proposal pdf in the checkersproj folder. This pdf is also displayed on the app website.

===========================================================================

Run Instructions (Downloaded Version):

To run this application, you must first clone this repo to your system.

Visualizer:
To run the visualizer, run the 'visual.py' file. This will visualize the games between each algorithm on a checkerboard.
(You choose which algorithms are playing).

Simulator:
To run the simulator, run the 'main.py' file. This will prompt you to choose two algorithms, and will then simulate 100 games between
these algorithms, and return a win/loss percentage, as well as a graph of statistics. You can change the number of games simulated.

===========================================================================

Languages: 
- Python

Tools:
- Pygame
- Pygbag

===========================================================================
