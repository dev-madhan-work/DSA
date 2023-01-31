def factorial(n):
    if n ==1:
        return n
    else:
        return n * factorial(n-1)
n = 5
if n < 0:
    print("It should be a postitive number")
elif n == 0:
    print("Factorial is: 1")
else:
    print("Factorial is: ",factorial(n))