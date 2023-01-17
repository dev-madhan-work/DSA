# 1
# 22
# 333
# 4444
# 55555

def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=' ')
        print(end='\n')

#driver code
n = int(input('Enter number of Lines:'))
pattern(n)