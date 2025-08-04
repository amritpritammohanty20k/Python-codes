# Commonly Used Python String Functions with Simple Examples n outputs .


#  len()function - returns the length of thr variable
a='krishna'
print(len(a))

# endswith()function - tells whether variable ends with 'hna'or not .
print(a.endswith("hna"))
# startswith()function - tells whether variable start with 'kr'or not.
print(a.startswith("kr"))
'''Example --- Since name is KRISHNA'''

#capitalize()function - if the name is "amrit" , it convert it to "Amrit"
'''ONLY THE 1ST ALPHABET GOT CAPITALIZED'''
b='amrit'
print(b.capitalize())

text = "  Hello World 123!  "

# lower(): Convert all characters to lowercase
print(text.lower())  # Output: "  hello world 123!  "

# upper(): Convert all characters to uppercase
print(text.upper())  # Output: "  HELLO WORLD 123!  "

'''
# strip(): Remove spaces from both ends
print(text.strip())  # Output: "Hello World 123!"

# lstrip(): Remove spaces from the left side only
print(text.lstrip())  # Output: "Hello World 123!  "

# rstrip(): Remove spaces from the right side only
print(text.rstrip())  # Output: "  Hello World 123!"
'''

# replace(): Replace part of the string with another
print(text.replace("World", "Universe"))  # Output: "  Hello Universe 123!  "

# find(): Returns the index of the first match of the substring
print(text.find("World"))  # Output: 8

# index(): Same as find() but gives an error if not found
print(text.index("World"))  # Output: 8

# count(): Counts how many times a word/character appears
print(text.count("l"))  # Output: 3

# isalpha(): Checks if all characters are letters (no numbers or spaces)
print("Hello".isalpha())  # Output: True
print("Hello123".isalpha())  # Output: False

# isdigit(): Checks if all characters are numbers
print("123".isdigit())  # Output: True
print("123abc".isdigit())  # Output: False

# isalnum(): Checks if all characters are letters or numbers (no symbols or spaces)
print("Hello123".isalnum())  # Output: True
print("Hello 123".isalnum())  # Output: False

# isspace(): Checks if the string only has spaces
print("   ".isspace())  # Output: True
print("Hello".isspace())  # Output: False

# islower(): Checks if all letters are lowercase
print("hello".islower())  # Output: True
print("Hello".islower())  # Output: False

# isupper(): Checks if all letters are uppercase
print("HELLO".isupper())  # Output: True
print("Hello".isupper())  # Output: False

# split(): Splits the string into parts using a space or character
print(text.split())  # Output: ['Hello', 'World', '123!']
print("a,b,c".split(","))  # Output: ['a', 'b', 'c']

# join(): Join list items into a string using a separator
print("-".join(["a", "b", "c"]))  # Output: "a-b-c"

# format(): Insert values into a string
name = "amrit"
age = 19
print("My name is {} and I am {} years old".format(name, age))  # Output: My name is amrit and I am 19 years old

# f-string: Another way to insert variables 
print(f"My name is {name} and I am {age} years old")  # Output: My name is amrit and I am 19 years old
