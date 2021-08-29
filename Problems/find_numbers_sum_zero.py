"""
Find N distinct integers with zero sum
"""

def find_numbers(n):
    result = []

    for i in range(1, n //2 + 1):
        result.extend([i, -i])

    if n % 2 == 1:
        result.append(0)

    return result


if __name__=='__main__':
    N = 5
    print(find_numbers(N))
    N = 6
    print(find_numbers(N))
