# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:44:17 2021

@author: HomePC0
"""

"""

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

"""


dimensionData = []
totalData = []
sideData = []

with open("2-1Input.txt", "r") as dataFile:
    for line in dataFile:
        dimensionData.append(line.strip())
        
        


# LxWxH    
# Surface area calculations:
# Dimension 1 = 2xLxW
# Dimension 2 = 2xWxH
# Dimension 3 = 2xHxL
# Must also include length of smallest side
        
for data in dimensionData:
    tempData = []
    tempSideData = []
    individualDimensions = data.split("x")
    
    
    
    d1 = int(individualDimensions[0]) * int(individualDimensions[1]) * 2 # 638
    d2 = int(individualDimensions[1]) * int(individualDimensions[2]) * 2 # 440
    d3 = int(individualDimensions[0]) * int(individualDimensions[2]) * 2 # 1160

    
    l1 = int(individualDimensions[0]) * int(individualDimensions[1]) # 319
    l2 = int(individualDimensions[1]) * int(individualDimensions[2]) # 220
    l3 = int(individualDimensions[0]) * int(individualDimensions[2]) # 580
    
    
    
    tempData.append(d1)
    tempData.append(d2)
    tempData.append(d3)
    tempData.append(l1)
    tempData.append(l2)
    tempData.append(l3)
    smallestSide = min(tempData)
    
    sumData = d1 + d2 + d3 + smallestSide
    
    totalData.append(sumData)

    tempSideData.append(individualDimensions[0])
    tempSideData.append(individualDimensions[1])
    tempSideData.append(individualDimensions[2])

    sideDimensions = int(individualDimensions[0]) * int(individualDimensions[1]) * int(individualDimensions[2])

    largestSide = max(tempSideData)
    tempSideData.remove(largestSide)

    """
    # This was wrong
    if int(tempSideData[0]) <= int(tempSideData[1]):
        sideSum = int(individualDimensions[0]) + int(individualDimensions[0]) + int(individualDimensions[0]) + int(individualDimensions[0])
    elif int(tempSideData[1]) <= int(tempSideData[0]):
        sideSum = int(individualDimensions[1]) + int(individualDimensions[1]) + int(individualDimensions[1]) + int(individualDimensions[1])
    else: 
        sideSum = (int(tempSideData[0]) * 2) + (int(tempSideData[1]) * 2)
    """
    
    sideSum = 2 * min(int(individualDimensions[0]) + int(individualDimensions[1]), int(individualDimensions[1]) + int(individualDimensions[2]), int(individualDimensions[0]) + int(individualDimensions[2]))
    
    totalRibbonAndBowSum = sideSum + sideDimensions

    sideData.append(totalRibbonAndBowSum)
    
    
    
    

#print(sum(totalData))
print(sum(sideData))

#3800576
    