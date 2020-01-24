# a = "refrigerator"
# count = 0
# for i in a:
#   count = count+1
#   print(count)

# print ('e' in 'Umbrella')
# x='this is orange juice'
# print ('orange')

a = ['a','e','i','o','u','A','E','I','O','U',' ']
b = "Hello, have a good day"
for i in b:
  if i not in a:
    b = b[:b.index(i)]+b[b.index(i)+1:]
print (b)

# s1=input("enter the string")
# if(sorted(s1)==sorted(s2)):
#   print('the sring is anagram')
# else:
#   print('the strinf is not anagram')




