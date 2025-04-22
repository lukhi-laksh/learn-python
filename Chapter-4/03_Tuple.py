a = (4, 5, 2, 3, False, "Rohan", 44.7)        # Tuple with mixed data types
print(a)                                      # Prints the entire tuple

print(a[0])                                   # Prints the first element
print(a[-1])                                  # Prints the last element
print(len(a))                                 # Length of the tuple
print(a.count(5))                             # Counts how many times 5 appears
print(a.index("Rohan"))                       # Finds the index of "Rohan"
print(type(a[6]))                             # Shows the type of the last element
print(a[1:5])                                 # Slicing from index 1 to 4
print("Rohan" in a)                           # Checks if "Rohan" is present in the tuple