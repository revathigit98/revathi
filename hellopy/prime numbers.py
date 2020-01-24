num=int(input("enter the numbers"))
for i in range(2,num):
    # if(num==3):
    #     print(num,"is a prime number")
    #     break
    # else:
    #     print(num,"not a prime number")
    #     break

    if(num%i==0):
        print(num,"is not prime number")
        break
    else:
        print(num,"is a prime number")
        break