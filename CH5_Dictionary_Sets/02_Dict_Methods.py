marks = {
    "Amrit":100,
    "Omm":95,
    "Krishna":101,
    "Don":87,
    "list":[1,4,9]
}
''' Dictionary Methods'''
 
 #1.ITEMS()
print(marks.items()) # Returns a list of (key,value) tuples.

#2.KEYS()
print(marks.keys()) # Returns a list containing dictionary keys.

#3.VALUES()
print(marks.values()) # Returns a list containing values .
#4.UPDATE()
marks.update({"Krishna":98,"puchl":199}) # Returns a list containing updated values 
                             # Unlike String its UPDATED the whole dictionary . 
                             # It also adds a new value .
                             # e.g:: krishna:100 - krishna140(the new value replaces the old one)
print(marks)

#4.GET()
print(marks.get("Amrit")) #Retuns the value of the specific key .
                          #If the key is not existed then it retuns [NONE]


'''THE DIFFERENCE BETWEEN'''#GET AND # [ ]


'''
print(marks.get("Amrit2")) * Prints "None" if the key is not exsited * .
print(marks["Amrit2"]) * Returns "Error" if the key is not exsited *
'''

# 5. pop() - Removes a key and returns its value
removed_value = marks.pop("Krishna")
print(removed_value)   # Output: 101
print(marks)           # 'Krishna' is removed

# 6. popitem() - Removes and returns the LAST inserted key-value pair
last_item = marks.popitem()
print(last_item)       # Example Output: ('list', [1, 4, 9]) (depends on last inserted)
print(marks)

# 7. setdefault() - Returns value of a key. 
# If key not found, adds the key with a default value.
print(marks.setdefault("Don", 90))      # Key exists → Output: 87 (no change)
print(marks.setdefault("Sita", 99))     # Key does not exist → Adds 'Sita': 99
print(marks)  

# 8. copy() - Makes a copy of the dictionary (so original is safe)
marks_copy = marks.copy()
marks_copy["Omm"] = 60                  # Change in copy does not affect original
print("Original:", marks)              
print("Copy:", marks_copy)              

# 9. clear() - Removes everything from the dictionary
marks.clear()
print(marks)  # Output: {}
