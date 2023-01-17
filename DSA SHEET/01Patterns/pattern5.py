# * * * * * 
# * * * * 
# * * *
# * * 
# * 

def pattern(n):
    for i in range(1,n+1):
        for j in range((n-i+1)):
            print('* ',end='')
        print('\n')

#driver code
n = int(input("Enter number of lines:"))
pattern(n)
