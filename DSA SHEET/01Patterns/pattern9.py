#     *    
#    * *   
#   * * *   
#  * * * *

def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')
        for j in range(2*i+1):
            print('*',end='')
        for j in range(n-i-1):
            print(' ',end='')
        print(end='\n')
    for i in range(n):
        for j in range(i):
            print(' ',end='')
        for j in range((2*n-1) - (i*2)):
            print('*',end='')
        for j in range(n):
            print(' ',end='')
        print('',end='\n')

n = int(input('Enter no. of rows:'))
pattern(n)