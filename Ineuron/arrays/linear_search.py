#function definition
#space complexity : O(1)
#Time Complexity: O(n)
def linearSearch(li,x):
    for i in range(0,len(li)):
        if x == li[i]:
            return i
    return -1
#driver code
li = [1,22,33,44,65,333,55]
x = int(input("Enter x:"))
index = linearSearch(li,x)
print(x," found at ", index)