# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 06:28:29 2021

@author: HomePC0
"""

# Creating a map for santa

"""


tment building, but he can't find the right floor - the directions he got are a little confusing. 
He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; 
he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?


"""


# Solution to part 1
floorCtr = 0

with open("1-1input.txt", "r") as fileData:
    for line in fileData:
        for characters in line:
                if characters == "(":
                    floorCtr += 1
                else:
                    floorCtr -= 1


print(floorCtr)


"""

--- Part Two ---
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 
The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?

"""


# Solution to part 2

floorCtr = 0
charCtr = 0


with open("1-1input.txt", "r") as fileData:
    for line in fileData:
        for characters in line:


            
                charCtr += 1
                if characters == "(":
                    floorCtr += 1
                else:
                    floorCtr -= 1
                
                if floorCtr == -1:
                    print(floorCtr)
                    print(charCtr)
                    break
                




