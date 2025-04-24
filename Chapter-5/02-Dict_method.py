d = {} #empty Dictionary

marks = {
    "Laksh": 90,
    "Harsh": 67,
    "Taksh": 46,
    "Daksh": 89,
    2: 56,
    3: "Darsh",
    "Suresh": 33,
}

print(marks.items())  # Returns all key-value pairs as (key, value) tuples
print(marks.keys())   # Returns all the keys in the dictionary
print(marks.values()) # Returns all the values in the dictionary

marks.update({"Laksh": 99, "Paresh": 67})  # Updates or adds new key-value pairs
print(marks)  # {'Laksh': 99, 'Harsh': 67, 'Taksh': 46, 'Daksh': 89, 2: 56, 3: 'Darsh', 'Suresh': 33, 'Paresh': 67}

print(marks.get("Laksh2"))  # None, key doesn't exist
# print(marks["Laksh2"])  # Uncommenting will cause KeyError

marks.pop("Taksh")  # Removes "Taksh" and returns its value
print(marks)  # {'Laksh': 99, 'Harsh': 67, 'Daksh': 89, 2: 56, 3: 'Darsh', 'Suresh': 33, 'Paresh': 67}

del marks["Harsh"]  # Removes "Harsh" key-value pair
print(marks)  # {'Laksh': 99, 'Daksh': 89, 2: 56, 3: 'Darsh', 'Suresh': 33, 'Paresh': 67}

marks.clear()  # Clears the dictionary
print(marks)  # {}

marks = {"Laksh": 90, "Harsh": 67, "Taksh": 46}
print(marks.popitem())  # Randomly removes and returns a key-value pair, e.g., ('Taksh', 46)
print(marks)  # {'Laksh': 90, 'Harsh': 67}

print(marks.setdefault("Laksh", 95))  # Returns 90 because "Laksh" exists
print(marks.setdefault("Rohan", 50))  # Adds "Rohan" with value 50 and returns 50
print(marks)  # {'Laksh': 90, 'Harsh': 67, 'Rohan': 50}

print("Laksh" in marks)  # True, because "Laksh" exists
print("Rohan" in marks)  # True, because "Rohan" was added
print("Suresh" in marks)  # False, because "Suresh" is not in the dictionary
