# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

# def testDivibility(n):
#     for i in range(1,20):
#         if n % i == 0:
#             continue
#         else:
#             return n
#
# smallDiv = True
# i = 1
# while smallDiv:
#     if testDivibility(i) == -1:
#         i += 1
#     else:
#         smallDiv = False
#
# print(i)
import math

def generate_primes(upper_limit):
    list_of_primes = []
    list_of_primes.append(2)

    for i in range(3, upper_limit, 2):
        j = 0
        is_prime = True
        while list_of_primes[j] * list_of_primes[j] <= i:
            if i % list_of_primes[j] == 0:
                is_prime = False
                break

            j += 1

        if is_prime:
            list_of_primes.append(i)

    return list_of_primes


divisor_max = 20
primes = generate_primes(divisor_max)
print(primes)
result = 1
for i in range(len(primes)):
    a = math.floor(math.log(divisor_max) / math.log(primes[i]))
    result = result * math.pow(primes[i], a)

print(result)
