number = int(input("Enter number: "))
for i in range(2,number):
    if number % i == 0:
        print("Not prime")
        break
else:
    print("Prime")