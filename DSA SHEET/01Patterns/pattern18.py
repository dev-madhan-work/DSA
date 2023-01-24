#def pattern
def pattern(n):
    for i in range(0,n):
        charAscii = ord('A')+(n-1)
        for j in range(charAscii-i,charAscii+1):
            print(chr(j),end="")
        print(end="\n")
#driveer code
n = int(input("Enter no. of rows:"))
pattern(n)