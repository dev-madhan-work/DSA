#binary search using iteration
def binarySearch(arr, x, low, high):
    while low <= high:
        mid = low + ((high - low)//2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = high -1
        else:
            low = low+1
    return "Not found"
#driver code
arr = [10,20,20,30,40,50,80]
x = int(input("Enter x:"))
index = binarySearch(arr, x, 0, len(arr)-1)
print(x," found at ", index)