def check_word(word):   
    with open("Problem-2.txt", "r") as f:
        data = f.read()

    if(data.find(word) != -1):
        print("Data found")
    else:
        print("Data not found")

check_word("Java")