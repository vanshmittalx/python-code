a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
d = int(input("Enter number: "))
if a>b:
    if a>c:
        if a>d:
            print(a,"is the largest number")
        else:
            print(d,"is the largest number")
    else:
        if c>d:
            print(c,"is the largest number")
        else:
            print(d,"is the largest number")
else:
    if b>c:
        if b>d:
            print(b,"is the largest number")
        else:
            print(d,"is the largest number")
    else:
        if c>d:
            print(c,"is the largest number")
        else:
            print(d,"is the largest number")