# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2 
# 1 

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,(n-i+1)+1):
            print(j,end=' ')
        print('\n')

#driver code
n = int(input("Enter number of lines:"))
pattern(n)
