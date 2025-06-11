empty = []
hello = ['h', 'e', 'l', 'l', 'o']

for i in hello:
    empty.append(i)
j = 0
while(len(empty) != 0):
    hello[j] = empty[-1]
    
    j += 1
    empty.pop()
    

print(hello)