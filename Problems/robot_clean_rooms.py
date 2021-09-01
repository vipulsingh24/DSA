def is_valid_cell(matrix, current_row, current_col, max_row, max_col):
    if current_row < 0 or current_col < 0 or current_row >= max_row or current_col >= max_col \
            or matrix[current_row][current_col] == "X":
        return False
    return True


def get_clean_area(matrix, r, c, cleaned_area, R, C, direction="r"):
    if not is_valid_cell(matrix, r, c, R, C):
        return 0

    if cleaned_area[r][c] == 1:
        return 0

    count = 1
    cleaned_area[r][c] = 1

    if direction == "r":
        c = c + 1
    elif direction == "d":
        r = r + 1
    elif direction == "l":
        c = c - 1
    elif direction == "u":
        r = r - 1

    if is_valid_cell(matrix, r, c, R, C):
        count += get_clean_area(matrix, r, c, cleaned_area, R, C, direction=direction)
    else:
        if direction == "r":
            direction = "d"
            r += 1
            c -= 1
        elif direction == "d":
            direction = "l"
            r -= 1
            c -= 1
        elif direction == "l":
            direction = "u"
            c += 1
            r -= 1
        elif direction == "u":
            direction = "r"
            r += 1
            c += 1
        count += get_clean_area(matrix, r, c, cleaned_area, R, C, direction=direction)

    return count


def get_max_clean_region(area):
    max_clean_area = 0

    R = len(area)
    C = len(area[0])

    cleaned_area = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if area[i][j] == "." and cleaned_area[i][j] == 0:
                clean_area = get_clean_area(area, i, j, cleaned_area, R, C)
                max_clean_area = max(max_clean_area, clean_area)

    return max_clean_area


A = ["...X..", "....XX", "..X..."]
print("Max Region 1:  ", get_max_clean_region(A))

"""
. . . . X .
. . . . x x
. . x . . . 
. . . . . .
. . . X . .
"""
A = ["....X.", "....XX", "..X...", "......", "...X.."]
print("Max Region 2: ", get_max_clean_region(A))

"""
. . . . X .
X . . . x x
. . . . . X 
. . . . . .
. . . X . .
"""
A = ["....X.", "X...XX", ".....X", "......", "...X.."]
print("Max Region 3: ", get_max_clean_region(A))

