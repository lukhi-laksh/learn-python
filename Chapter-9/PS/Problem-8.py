f = open("problem-9.txt")
content = f.read()
if("twinkle" in content):
    print("word find in file")
else:
    print("word in not find in file")
f.close()