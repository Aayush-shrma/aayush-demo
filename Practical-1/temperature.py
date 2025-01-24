   #PRACTICAL NO -1 
x=input("If in celsius press 1 if  Fahrenheit press-0:")
a=int(input("Whats your tempreture?:"))
if x=='1':
  y=((a*9/5))+32
  print(f"your tempreture in fahrenheit is {y:.2f}")
elif x=='0':
    z=((a-32)*5)/9
    print(f"your tempreture in celsius is{z:.2f}")
else:
   print("invalid input")
   