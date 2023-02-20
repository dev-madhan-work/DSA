def checkArmstrong(n):
    temp = n
    digits = 0
    while temp > 0:
        temp = temp // 10
        digits = digits+1
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit**digits)
        temp = temp // 10
    
    if sum == n:
        return True
    else:
        return False


n = int(input("Enter no:"))
print(checkArmstrong(n))