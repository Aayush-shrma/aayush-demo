#practical-4

no=int(input("Enter the length of list:"))
list=[]
for i in range(0,no):
    numbers=int(input(f"Enter the {i}value for list:"))
    list.append(numbers)

total=sum(list)
avg=total/no
print(f"your avg is:{avg}")