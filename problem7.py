'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math

def getMax(n):
    return math.ceil(math.sqrt(n))


def isPrime(n):
    upper_limit = getMax(n) + 1
    for i in range(2,upper_limit):
        if n % i == 0:
            return False

    return True


prime_num = 2
counter = 1

while(True):
    if isPrime(prime_num):
        counter += 1

    if counter == 10001:
        print(prime_num)
        break

    print(prime_num)
    prime_num += 1
