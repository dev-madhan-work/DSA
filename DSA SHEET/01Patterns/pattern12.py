#pattern function
def pattern(n):
    #rows
    for row in range(0,n):
        #printing numbers
        for i in range(1,row+2):
            print(i,end="")
        #printing spaces
        for i in range(1,((2*n) - (2*i))):
            print(" ",end="")
        #printing numbers
        for i in range((row+1),0,-1):
            print(i,end="")
        print(end="\n")
#driver code
n = int(input("Enter no. of rows:"))
pattern(n)