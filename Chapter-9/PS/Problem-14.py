word = "Dony"

with open("Problem-14_t.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("Problem-14_t.txt", "w") as f:
    f.write(contentNew)

    