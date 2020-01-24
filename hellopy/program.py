# s=['revs','keerthi','py','sherif']
# for i in range(s):
#     if len(s) == len(max(s, key=len)):
#         print(s)

# def Nmaxelements(list1, N):
#     l = []
#
#     for i in range(0, N):
#         max1 = 0
#
#         for j in range(len(list1)):
#             if list1[j] > max1:
#                 max1 = list1[j];
#
#         list1.remove(max1);
#         l.append(max1)
#
#     print(l)
#
#
# # Driver code
# list1 = [1,4,6,7,3,6,8,9,3]
# N = 5
#
# # Calling the function
# Nmaxelements(list1, N)


x1=[2,5,6,3,69,6,8]
x=list(set(x1))
print(x)
#x.sort()
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if(x[i]>x[j]):
            x[i],x[j]=x[j],x[i]
print(x)
n=int(input("enter the number"))
print(x[-n])
print(x)