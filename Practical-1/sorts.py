#practical - 8

num=list(map(int,input("Write the number in the given list to sort with space between each one:").split()))
order=int(input("which order would you like to sort?:"))
if order==1:
    asc_order=sorted(num)
    print(asc_order)
elif order==0:
    des_order=sorted(num,reverse=True)
    print(des_order)
else:
    print("Invalid")