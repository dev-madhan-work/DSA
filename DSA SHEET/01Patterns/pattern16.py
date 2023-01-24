#pattern function
def pattern(n):
    flag = 'A'
    ascii = ord(flag)
    for row in range(0,n):
        for j in range(0,row+1):
            print(chr(ascii),end=" ")
        ascii = ascii+1
        print(end="\n")

#driver code
n = int(input("Enter no. of rows:"))
pattern(n)