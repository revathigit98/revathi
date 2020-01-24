# for i in range(0,4):
#     print(' '*(4-i-1)+'*'*(i+1))
#     for j in range(4-1,0,-1):
#        print('o'*(4-j)+'*'*(j))
for row in range(7):
    for col in range(7):
        if row+col==3 or col-row==3  or row-col==3 or row+col==9 :
            print("*",end="")
        else:
            print(end=" ")
    print()