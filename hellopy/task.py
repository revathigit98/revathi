#1 x=['abc','abc','xyz','zxy']
# s=[]
# x=list(set(x))
# s.append(x)
# print(s)

# x=[1,2,3,4,5,6,1,2,4,5,3,5]
# n=int(input("enter the number"))
# print("enter the number")
# for i in x:
#     l=x.count(i)
# print(l)


#3 x=[1,2,3,4]
# l1=1
# for i in x:
#     l1=l1*i
# print(l1)

#4 x=[1,3,4,5,6,7,2,8]
# x.sort()
# print(x)
# l=[]
# n=int(input("enter the number"))
# while n>0:
#     a=x[-n]
#     l.append(a)
#     n-=1
# print(l)



#5 def check(string, sub_str):
#     if (string.find(sub_str) == -1):
#         print("NO")
#     else:
#         print("YES")
# string = "revathi"
# sub_str = "rev"
# check(string, sub_str)

#6 x = "abcdef"
# y = "defah"
# x1=0
# x2=0
# = set.intersection(set(y), set(x))
# for l in set(y):
#     x1 += x.count(l)
# for l in set(x):
#     x2 += y.count(l)
# num = min(x1,x2)
# print (num)


#8 l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# d = {}
# for a, b in l:
#     d.setdefault(a, []).append(b)
# print (d)


# x=['abc','bcd','ghi','jkl','ggg']
# print(x[::2])

# 10result_str="";
# for row in range(0,7):
#     for column in range(0,7):
#         if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str);









