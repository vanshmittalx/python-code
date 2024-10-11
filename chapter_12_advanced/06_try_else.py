try:
    number = int(input("Enter number: "))
    print(number)
    
except Exception as e:
    print("Wrong input type")

else: #only run when try is True
    print("I am inside else")