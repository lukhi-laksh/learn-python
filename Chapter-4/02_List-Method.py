friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]  

friends.append("Laksh")                      # Adds "Laksh" at the end
friends.insert(2, "Banana")                  # Inserts "Banana" at index 2
friends.remove("Orange")                     # Removes the first occurrence of "Orange"
friends.pop()                                # Removes the last item from the list
print(friends)                               # Prints the current list

print(friends.index("Rohan"))                # Finds the index of "Rohan"
print(friends.count("Apple"))                # Counts how many times "Apple" appears
print(len(friends))                          # Returns the total number of items in the list
print(friends[::-1])                         # Reverses the list using slicing
print(friends[1:5])                          # Prints a slice from index 1 to 4
print("Apple" in friends)                    # Checks if "Apple" is in the list
print(type(friends[3]))                      # Shows the data type of item at index 3
