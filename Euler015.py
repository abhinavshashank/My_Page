'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?'''

gridSize = [20,20]
 
def recPath(gridSize):
    if gridSize == [0,0]: return 1
    paths = 0
    if gridSize[0] > 0:
        paths += recPath([gridSize[0]-1,gridSize[1]])
    if gridSize[1] > 0:
        paths += recPath([gridSize[0],gridSize[1]-1])
 
    return paths
 
result = recPath(gridSize)
print (result)
