# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:05:07 2021

@author: Sin-agg
"""
from sudoku_OOP import Grid
import pygame
from pygame.locals import *
import numpy as np
import time

#############
programIcon = pygame.image.load('ikon.png')
WIDTH, HEIGHT = 450, 450
WHITE = (255,255,255)
GREEN = (50,205,50)
GREY = (169,169,169)
BLACK = (0,0,0)
FPS = 60
pygame.font.init()
font = pygame.font.SysFont(None, 25)
###################

def main():
    """
    This function displays an initialized grid using the Grid class then displays the solver algorithm steps as soon as the user left clicks
    anywhere in the window.
    ----
    NOTES : 
    Although the Grid class works with any grid dimension. This displaying part has been written for the most common 9x9 case. 
    """
    clock = pygame.time.Clock()
    run = True
    draw_grid()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]==1:
                algo_displayer()
            else:
                pass

        clock.tick(FPS)
    pygame.display.quit()

def draw_grid():
    WIN.fill(WHITE)
    for i in range(9):
        pygame.draw.rect(WIN, GREY, [0,50+i*50,450,1])
    for i in range(9):
        pygame.draw.rect(WIN, GREY, [50+i*50,0,1,450])

    pygame.draw.rect(WIN, BLACK, [150-3,0,6,450])
    pygame.draw.rect(WIN, BLACK, [300-3,0,6,450])
    pygame.draw.rect(WIN, BLACK, [0,150-3,450,6])
    pygame.draw.rect(WIN, BLACK, [0,300-3,450,6])
    pygame.display.update()

    for i in range(9):
        for j in range(9):
            if une_grille.grid0[i][j] != 0 :
                writer(une_grille.grid0[i][j], tab0[i][j])

def algo_displayer():
    for ele in une_grille.registre:
        time.sleep(0.05) #This function is actually slowed down so the user can follow the algorithm steps.
        writer(ele[0], tab0[ele[1]][ele[2]], color = GREEN)

def writer(anumber, crds_case, color = BLACK ):
    if anumber == 0:
        pygame.draw.rect(WIN, WHITE, [crds_case[0] + 5,crds_case[1] + 5,30,30])
    else :
        number_text = font.render(str(anumber), True, color)
        WIN.blit(number_text, [crds_case[0]+20,crds_case[1]+20])
    pygame.display.update()

tab0 = np.zeros([9,9], dtype=list)
for i in range(tab0.shape[0]):
    for j in range(tab0.shape[1]):
        tab0[i][j] = [50*j, 50*i]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
pygame.display.set_icon(programIcon)

if __name__ == "__main__":
    une_grille = Grid(nval = 15)
    print(une_grille.grid0)
    print(une_grille.grid)
    print(une_grille.registre[:20])
    main()


