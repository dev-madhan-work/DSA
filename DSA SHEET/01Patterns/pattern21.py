def pattern(n):
    #rows
    for i in range(n):
        #stars
        if i == 0 or i == (n-1):
            for j in range(n):
                print("*",end='')
        else:
            #stars
            for j in range((n - n//2)//2):
                print("*",end='')

            #spaces
            for j in range(0,n-2):
                print(' ',end='')

            #stars
            for j in range((n - n//2)//2):
                print('*',end='')
        print(end='\n')

#driveer code
n = int(input("Enter no. of rows:"))
pattern(n)