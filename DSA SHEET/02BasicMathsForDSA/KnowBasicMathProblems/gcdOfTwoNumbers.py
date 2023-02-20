num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
divisorMax = num1 if (num1<num1) else num2
result = 0
for i in range(1,(divisorMax+1)):
    if num1 % i == 0 and num2 % 2 ==0:
        result = i

print("GCD:", result)