list1 = ["Rahul","Vansh","Parth"]
check = input("Enter name: ")
check = check.capitalize()
if check in list1:
    print("Name exists")
else:
    print("Name does not exist")