with open("problem-7.txt", "r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
    if (num != ""):
        print(int(num))
