def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#8 * 7 * 6
print(factorial(3))

n = int(input("Enter total number of elements: "))
r = int(input("Enter number of combinations: "))
result = factorial(n) // (factorial(r)*factorial(n-r))
print('result: ',result) 