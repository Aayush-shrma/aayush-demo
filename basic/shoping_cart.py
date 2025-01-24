def shopping():
    print("Welcome to our store")
    print("what type of item would you like?")
    fruits = ['apple', 'banana', 'coconut', 'pineapple']
    grocery = ['salt', 'pepper', 'coffee', 'sugar']
    while True:
        items = input("Type A for fruits and Type B for grocery: ").upper()
        if items == 'A':
            while True:
                fruit = list(map(int, input(f"Choose:(write its no. in list):{fruits} = ").split()))
                for i in fruit:
                    if 1 <= i <= len(fruits):
                        print(f"{fruits[i-1]} is in your bag")
                    else:
                        print(f"Invalid choice: {i}")
                again = input("more fruits or not?:if then type yes else no: ").lower()
                if again != 'yes':
                    break
        elif items == 'B':
            while True:
                saman = list(map(int, input(f"Choose:(write its no. in list):{grocery} = ").split()))
                for i in saman:
                    if 1 <= i <= len(grocery):
                        print(f"{grocery[i-1]} is in your bag")
                    else:
                        print(f"Invalid choice: {i}")
                again = input("more groceries or not?:if then type yes else no: ").lower()
                if again != 'yes':
                    break
        else:
            print("Invalid input. Please try again.")
            continue
        shop_again = input("Do you want to shop for other items? Type 'yes' to continue or 'no' to stop: ").lower()
        if shop_again != 'yes':
            print("Thank you for shopping!")
            break

shopping()
