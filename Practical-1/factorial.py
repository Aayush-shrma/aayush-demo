#practical-6
def factorialgive(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorialgive(num-1)
    

num=int(input("enter  a numebr you wanna check fatcorial for :"))
factorial=factorialgive(num)
print(f"Your answer is:{factorial}")