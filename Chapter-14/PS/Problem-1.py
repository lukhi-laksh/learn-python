try:
    with open("text1.txt") as f:
        f.read()
except Exception as e:
    print(e)

    
try:
    with open("text2.txt") as f:
        f.read()
except Exception as e:
    print(e)

    
try:
    with open("text3.txt") as f:
        f.read()
except Exception as e:
    print(e)


print("Thank You")