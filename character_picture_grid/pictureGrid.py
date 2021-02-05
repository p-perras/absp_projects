#! python3
# pictureGrid.py
# ABSP - Chapter 4


def rotate_90(grid):
    """
    Summary:
        Rotates a 2d grid 90 degrees and prints it.

    Args:
        grid (list): 2d representation of a grid
    """
    for row in range(len(grid[0])):
        print()
        for col in range(len(grid)):
            print(grid[col][row],end='')


if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
    
    rotate_90(grid)
