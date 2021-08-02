"""
Find length of the largest region in Boolean Matrix

[[0, 0, 1, 0, 1],
 [0, 0, 1, 1, 0],
 [1, 0, 1, 1, 0]]

Output: 6

From a given cell you can traverse all the possible 8 adjacent node.
"""
offsets = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1),
           "up_right": (-1, 1), "down_right": (1, 1), "up_left": (-1, -1), "down_left": (1, -1)}


def is_legal_pos(M, x, y, R, C):
    return ((x >= 0) and (x < R) and
            (y >= 0) and (y < C) and
            (M[x][y] and M[x][y] != 1))

def dfs(M, current_row_idx, current_col_idx, R, C, count):
    print(current_row_idx, current_col_idx, R, C)
    if is_legal_pos(M, current_row_idx, current_col_idx, R, C):
        print("I am inside")
        M[current_row_idx][current_col_idx] = 2
        print(M)
    
        for direction in offsets.keys():
            offset = offsets[direction]
            count[0] += 1
            dfs(M, current_row_idx + offset[0], current_col_idx + offset[1], R, C, count)
    print(count)


def max_land_area(M):
    max_row = len(M)
    max_col = len(M[0])
    result = -9999999999999999

    for i in range(max_row):
        for j in range(max_col):
            if M[i][j] == 1:
                count = [1]
                dfs(M, i, j, max_row, max_col, count)
                result = max(result, count[0])
            else:
                M[i][j] = 2  # Mark Visited node as 2
                continue
    print(M)
    return result

if __name__ == "__main__":
    land = [[0, 0, 1, 1, 0],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1]]
    print(land)
    print(max_land_area(land))
