name = "Laksh Lukhi"

print(len(name))  # Length of the string

print(name.endswith("Lukhi"))       # Checks if string ends with "Lukhi"
print(name.startswith("Laksh"))     # Checks if string starts with "Laksh"

print(name.lower())     # Converts to lowercase
print(name.upper())     # Converts to uppercase
print(name.title())     # Converts first letter of each word to uppercase

print(name.find("Lukhi"))   # Returns index of first occurrence of "Lukhi"
print(name.replace("Laksh", "Raj"))  # Replaces "Laksh" with "Raj"

print(name.isalpha())   # Checks if all characters are alphabetic (no space)
print(name.isdigit())   # Checks if string has only digits
print(name.isspace())   # Checks if string contains only whitespace
print(name.islower())   # Checks if all letters are lowercase
print(name.isupper())   # Checks if all letters are uppercase

print(name.strip())     # Removes leading/trailing whitespaces
print(name.split())     # Splits the string by space into a list
print(".".join(name))   # Joins each character with a dot
