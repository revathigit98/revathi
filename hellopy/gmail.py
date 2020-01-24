l=("The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.")
ls=[]
l1=l.split()

l2=list(set(l1))
print(l2)
n=0
for i in l2:
    a=l1.count(i)
    l2[n]=(i,a)
    n=n+1
print(l2)
l2=sorted(l2,key=lambda x : x[1],reverse=True)
#print(l2)