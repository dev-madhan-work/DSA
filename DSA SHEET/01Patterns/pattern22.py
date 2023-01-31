#def 
def pattern(n):
    for i in range(2*n-1):
        #cols
        for j in range(2*n-1):
            top = i
            left = j
            right = (2*n)-1-j
            bottom = (2*n)-1-i
            number = min(top,left,right,bottom)
            print(n - number,end='')
        print(end='\n')

n = int(input("Enter no. of rows:"))
pattern(n)