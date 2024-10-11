word = "donkey"
with open("file.txt") as f:
    content = f.read()
newContent = content.replace(word, "######")
with open("file.txt", "w") as f:
    f.write(newContent)