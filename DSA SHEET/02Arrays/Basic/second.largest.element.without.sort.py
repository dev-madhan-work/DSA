# #findSecondLargestNumbe function
# def findSecondLargestNumbe(arr):
#     first = 0
#     second = 0
#     for i in range(len(arr)):   
#         if arr[i] > first:
#             first = arr[i]
#         if arr[i] > second and arr[i] < first:
#             second = arr[i]
#     return second





# #driver code 
# arr = [150,3,8,2,22,1,6,100,50,125]
# secondLargestElemt = findSecondLargestNumbe(arr)
# print("Second largest element:",secondLargestElemt)

A = [1,2,3,4]
x = 1
# index = 
i = 0
print('variable at',i,"Before rotation",   A[i])
print('variable at',i,"after rotation",   A[(i+x)%len(A)])
rotatioArray = []
for j in range(len(A)):
    rotatioArray.append(A[(j+x)%len(A)])
print("B:",rotatioArray)


