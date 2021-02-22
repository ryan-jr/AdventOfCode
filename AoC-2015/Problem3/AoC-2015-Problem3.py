# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 05:44:12 2021

@author: HomePC0
"""

"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

# Key hint: 2 dimensional grid = x,y coordinate plane

He begins by delivering a present to the house at his starting location, 
and then an elf at the North Pole calls him via radio and tells him where to move next. 
Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, 
and so his directions are a little off, and Santa ends up visiting some houses more than once. 
How many houses receive at least one present?

# Key Hint: At least one present

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

"""

uniqueCoordList = ["0, 0"]
santaList = [0, 0]
roboList = [0, 0]

uniquectr = 0

with open("3-1Input.txt", "r") as dataFile:
    for line in dataFile:
        for character in line:
            
            delta = santaList
            
            if character == "<":
                
                delta = [delta[0] - 1, delta[1]]
            elif character == ">":
                
                delta = [delta[0] + 1, delta[1]]
            elif character == "^":
                
                delta = [delta[0], delta[1] + 1]
                
            else:
                delta = [delta[0], delta[1] - 1]
                
            print(str(delta[0]) + ", " + str(delta[1]))
                
            if not str(delta[0]) + ", " + str(delta[1]) in uniqueCoordList:
                uniqueCoordList.append(str(delta[0]) + ", " + str(delta[1]))
                uniquectr += 1
                
            santaList = delta
                
print(len(uniqueCoordList))   
