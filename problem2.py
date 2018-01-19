# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(10))
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

sum = 0
for i in range(50):
    if fibonacci(i) > 4000000:
        break
    elif fibonacci(i) % 2 == 0:
        sum += fibonacci(i)

print(sum)
