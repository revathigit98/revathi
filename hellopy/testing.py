# l=[1,2,3,5]
# l1=[]
# a=l[0]
# b=l[1]
# c=)l[2]
# d=l[3]
# e=(b*c*d)
# f=(a*c*d)
# g=(a*b*d)
# h=(a*b*c)
# l1.append(e),l1.append(f),l1.append(g),l1.append(h)
# prin

l=[1,2,3,5]
x=1
l1=[]
for i in l:
    while l:
        d=l.pop()
        x=x*d
        l1.append(x)
print(l1)
