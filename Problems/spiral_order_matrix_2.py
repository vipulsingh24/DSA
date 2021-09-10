"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]
"""


def generate_spiral_matrix(n):
    result = [[0] * n for i in range(n)]
    rs = 0
    re = n
    cs = 0
    ce = n

    count = 0

    while (rs < re and cs < ce):
        for i in range(cs, ce):
            count += 1
            result[rs][i] = count
        rs += 1

        for i in range(rs, re):
            count += 1
            result[i][ce-1] = count
        ce -= 1

        if (rs < re):
            for i in range(ce-1, cs-1, -1):
                count += 1
                result[re-1][i] = count
            re -= 1

        if (cs < ce):
            for i in range(re-1, rs- 1, -1):
                count += 1
                result[i][cs] = count
            cs += 1

    return result


if __name__ == "__main__":
    n = 3
    print(generate_spiral_matrix(n))
    n = 4
    print(generate_spiral_matrix(n))












