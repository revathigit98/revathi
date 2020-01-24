# word=input('enter the string')
# vowels=[]
# for vowels in word:
#     if vowels[0] in 'aeiou':
#         vowels.append(word)
#     print(word)

words = input('enter the string')
for i in words:
    if i[0] in 'aeiou':
        print('the vowels are:',i)

l=[ c for c in words if c in 'aeiou']

print(l)