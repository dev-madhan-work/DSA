#pattern definition

# def pattern(n):
#     totalCharsInRow = 2*n-1
#     #rows
#     for i in range(1,n+1):
#         #columns
#         charsCol = (2*i-1)
#         spaces = totalCharsInRow - charsCol
#         for j in range(0,spaces//2):
#             print(" ",end="")
#         characterAscii = ord('A')-1
#         if i == 1:
#             print(chr(characterAscii+1),end="")
#         else:
#             for k in range(0, (charsCol//2)+1):
#                 characterAscii = characterAscii + 1
#                 print(chr(characterAscii), end="")
#             for l in range(1, (charsCol//2)+1):
#                 characterAscii = characterAscii - 1
#                 print(chr(characterAscii), end="")
#         for m in range(0, spaces//2):
#             print(" ",end="")
#         print(end="\n")


##strivers approach using symmetric
def pattern(n):
    totalCharsInRow = 2*n-1

    for i in range(0,n):
        charsCol = (2*i+1)
        spaces = (totalCharsInRow - charsCol)//2
        breakpoint = charsCol//2
        for j in range(0,spaces):
            print(" ",end="")
        characterAscii = ord('A')
        for k in range(0,charsCol):
            print(chr(characterAscii),end="")
            if k < breakpoint:
                characterAscii = characterAscii+1
            else:
                characterAscii = characterAscii - 1
        for l in range(0,spaces):
            print(" ",end="")
        print(end="\n")

#driver code
n=int(input("Enter no. of rows:"))
pattern(n)