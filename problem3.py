def primeFactor(n):
    i = 2
    while i**2 < n:
        while n % i == 0:
            n = n / i
        i += 1
    return n

print(primeFactor(600851475143))
