x=['reva','krish']
l=[]
for i in x:
    j=i.title()
    if (i==j):
        l.append(i)
    else:
        t=i.upper()
        l.append(t)
print(l)