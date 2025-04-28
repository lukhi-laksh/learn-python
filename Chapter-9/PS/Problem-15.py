word = ["Donkey", "bed", "ganda"]


with open("Problem-15_t.txt", "r") as f:
    content = f.read()

for words in word:
    content = content.replace(words, "#####")

    with open("Problem-15_t.txt", "w") as f:
        f.write(content)

    