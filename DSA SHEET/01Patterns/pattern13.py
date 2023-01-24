#pattern function
def pattern(n):
    #rows
    count = 0
    for row in range(0,n):
        for i in range(0,row+1):
            count = count+1
            print(count,end=" ")
        print(end="\n")

#driver code
n = int(input("Enter no. of rows:"))
pattern(n)