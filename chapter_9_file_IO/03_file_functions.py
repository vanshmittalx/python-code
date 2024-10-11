f = open("file.txt")
print(f.readline())
print(f.readlines())
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()