"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Input Format:
The first and the only argument contains N integers in an array A.
Output Format:

Return an integer, representing the minimum candies to be given.
Example:

Input 1:
    A = [1, 2]
Output 1:
    3
"""

def distribute_candies(childrens):
    candy_left = [1] * len(childrens)
    candy_right = [1] * len(childrens)

    for left in range(1, len(childrens)):
        if childrens[left] > childrens[left - 1]:
            candy_left[left] = candy_left[left-1] + 1

    for right in range(len(childrens) - 2, -1, -1):
        if childrens[right] > childrens[right + 1]:
            candy_right[right] = candy_right[right+1] + 1

    for k in range(len(childrens)):
        candy_right[k] = max(candy_left[k], candy_right[k])

    return sum(candy_right)


if __name__ == "__main__":
    A = [1,2]
    print(distribute_candies(A))  # 3
    A = [1, 5, 2, 1]
    print(distribute_candies(A))  # 7

