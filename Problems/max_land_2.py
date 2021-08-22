"""
Find Maximum number of connected 1's in a given matrix
"""
directions_offset = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), "up_left": (-1, -1), "up_right": (-1, 1), "down_left": (1, -1), "down_right": (1, 1)}


def is_legal_pos(row, col, max_row, max_col):
    if (row < 0) or (col < 0) or (row >= max_row) or (col >= max_col):
        return False
    return True


def get_area_size(matrix, row, col):
    if not is_legal_pos(row, col, len(matrix), len(matrix[0])):
        return 0

    if matrix[row][col] == 0:
        return 0
  
    matrix[row][col] = 0
    size = 1
    
    for direction in ["up", "right", "down", "left", "up_left", "up_right", "down_left", "down_right"]:
        direction_offset = directions_offset.get(direction)
        size += get_area_size(matrix, row + direction_offset[0], col + direction_offset[1])
    return size
    


def max_land_area(matrix):
    max_region = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                size = get_area_size(matrix, row, col)
                max_region = max(size, max_region)

    return max_region


if __name__ == "__main__":
    """
    00110
    01110
    01100
    00001
    """
    M = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
    print(max_land_area(M))  # 7

    ###################
    """
    00110
    01110
    01100
    10001
    """
    M = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 0, 1]]
    print(max_land_area(M))  # 8

    ####################
    """
    00110
    00111
    10000
    00001
    """
    M = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
    print(max_land_area(M)) # 5

    ####################
    """
    00110
    00111
    11000
    00101
    """
    M = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 0, 0, 0], [0, 0, 1, 0, 1]]
    print(max_land_area(M)) # 8





