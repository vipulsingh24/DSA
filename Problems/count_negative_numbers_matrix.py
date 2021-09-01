"""
Count Negative Numbers in a Column-Wise and Row-Wise Sorted Matrix
Input:  M =  [-3, -2, -1,  1]
             [-2,  2,  3,  4]
             [4,   5,  7,  8]
Output : 4
We have 4 negative numbers in this matrix
"""



def count_neg_numbers(M):
    R = len(M)
    C = len(M[0])
    
    count = 0
    i = 0
    j = m - 1

    while j >= 0 and i < n:
        if M[i][j] < 0:
            count += (j + 1)
            i += 1
        else:
            j -= 1

    return count


if __name__ == "__main__":
    M = [[-3, -2, -1,  1], [-2,  2,  3,  4], [ 4,  5,  7,  8]]
    print(count_neg_numbers(M))

