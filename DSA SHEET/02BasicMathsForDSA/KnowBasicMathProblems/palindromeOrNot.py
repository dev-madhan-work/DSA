n = int(input("Enter a number to check palindrome or not:"))
temp = n
reversedNumber = 0
while n > 0:
    digit = n % 10
    reversedNumber = digit + (reversedNumber*10)
    n = n//10

if temp == reversedNumber:
    print(True)
else:
    print(False)
