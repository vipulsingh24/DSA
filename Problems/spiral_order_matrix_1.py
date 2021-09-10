"""
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

def print_spiral_order(matrix):
    rs = 0  # row starting index
    re = len(matrix)  # row ending index  # re = 3
    cs = 0
    ce = len(matrix[0])  # ce = 3

    while (rs < re and cs < ce):
        # Print the first row
        for i in range(cs, ce):
            print(matrix[rs][i], end=" ")  # 1,2,3
        rs += 1  # rs=1

        # Print the last col
        for i in range(rs, re):  # 1-3
            print(matrix[i][ce-1], end=" ")  # 6,9
        ce -= 1  # ce = 2

        if (rs < re):
            # Print the last row
            for i in range(ce-1, cs-1, -1):  # 1 to -1,-1
                print(matrix[re-1][i], end=" ")
            re -= 1  # re = 2

        if (cs < ce):
            # Print the first col
            for i in range(re-1, rs-1, -1):  # 1 to 0, -1 
                print(matrix[i][cs], end=" ")
            cs += 1  # cs = 1

    return None


if __name__ == "__main__":
    M = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    print_spiral_order(M)


# Time - O(mn)
# Space - O(1)












