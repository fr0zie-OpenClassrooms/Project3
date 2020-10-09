def gameLocation():
    # Create an empty list to setup the game
    grid = []
    for row in range(15):
        grid.append([])
        for column in range(15):
            grid[row].append([row, column])

    return grid

def wallsLocation():
    """Method that sets default walls and randomizes middle walls location."""
    grid = gameLocation()
    # Create an empty list for walls location
    defaultWalls = []

    i = 0
    for row in grid:
        j = 0
        for column in grid[i]:
            if (grid[i][j] == [0, j] or grid[i][j] == [14, j] or grid[i][j] == [i, 0] or grid[i][j] == [i, 14]) and grid[i][j] != [0, 7] and grid[i][j] != [14, 7]:
                defaultWalls.append([i, j])
            j += 1
        i += 1
    
    return defaultWalls

def startAt():
    grid = gameLocation()
    return grid[0][7]

def finishAt():
    grid = gameLocation()
    return grid[14][7]

print('Walls:', wallsLocation())
print('MacGyver:', startAt())
print('Guardian:', finishAt())

class Labyrinth:
    pass

class MacGyver:
    pass

class Guardian:
    pass

class GUI:
    pass