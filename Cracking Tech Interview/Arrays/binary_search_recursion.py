def binarySearchHelper(arr,x,low,high):
    # print("Called")
    if low > high:
        return "No Match"
    # else:
    while low <= high:
        mid = low + ((high - low)//2)
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binarySearchHelper(arr,x,low, mid -1)
        else:
            return binarySearchHelper(arr, x, mid+1, high)

def binarySearch(arr,x):
    return binarySearchHelper(arr, x, 0, len(arr)-1)

arr = [1,22,33,44,65,75,85]
x = int(input("Enter x: "))
index = binarySearch(arr, x)
print(x," found at ", index)