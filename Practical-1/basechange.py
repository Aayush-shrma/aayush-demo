#pratcical - 10
def convertbase(number,base1,base2):
    decimalnum=int(number,base1)
    if base2==10:
        return decimalnum
    else:
        ans=""
        values="0123456789ABCDEF"
        while decimalnum>0:
            rem=decimalnum % base2
            ans=values[rem]+ans
            decimalnum //=base2

        return ans
 



number=input("Enter the number that you want :")
base1=int(input("Enter the base of the given num:"))
base2=int(input("Enter the base of num you wanna convert to :"))
converted=convertbase(number,base1,base2)
print(f"Your converted ans is {converted}")

