empty = []
hello = ['h', 'e', 'l', 'l', 'o']

for i in range(len(hello)):
    empty.append(hello[i])
j = 0
while(len(empty) != 0):
    hello[j] = empty.pop()
    
    j += 1
    

print(hello)