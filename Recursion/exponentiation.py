def exponent(a, n):
    if n == 0:
        return 1

    if n == 1:
        return a

    result = a * exponent(a, abs(n)-1)
    
    if n < 0:
        result = 1 / result

    return result


     
