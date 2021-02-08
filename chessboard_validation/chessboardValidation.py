#! Python3
# chessBoardVamidation.py
# ABSP - Chapter 5

# Necessary conditions:
# - exactly one black & white king - otherwise game finished
# - max 16 black/white pieces
# - max 8 black/white pawns
# - max 2 pawns, knights, bishops, rooks
# - must be within space 1a to 8h


def is_valid_chessboard(board):
    """
    Summary:
        Validates the provided chessboard if it meets the necessary conditions.

    Args:
        board (dict): Dictionnary representation of a chessboard. (ex: {'1a':'wrook'})

    Returns:
        (bool): True or False
    """
    #Counting occurrences of each figure from provided chessboard
    count = {}
    for figure in board.values():
        count.setdefault(figure, 0)
        count[figure] = count[figure] + 1

    #Check if exactly one white & black king
    for king in ['wking', 'bking']:
        if count[king] != 1:
            return False

    #Check if not more than 16 black/white pieces
    whites = blacks = 0
    for color in board.values():
        if color[0] == 'b':
            blacks += 1
        elif color[0] == 'w':
            whites += 1
        else:
            return False #color other than white or black - incorrect

        if blacks > 16 or whites > 16:
            return False

    #Check if max 8 pawns of each color
        if count['wpawn'] > 8 or count['bpawn'] > 8:
            return False
    
    #Check for all others than kings and pawns
    #If in dictionary, has to equal either 1 or 2
    for figure in ['bknight', 'wknight', 'bbishop', 'wbishop', 'brook', 'wrook', 'bqueen', 'wqueen']:
        if figure in count.keys():
            if count[figure] > 2:
                return False
            
    #Check if all chessboard keys within range 1a:8h
    for k in board.keys():
        if k[0] in range(1, 9):
            return False
        if k[1] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False

    return True


if __name__ == '__main__':
    example_board = {
    '1a':'wrook','1b':'wknight','1c':'wbishop','1d':'wking','1e':'wqueen','1f':'wbishop','1g':'wknight','1h':'wrook',
    '2a':'wpawn','2b':'wpawn','2c':'wpawn','2d':'wpawn','2e':'wpawn','2f':'wpawn','2g':'wpawn','2h':'wpawn',
    '8a':'brook','8b':'bknight','8c':'bbishop','8d':'bking','8e':'bqueen','8f':'bbishop','8g':'bknight','8h':'brook',
    '7a':'bpawn','7b':'bpawn','7c':'bpawn','7d':'bpawn','7e':'bpawn','7f':'bpawn','7g':'bpawn','7h':'bpawn'
    }

    is_valid_chessboard(example_board)