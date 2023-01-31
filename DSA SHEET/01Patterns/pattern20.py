def pattern(n):
    #rows
    for i in range(n):
        #column
        for j in range(0,(i+1)):
            print('*',end='')
        for j in range(0,((2*n)-2*(i+1))):
            print(' ',end='')
        for j in range(0,(i+1)):
            print('*',end='')
        print(end='\n')
    for i in range(n-2,-1,-1):
        #column
        for j in range(0,(i+1)):
            print('*',end='')
        for j in range(0,((2*n)-2*(i+1))):
            print(' ',end='')
        for j in range(0,(i+1)):
            print('*',end='')
        print(end='\n')
#driver code
n = int(input('Enter no. of rows:'))
pattern(n)