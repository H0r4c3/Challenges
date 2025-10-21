'https://py.checkio.org/en/mission/wall-keeper/'

'''
rule of the puzzle :

This puzzle uses 5x5 grid. Each panel has two state ( light on or off ).
if you click a panel, the panel and adjacent (4 directions) panels will flip. ( on <=> off )
The goal is all panels lights off.
Practical Solving Strategy
Here's a practical approach for manual solving:

Start by clearing the top row:
For each light that is ON in the top row, click the light directly below it
Clear the second row:
For each light that is ON in the second row, click the light below it
Continue this pattern for all rows except the last one
Check the bottom row:
If all lights are OFF, you've solved it
If any lights are ON, the current configuration cannot be solved
'''
import pandas as pd
import numpy as np
    
def find_neighbors(row, col, num_rows=5, num_cols=5):
    """Find the four adjacent neighbors (up, down, left, right) for a cell at (row, col)."""
    neighbors = list()
    
    # Check up
    if row > 0:
        neighbors.append((row-1, col))
    # Check down
    if row < num_rows-1:
        neighbors.append((row+1, col))
    # Check left
    if col > 0:
        neighbors.append((row, col-1))
    # Check right
    if col < num_cols-1:
        neighbors.append((row, col+1))
    
    return neighbors

def find_neighbors_for_all_cells(grid):
    # Create a dictionary to store cell values and their neighbors
    cell_neighbors = dict()

    # Iterate through each cell in the grid
    for row in range(5):
        for col in range(5):
            # Get the cell value
            cell_value = int(grid.iloc[row, col])
            
            # Find neighbors
            neighbor_positions = find_neighbors(row, col)
            
            # Get the values at those neighbor positions
            neighbor_values = [int(grid.iloc[r, c]) for r, c in neighbor_positions]
            
            # Store in our dictionary
            cell_neighbors[cell_value] = neighbor_values

    return cell_neighbors

def flip_cells(on_panels, cell_value, cell_neighbors_dict, result):
    # click on the number below the cell_value
    neighbors = cell_neighbors_dict[cell_value+5]
    for cell in neighbors:
        if cell in on_panels:
            on_panels.remove(cell)
        else:
            on_panels.append(cell)
    result.append(cell_value+5)
    on_panels = sorted(on_panels)        
    return on_panels, result
    
    
def wall_keeper(on_panels):
    result = list()
    # Create a 5x5 grid with values from 1 to 24
    grid = pd.DataFrame(np.arange(1, 26).reshape(5, 5))
    
    cell_neighbors_dict = find_neighbors_for_all_cells(grid)
    print(cell_neighbors_dict)
    
    for cell in on_panels:
        on_panels, result = flip_cells(on_panels, cell, cell_neighbors_dict, result)
        
    print(result)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import chain


    def checker(solution, on_panels):
        answer = solution(on_panels)
        wk_p = list((0, 1)[n in on_panels] for n in range(1, 26))
        p = list(wk_p[n: n+5] for n in range(0, 25, 5))
        for a in answer:
            r, c = (a-1) // 5, (a-1) % 5
            p[r][c] = 1 - p[r][c]
            if r+1 < 5:
                p[r+1][c] = 1 - p[r+1][c]
            if r-1 > -1:
                p[r-1][c] = 1 - p[r-1][c]
            if c+1 < len(p[0]):
                p[r][c+1] = 1 - p[r][c+1]
            if c-1 > -1:
                p[r][c-1] = 1 - p[r][c-1]
        return sum(chain(*p)) == 0

    assert checker(wall_keeper, [5, 7, 13, 14, 18]), 'basic'
    assert checker(wall_keeper, list(range(1, 26))), 'all_lights'
