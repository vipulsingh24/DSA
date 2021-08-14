def multiply_recursive(n, a):
    """
    Args:
        n: multiplier
        a: multiplicand
    """
    if n == 1:
        return a

    return multiply_recursive(n-1, a) + a


assert multiply_recursive(4, 5) == 20
