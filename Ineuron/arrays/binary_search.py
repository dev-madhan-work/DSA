#function definition
def binarySearch(li,x,left,right):
        while left <= right:
            mid = left + (right-left)//2
            if li[mid] == x:
                print("mid",mid)
                return mid
            elif li[mid] < x:
                return binarySearch(li,x,mid+1,right)
            else:
                return binarySearch(li,x,left,mid-1)
        return "Not found"
#driver code
##Must be a sorted Array. Either in ascending or descending
li = [1,22,33,44,65,75,85]
x = int(input("Enter x:"))
index = binarySearch(li,x,0,len(li)-1)
print(x," found at ",index)