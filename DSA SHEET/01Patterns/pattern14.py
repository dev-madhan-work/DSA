#pattern function
def pattern(n):
    #rows
    
    for row in range(0,n):
        flag = 'A'
        ascii = ord(flag)
        for i in range(0,row+1):
            print(chr(ascii),end=" ")
            ascii = ascii+1
        print(end="\n")

#driver code
n = int(input("Enter no. of rows:"))
pattern(n)