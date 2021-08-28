"""
Min Steps to Make Piles Equal Height
"""


def min_steps_equal(piles) -> int:
    if len(piles) < 2:
        return 0

    piles = sorted(piles, reverse=True)

    steps = 0
    for i in range(1, len(piles)):
        steps += i if piles[i - 1] != piles[i] else 0
 
    return steps

if __name__ == "__main__":
    print(min_steps_equal([5, 2, 1]))
    print(min_steps_equal([4, 5, 5, 4, 2]))
