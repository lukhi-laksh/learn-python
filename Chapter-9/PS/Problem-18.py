with open("Problem-16_t.txt") as f:
     content = f.read()

with open("Problem-16_copy.txt") as t:
    contents = t.read()

if(content == contents):
    print("both are same")
else:
    print("both are not same")