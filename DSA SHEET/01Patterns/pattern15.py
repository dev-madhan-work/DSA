#pattern function
def pattern(n):
    #rows
    for i in range((n-1),-1,-1):
        flag = 'A'
        ascii = ord(flag)
        for j in range(0,i+1):
            print(chr(ascii),end=" ")
            ascii= ascii+1
        print(end="\n")
#driver code
n = int(input("Enter no. of rows:"))
pattern(n)
