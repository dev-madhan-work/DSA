#function count digits
def countDigits(n):
    count = 0
    while n>0:
        n = n//10
        count = count+1

    return count

#driver code
n = int(input("Enter a number to count digits:"))
print("Number of digits: ", countDigits(n))


#using strings
N = 1
N = str(N)
count = 0
for each in N:
    count = count+1
print("Count: ", count)