# [12,16,18,24,3,5,8,10]
def rotationSearchHelper(arr, low, high, key):
    mid = low + ((high-low)//2)
    if low > high:
        return "NO MATCH"
    if arr[mid] == key:
        return mid
    
    if arr[mid] <= key and arr[low] <= arr[mid] and key >= arr[low]:
        return rotationSearchHelper(arr, low, mid - 1, key)

    elif arr[mid] >= key and arr[low] >= arr[mid] and key <= arr[high]:
        return rotationSearchHelper(arr, mid + 1, high, key)
    
    elif arr[high] <= arr[mid]:
        return rotationSearchHelper(arr, mid+1, high, key)
    
    elif arr[low] >= arr[mid]:
        return rotationSearchHelper(arr, low, mid -1 ,high, key)

    return -1
def searchInRotatedArray(arr,key):
    return rotationSearchHelper(arr, 0, len(arr)-1, key)

#driver code 
arr =  [12,16,18,24,3,5,8,10]
print(searchInRotatedArray(arr,10))
