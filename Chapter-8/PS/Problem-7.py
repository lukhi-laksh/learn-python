def rem(l, word):
    for item in l:
        if(item == word):
            l.remove(word)
    return l
        
l = ["laksh", "shubham", "rohan", "an"]

print(rem(l, "an"))
