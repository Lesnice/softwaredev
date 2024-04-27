def count_mines(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Define the directions to check for adjacent cells
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is not a mine ('-'), count adjacent mines
            if grid[i][j] == '-':
                mines_count = 0
                # Check each direction for adjacent cells
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    # Check if the adjacent cell is within the grid boundaries
                    if 0 <= x < rows and 0 <= y < cols:
                        # If the adjacent cell is a mine ('#'), increment the mines_count
                        if grid[x][y] == '#':
                            mines_count += 1
                # Replace the dash ('-') with the number of adjacent mines
                grid[i][j] = str(mines_count)

    return grid

