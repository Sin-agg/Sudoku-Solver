# Sudoku-Solver
This repository contains a sudoku grid generator and solver using a backtracking algorithm. This part is contained in the sudoko_OOP.py script. It fully functions
independently of the main.py script. It can generate a grid of given dimension and difficulty (number of pre-filled cells). The program will keep generating grids until it generates one that is solvable under a given amount of time. Please note that it isn't considered here the human way of solving a sudoku grid but rather the good old computer brute force.

The goal of the project was to eventually display the algorithm steps taken while trying to solve the grid. This part has been implemented and can be seen by simply running the 
main.py script. Please note that this part has been written for the most common case of a 9x9 grid. Also the displaying speed doesn't reflect the algorithm working speed. It has been intentionally slowed down so that the user can follow through.
