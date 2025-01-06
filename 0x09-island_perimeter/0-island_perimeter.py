#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A rectangular grid where:
            - 0 represents water
            - 1 represents land
            - Cells are connected horizontally/vertically
            - Grid is surrounded by water
            - Contains only one island (or nothing)
            - No lakes inside the island

    Returns:
        int: The perimeter of the island

    The function works by checking each landcell and counting exposed edges.
    An edge is exposed if it's adjacent to water or the grid boundary.
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four edges of the current land cell

                # Top edge
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Bottom edge
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # Left edge
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Right edge
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
