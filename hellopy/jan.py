# def str_len(str):
#     count=0
#     for char in str:
#         count +=1
#     return count
# print(str_len("the"))  #to find the len of str
#
# def str_len(str):
#     d={}
#     for i in str:
#          keys=d.keys()
#          if i in keys:
#              d[i]+= 1
#          else:
#              d[i]=1
#     return(d)
# print (str_len("length of lthtt"))  #program to count the number of characters in a string




#
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))












