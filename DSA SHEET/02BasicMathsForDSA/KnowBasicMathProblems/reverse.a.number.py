n = int(input("Enter a number"))
reversedNumber = 0
while n > 0:
    digit = n % 10
    reversedNumber = digit + (reversedNumber*10)
    n = n//10

print(reversedNumber)