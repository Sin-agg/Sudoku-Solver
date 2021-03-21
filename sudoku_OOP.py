# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:27:11 2021

@author: Sin-agg
"""

import numpy as np
import random as rd
import time
import sys

class Grid():
    """
    A class to represent a sudoku grid.

    ...
    Attributes
    ----------

    nval : int
        the number of placed numbers in the initialized grid
    dim : tuple
        dimension of the grid
    create_tries_max : int
        the number of times the program should try to create a grid
    init_time_max : float
        the maximum amount of time to be spent trying to set up a single grid
    solve_time_max :
        the maximum amount of time to be spent trying to solve the created grid

    Methods
    -------
    create_grid():
        monitors the differents methods needed to generate a solvable sudoku grid and monitors the time spent doing it.
    initialize_grid():
        generates a random grid according to the attributes specifications.
    solver():
        solves the grid using a backtracking algorithm in a recursive way and records its every step. It is the last step in
        the grid generation. If it solves the grid it retruns it.
    verify():
        verifies if a given change is permitted.

    NOTES
    ----
    This script can work:
        - by it's own (just un-comment the last bit).
        - in the main.py script where the algorithm steps are displayed graphically.


    """

    def __init__(self, nval=15, dim=(9,9), create_tries_max=1000, init_time_max=5e-3, solve_time_max = 1):
        self.nval = nval+1
        self.dim = dim
        self.t0 = 0
        self.t1 = 0
        self.create_tries_max = create_tries_max
        self.k = 0
        self.init_time_max = init_time_max
        self.solve_time_max = solve_time_max
        self.registre = []
        self.grid =  self.create_grid()

    def create_grid(self):
        for tries in range(self.create_tries_max):
            self.k = 0
            if tries == self.create_tries_max -1:
                print(f"Tried {self.create_tries_max} times, I have failed")
                sys.exit(1)
            self.grid0 = np.zeros([self.dim[0],self.dim[1]], dtype=int)
            try:
                self.grid0 = self.initialize_grid()
            except SystemExit:
                print(f"TRY #{tries}: Spent too much time initializing grid. Re-trying.")
                continue
            self.grid = np.copy(self.grid0)
            try:
                self.registre = []
                self.t0 = time.time()
                self.grid = self.solver()
                if 0 not in self.grid:
                    print(f"Found grid with solution after n = {tries+1} tries!")
                    return self.grid
                else:
                    print(f"TRY #{tries} converged to null solution")
                    continue
            except SystemExit:
                print(f"TRY #{tries} too much time spent trying to solve current grid, continuing")
                continue
        print("Maximum tries reached")

    def initialize_grid(self):
        for i in range(self.nval):
            rx = rd.randint(0, self.grid0.shape[0]-1)
            ry = rd.randint(0, self.grid0.shape[1]-1)
            cx = int(rx/3)
            cy = int(ry/3)
            time0 = time.time()
            while(self.grid0[rx][ry]==0):
                if time.time()-time0 > self.init_time_max:
                    sys.exit(1)
                r = rd.randint(1, 9)
                if ((r in self.grid0[rx,:]) or (r in self.grid0[:,ry]) or (r in self.grid0[3*cx:3*cx+3,3*cy:3*cy+3])):
                    continue
                else:
                    self.grid0[rx][ry] = r
        return self.grid0

    def solver(self):
        self.t1 = time.time()
        if self.t1-self.t0 > self.solve_time_max:
            sys.exit(1)
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i][j]==0:
                    for n in range(1,10):
                        self.registre.append([n,i,j])
                        if self.verify(n,i,j):
                            self.grid[i][j]=n

                            self.solver()
                            if 0 not in self.grid:
                                break
                        self.registre.append([0,i,j])
                        self.grid[i][j]=0

                    return self.grid

    def verify(self, number, x, y):
        cx = int(x/3)
        cy = int(y/3)
        if((number in self.grid[x,:]) or (number in self.grid[:,y]) or (number in self.grid[3*cx:3*cx+3,3*cy:3*cy+3])):
            return False
        return True

"""
game = Grid(nval = 10)
print(game.grid)
print(game.grid0)
print(game.registre[:20])

"""
