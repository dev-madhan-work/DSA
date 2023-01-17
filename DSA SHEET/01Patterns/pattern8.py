# **********
#  ********
#   ******
#    ****
#     **
#      *

def pattern(n):
    for i in range(n):
        for j in range(i):
            print(' ',end='')
        for j in range((2*n-1) - (i*2)):
            print('*',end='')
        for j in range(n):
            print(' ',end='')
        print('',end='\n')

#driver code 
n = int(input('Enter number of rows:'))
pattern(n)