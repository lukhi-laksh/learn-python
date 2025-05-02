freq = {}

numbers = [1, 2, 2, 3, 1, 4, 2, 1, 5, 12, 12, 14]

# Hashing logic
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(f"Number {key} appears {freq[key]} times")

print(freq)