#sorting
def sorting(arr):
   for i in range(0,(len(arr)-1)):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
         
        
   return arr
#driver code
arr = [1,2,4,3,22,6,5,8]
print(len(arr)-2)
sortedArray = sorting(arr)
print(sortedArray)
print("Largest Element:",sortedArray[len(sortedArray)-1])