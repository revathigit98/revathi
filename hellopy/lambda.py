# g=(lambda x,y :x+y)
# print("g=",g(2,3))

# s='this is the lambda functions'
# (lambda s:print(s))(s)

r=(lambda a:a+15)
print(r(15))
s=filter(lambda x,y:x*y)
print(s(2,3)) # to create a lambda func add 15 to other number and mul to x,y

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# def arg_mul(n):
#     return lambda x:x*n
# result = arg_mul(2)
# print("double the value =",result(15))


