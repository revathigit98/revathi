#1 x=[1,2,3,4,2,3]
# l1=[]
# x=list(set(x))
# l1.append(x)
# print(l1)

#2 d={"name":"revs","s.no":21}
# d1 = {value:key for key,value in dict.items(d)}
# print(d1)  # "dict compehension"

# a=[1,2,3]
# b=[4,5,6]
# z=a+b
# print(z)

# z="hello"
# print (z[::-1])
x="hello"
y = {}
for i in x:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1
print(x)
print( "count each character:" +str(y))


#8 x=[1,2,3,4,5,6,7,8,9,10]
# y=[]
# z=[i for i in x if i%2==0]
# y.append(z)
# print(x)
# print("the new list:",y)

#4 x = [19, 21, 46]
# y = ['one', 'two', 'three']
# l= zip(x, y)
# print(list(l))










