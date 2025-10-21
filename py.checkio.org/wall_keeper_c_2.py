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

class Cell:
    """
    Represents a cell in a 5x5 grid with position-determined value, light status, and automatic neighbor setup.
    Values are automatically assigned based on position (1-25) starting from top-left,
    going row by row.
    """
    
    # Class variable to store all created cells
    _grid = {}
    # Dictionary to map values to cell positions for quick lookup
    _value_to_position = {}
    
    def __init__(self, row, column, light=False):
        """
        Initialize a new Cell object and set up its neighbors.
        
        Args:
            row (int): Row position (0-4)
            column (int): Column position (0-4)
            light (bool, optional): Initial light status. Defaults to False.
        """
        # Validate input parameters
        if not (0 <= row <= 4 and 0 <= column <= 4):
            raise ValueError("Row and column must be between 0 and 4")
            
        self._row = row
        self._column = column
        # Calculate value based on position (1-25)
        self._value = row * 5 + column + 1
        self._light = light
        
        # Store this cell in our tracking systems
        Cell._grid[(row, column)] = self
        Cell._value_to_position[self._value] = (row, column)
        
        # Set up neighbors
        self._setup_neighbors()
    
    def _setup_neighbors(self):
        """
        Sets up all neighbor relationships for this cell.
        Creates new cells for neighbors that don't exist yet and
        establishes bidirectional relationships.
        """
        # Initialize all neighbors
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        
        # Check and create up neighbor
        if self._row > 0:
            up_pos = (self._row - 1, self._column)
            if up_pos in Cell._grid:
                self._up = Cell._grid[up_pos]
            else:
                self._up = Cell(self._row - 1, self._column)
            self._up._down = self
            
        # Check and create down neighbor
        if self._row < 4:
            down_pos = (self._row + 1, self._column)
            if down_pos in Cell._grid:
                self._down = Cell._grid[down_pos]
            else:
                self._down = Cell(self._row + 1, self._column)
            self._down._up = self
            
        # Check and create left neighbor
        if self._column > 0:
            left_pos = (self._row, self._column - 1)
            if left_pos in Cell._grid:
                self._left = Cell._grid[left_pos]
            else:
                self._left = Cell(self._row, self._column - 1)
            self._left._right = self
            
        # Check and create right neighbor
        if self._column < 4:
            right_pos = (self._row, self._column + 1)
            if right_pos in Cell._grid:
                self._right = Cell._grid[right_pos]
            else:
                self._right = Cell(self._row, self._column + 1)
            self._right._left = self
    
    # Essential property definitions that were missing before
    @property
    def row(self):
        """Get the row position of the cell."""
        return self._row
    
    @property
    def column(self):
        """Get the column position of the cell."""
        return self._column
    
    @property
    def value(self):
        """Get the cell's value (1-25)."""
        return self._value
    
    @property
    def light(self):
        """Get the cell's light status."""
        return self._light
    
    @property
    def up(self):
        """Get the cell's up neighbor."""
        return self._up
    
    @property
    def down(self):
        """Get the cell's down neighbor."""
        return self._down
    
    @property
    def left(self):
        """Get the cell's left neighbor."""
        return self._left
    
    @property
    def right(self):
        """Get the cell's right neighbor."""
        return self._right
    
    def switch_light(self):
        """
        Switches the light status of the cell between True and False.
        
        Returns:
            bool: The new light status
        """
        self._light = not self._light
        return self._light
    
    @classmethod
    def print_grid(cls):
        """
        Prints the current state of the grid with colors:
        - Green for cells that are OFF
        - Red for cells that are ON
        
        The grid is printed as a 5x5 matrix where each cell shows its value.
        """
        # ANSI color codes for our output
        GREEN = '\033[32m'  # For cells that are OFF
        RED = '\033[31m'    # For cells that are ON
        RESET = '\033[0m'   # Reset color back to default
        
        # Print top border
        print("+" + "-" * 29 + "+")
        
        # Iterate through each row
        for row in range(5):
            # Print each row with vertical borders
            print("|", end=" ")
            
            # Print each cell in the row
            for col in range(5):
                # Get or create the cell at this position
                cell = cls.get_cell_by_value(row * 5 + col + 1)
                
                # Choose color based on light status
                color = RED if cell.light else GREEN
                
                # Print the value with proper spacing and color
                # We use 4 spaces for each cell (2 digits + 2 spaces)
                print(f"{color}{cell.value:2d}{RESET}", end=" ")
            
            # End the row
            print("|")
        
        # Print bottom border
        print("+" + "-" * 29 + "+")
    
    def click(self):
        """
        Performs a click action on this cell, which:
        1. Switches this cell's light
        2. Switches the lights of all existing neighbors (up, down, left, right)
        """
        # Switch this cell's light
        self.switch_light()
        
        # Switch lights of all existing neighbors
        if self._up:
            self._up.switch_light()
        if self._down:
            self._down.switch_light()
        if self._left:
            self._left.switch_light()
        if self._right:
            self._right.switch_light()
    
    @classmethod
    def get_cell_by_value(cls, value):
        """
        Finds and returns a cell by its value. Creates the cell if it doesn't exist.
        
        Args:
            value (int): The value to look for (1-25)
            
        Returns:
            Cell: The cell with the specified value
            
        Raises:
            ValueError: If value is not between 1 and 25
        """
        if not (1 <= value <= 25):
            raise ValueError("Value must be between 1 and 25")
            
        # If we know this value, return its cell
        if value in cls._value_to_position:
            row, col = cls._value_to_position[value]
            return cls._grid[(row, col)]
            
        # If we don't have this cell yet, create it
        row = (value - 1) // 5
        col = (value - 1) % 5
        return Cell(row, col)
    
    @classmethod
    def click_cells(cls, values):
        """
        Clicks multiple cells specified by their values.
        
        Args:
            values (list): List of values (1-25) indicating which cells to click
            
        Example:
            Cell.click_cells([5, 7, 13, 14, 18])
        """
        for value in values:
            cell = cls.get_cell_by_value(value)
            cell.click()
    
    @classmethod
    def reset_grid(cls):
        """
        Resets the grid by clearing all stored cells and value mappings.
        """
        cls._grid.clear()
        cls._value_to_position.clear()
    
    def __str__(self):
        """
        Returns a string representation of the cell.
        """
        return f"Cell({self.row}, {self.column}): value={self.value}, light={'ON' if self.light else 'OFF'}"
    


