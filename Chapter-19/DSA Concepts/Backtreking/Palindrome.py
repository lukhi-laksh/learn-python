def laksh(stri, first, last):
    if first >= last:
        return True
    
    if stri[first] != stri[last]:
        return False
    
    return laksh(stri, first + 1, last -1)


string = "nayan"
print(laksh(string, 0, len(string) - 1))
        