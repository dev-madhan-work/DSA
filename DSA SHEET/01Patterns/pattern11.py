# 1
# 01
# 101
# 0101
# 10101

def pattern(n):
    for i in range(1,n+1):
        if i%2 != 0:
            start = 1
        else:
            start = 0
        for j in range(i):
            if start == 1:
                print(start,end='')
                start = start - 1
            else:
                print(start,end='')
                start = start + 1
        print(end='\n')

n = int(input('Enter no. of rows:'))
pattern(n)