# l1=[1,2,3]
# l2=[1,3,4]
# l1.extend(l2)
# print(l1)
# print(l1+l2)
# l1.clear()
# print

x=[12,10,5,3]
s1=[]
for i in range(len(x)):
    s=x[::]
    s.pop(i)
    total =sum(s)
    s1.append(total)
    #s.append(x)
print("output",s1)


