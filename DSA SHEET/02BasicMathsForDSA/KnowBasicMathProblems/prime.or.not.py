n = int(input("Enter no:"))
for i in range(2, n//2+1):
    if n % i == 0:
         print(False)
         exit()

print(True)
