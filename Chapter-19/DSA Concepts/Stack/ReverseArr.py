empty = []
hello = ['h', 'e', 'l', 'l', 'o']

for i in range(len(hello)):
    empty.append(hello[i])
j = 0
while(len(empty) != 0):
    hello[j] = empty[-1]
    
    j += 1
    empty.pop()
    

print(hello)