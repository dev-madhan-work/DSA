# *
# * *
# * * * 
# * * * *
# * * * *  *

#function
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('* ', end='')
        print(end='\n')





#driver code
pattern(5)