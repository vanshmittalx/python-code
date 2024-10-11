a = int(input("Enter number"))
b = int(input("Enter number"))

if (b==0):
    raise ZeroDivisionError("division by 0 is not supported")
else:
    print(a/b)