def laksh(s, count):
    if count == -1:
        return 0
    
    if s[count] == "a" or s[count] == "e" or s[count] == "i" or s[count] == "o" or s[count] == "u":
        return 1 + laksh(s, count - 1)
    else:
        return laksh(s, count - 1)
    
s = "counting"
print(laksh(s, len(s) - 1))