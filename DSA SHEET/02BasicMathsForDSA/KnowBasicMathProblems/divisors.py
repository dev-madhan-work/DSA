def divisors(n):
    for i in range(1, (n//2)+1):
        if n %i == 0:
            print(i,end=" ")
    print(n)
n = int(input("Enter n:"))
divisors(n)