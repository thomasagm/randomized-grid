import random
from graphics import *

size=25
ratio=0.2
empty=0.6
satisfy=0.8

red=0
blue=1
white=2

def swap(grid, i1, j1, i2, j2):
    """"Swap two values in the grid."""
    grid[i1][j1], grid[i2][j2]= grid[i2][j2], grid[i1][j1]

def createGrid(size, ratio, empty):
    """Generate a random using the Fisher-Yates shuffles."""
    total_cells = size * size
    white_cells = int(total_cells * empty)
    color_cells = total_cells - white_cells
    red_cells = int(color_cells * ratio)
    # blue_cells = color_cells - red_cells

    # Fill the grid non-randomly.
    grid=[]
    c=0
    for i in range(size):
        row=[]
        for j in range(size):
            if c<red_cells:
                row.append(red)
            elif c<color_cells:
                row.append(blue)
            else:
                row.append(white)
            c+=1
        grid.append(row)

    # Apply shuffles to randomize grid.
    for c in range(total_cells-1):
        x=c+random.randint(0,total_cells-c-1)
        swap(grid, c//size, c%size, x//size, x%size)
    return grid

    #Initialize Grid Drawing
def displayGrid(win, grid):
    """Draw the grid to fill the entire window automatically."""
    rows = len(grid)
    cols = len(grid[0])

    win_width = win.getWidth()
    win_height = win.getHeight()

    cell_width = win_width / cols
    cell_height = win_height / rows
    win.autoflush = False   # turn off auto-updating

    for i in range(rows):
        for j in range(cols):
            x1 = j * cell_width
            y1 = i * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            rect = Rectangle(Point(x1, y1), Point(x2, y2))

            # Color based on value
            if grid[i][j] == red:
                rect.setFill("red")
            elif grid[i][j] == blue:
                rect.setFill("blue")
            elif grid[i][j] == white:
                rect.setFill("white")

            rect.setOutline("black")   
            rect.draw(win) 
            

    update()
    win.getMouse()
    win.close()

def main():
    win = GraphWin("Segregation", 500, 500)
    grid = createGrid(size, ratio, empty)
    displayGrid(win, grid)
    pass

if __name__ == '__main__':
    main()
