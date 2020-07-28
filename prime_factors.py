import math

"""
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.
A natural number greater than 1 that is not prime is called a composite number.
For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself.
However, 4 is composite because it is a product (2 × 2) in which both numbers are smaller than 4
"""
def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):
        # while i divides n, print i ad divide n
        while n % i == 0:
            print(i)
            n = n / i

    # Condition if n is a prime number greater than 2
    if n > 2:
        print(n)

primeFactors(315)