def wall_keeper(on_panels):
    result = list()
    
    # Step 1: Set initial cells to ON
    print("Setting initial cells to ON:")
    for val in on_panels:
        cell = Cell.get_cell_by_value(val)
        if not cell.light:  # Only switch if it's OFF
            cell.switch_light()
        print(f'The light for {cell.value} is {cell.light}')
    
    print("\nInitial grid state:")
    Cell.print_grid()
    
    # Step 2: Process each row from top to bottom
    print("\nProcessing rows:")
    for row in range(4):  # Only process rows 0-3 since we need 'down' neighbors
        for col in range(5):
            value = row * 5 + col + 1  # Calculate cell value from row and column
            cell = Cell.get_cell_by_value(value)
            
            if cell.light and cell.down:  # Make sure cell is ON and has a down neighbor
                print(f'\nClicking down neighbor of cell {cell.value}:')
                result.append(cell.down.value)  # Add to result before clicking
                cell.down.click()  # This will also affect neighbors
                Cell.print_grid()
    
    # Step 3: Verify final state
    print("\nVerifying final state:")
    all_off = True
    for val in range(1, 26):  # Check all cells (1-25)
        cell = Cell.get_cell_by_value(val)
        if cell.light:
            all_off = False
            print(f'Warning: Cell {val} is still ON')
    
    if all_off:
        print("Success: All cells are OFF")
    else:
        print("Warning: Not all cells are OFF")
    
    print("\nFinal grid state:")
    Cell.print_grid()
    
    print(f'\nSequence of clicked cells: {result}')
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