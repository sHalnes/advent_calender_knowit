#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:52:11 2017

@author: s_halnes

Oppgave:
Julenissens hjelpere jobber med å lage en funksjon for å generere labyrinter. Generatoren fungerer ved å putte inn x og y koordinatene til hver celle og den forteller deg om det skal settes opp en vegg eller ikke.

De laget følgene generator:

Gitt koordinatene (x,y) til en celle, kalkuler x3 + 12xy + 5xy2
Tell antall enere i den binære representasjonen av svaret ovenfor; er det et oddetall skal det settes opp en mur, er det et partall skal det være åpent.
For en 10x10 labyrint, med øvre venstre hjørne i (x0,y0)=(1,1), får de følgende labyrint. Vegger er representert med '#' og åpne celler med '_'.



Med startpunkt i (1,1) og med gyldige bevegelser opp, ned, høyre og venstre, en celle av gangen; er det mulig å besøke de fleste cellene i labyrinten. Men ikke alle. Celler som (1,9), (1,10), (2,10) er ikke mulige å nå fra startposisjonen (1,1). Totalt er det 11 celler som ikke er mulige å nå.

Hjelperne bestemmer seg for å bygge en labyrint med den beskrevne generatoren, med 1000x1000 celler.

Hvor mange åpne celler er ikke mulige å nå fra startposisjon (1,1)?

Oppgaven er laget av Ole-Steinar Skrede. Ole-Steinar jobber i Knowit som utvikler i et av våre team!
"""

import numpy as np

x_size = y_size = 1000


# fill in maze with zeroes for open cells
def f(X, Y):
    l = []
    n_open_cells = x_size*y_size
    for y in Y:
        for x in X:
            binary = list('{0:b}'.format(x**3 + 12*x*y + 5*x*y**2))
            unique, counts = np.unique(binary, return_counts=True)
            d = dict(zip(unique, counts))
            cell = d['1']%2
            n_open_cells -= cell
            l.append(cell)
    return np.array(l).reshape(x_size,y_size), n_open_cells
    
def check_nabo(x,y, maze):
    neighbours = []
    #up
    if x > 0 and maze[x-1][y] == 0:
        neighbours.append((x-1, y))
    #down
    if x<x_size-1 and maze[x+1][y] == 0:
        neighbours.append((x+1, y))
    #left
    if y > 0 and maze[x][y-1] == 0:
        neighbours.append((x, y-1))
    #right
    if y < y_size-1 and maze[x][y+1] == 0:
        neighbours.append((x, y+1))
    maze[x][y] = True
    return neighbours
        
        

def main():

    X = [i for i in range(1,x_size+1)]
    Y = [i for i in range(1,x_size+1)]
    maze, n_open_cells = f(X, Y)
    
    #visit cells
    n_visited_cells = 0
    not_visited_neibours = [(0,0)]
    while not_visited_neibours:
        x,y = not_visited_neibours.pop()
        if maze[x][y] == 0:
            not_visited_neibours += check_nabo(x,y,maze)
            n_visited_cells += 1
    print('not visited: ', n_open_cells - n_visited_cells)
        

    
if __name__ == "__main__":
    main()
