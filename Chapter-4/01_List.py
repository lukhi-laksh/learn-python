friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])       # Prints first item: "Apple"
print(friends[5])       # Prints sixth item: "Aakash"
print(type(friends[3])) # Type of 345.06 → float

print(friends[-1])      # Last item: "Rohan"
print(friends[1:4])     # Slice: "Orange", 5, 345.06
print(len(friends))     # Total number of items in the list
print("Orange" in friends)  # Checks if "Orange" is in the list → True

print(friends[0])       # Prints first item: "Apple"
friends[0] = "Graps"  # Apple change to Graps  /// Unlike string Lists are mutable
print(friends)