fruits = {"Apple", "Orange", "Banana", "Mango"}

print(fruits)  # Prints the set

fruits.add("Pineapple")  # Adds "Pineapple" to the set
print(fruits)  # {'Apple', 'Banana', 'Mango', 'Orange', 'Pineapple'}

fruits.update(["Grapes", "Peach", "Apple"])  # Adds multiple items, "Apple" will be ignored as it's already there
print(fruits)  # {'Apple', 'Banana', 'Mango', 'Orange', 'Pineapple', 'Peach', 'Grapes'}

fruits.remove("Peach")  # Removes "Peach"
print(fruits)  # {'Apple', 'Banana', 'Mango', 'Orange', 'Pineapple', 'Grapes'}

fruits.discard("Mango")  # Removes "Mango", does not raise an error if "Mango" is not found
print(fruits)  # {'Apple', 'Banana', 'Orange', 'Pineapple', 'Grapes'}

print(fruits.pop())  # Removes a random element
print(fruits)  # Remaining elements

fruits.clear()  # Clears the set
print(fruits)  # set()

fruits = {"Apple", "Orange", "Banana"}
copy_fruits = fruits.copy()  # Creates a copy of the set
print(copy_fruits)  # {'Apple', 'Orange', 'Banana'}



