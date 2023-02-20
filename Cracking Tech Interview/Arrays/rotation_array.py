# 12 16 18 24 3 5 8 10

def arrayRotationHelper(arr, low, high):
    while low <= high:
        mid = low + ((high-low)//2)
        if arr[mid] > arr[mid+1] and mid < high:
            return mid
        if arr[mid] < arr[mid-1] and low < mid:
            return mid-1
        
        if arr[mid] < low:
            return arrayRotationHelper(arr, low, mid-1)
        return arrayRotationHelper(arr, mid+1, high)
    

#driver code
arr = [12,16,18,2,4,5,8,10]
result = arrayRotationHelper(arr, 0, len(arr)-1)
print("Pivot Point:",result)