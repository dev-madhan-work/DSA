#pattern definition
def pattern(n):
    #rows
    for i in range(n):
        #column
        #first set of stars
        for j in range(0,((2*n - 2*i)//2)+1):
            print('*',end='')
        
        #spaces
        for j in range((2*i)):
            print(' ',end='')

        #second set of stars:
        for j in range(0,((2*n - 2*i)//2)+1):
                print('*',end='')
        print(end='\n')

    #symmetry starts
    for i in range((n-1),-1,-1):
        #column
        #first set of stars
        for j in range(0,((2*n - 2*i)//2)+1):
            print('*',end='')
        
        #spaces
        for j in range((2*i)):
            print(' ',end='')

        #second set of stars:
        for j in range(0,((2*n - 2*i)//2)+1):
                print('*',end='')
        print(end='\n')


#driver code
n = int(input('Enter no. of rows:'))
pattern(n)