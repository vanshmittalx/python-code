f = open("poem.txt")
content = f.read()
if ("Twinkle" in content):
    print("Twinkle is present")
else:
    print("not present")
f.close()