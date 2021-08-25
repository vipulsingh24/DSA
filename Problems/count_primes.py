"""
Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
"""



def count_prime_numbers(n):
    prime = [True for i in range(n+1)]
    p = 2
    
    while (p * p <= n):
        print("p: ", p)
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                print("i: ", i)
                prime[i] = False
        p += 1


    for j in range(2, len(prime)):
        if prime[j]:
            print(j)



if __name__ == '__main__':
    n = 10
    print(count_prime_numbers(n))
