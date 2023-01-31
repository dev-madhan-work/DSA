def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))


count = 6
for i in range(count):
    print(fib(i),end=" ")
