
# # print(sum(d.append(values())))
# v=(sum(d.values()))
# print(v)
# # i for i in d.sum(values)

# result = {}
# for x in d:
#     for y in d.values():
#         result[y] = result.get(y, 0) + d[y]
#     print("values:",str(result))
# x=sum(d.values)
# print(x)


# for k,v in d.items():
#     for i in v:
#      if i > highest_total:
#         r_highest_total=k
#         highest_total=i
# print(r_highest_total,highest_
d={"a":[12,25,49] ,"b":[45,59,68]}
s={}
r_highest_total=''
highest_total=0
for k,v in d.items():
    d[k]={'tot':sum(v),'avg':round(sum(v)/len(v),2)}
    if max(v) > highest_total:
        r_highest_total=k
        highest_total=max(v)

print(r_highest_total,highest_total)
print(d[k])















