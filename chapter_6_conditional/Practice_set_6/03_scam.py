string = input("Enter string: ")
spam1 = "make a lot of money"
spam2="buy now"
spam3="subscribe this"
if spam1 in string:
    print("This text likely appears in spam messages.")
elif spam2 in string:
    print("This text likely appears in spam messages.")
elif spam3 in string:
    print("This text likely appears in spam messages.")
else:
    print("This text does not appear to be from a spam message.")