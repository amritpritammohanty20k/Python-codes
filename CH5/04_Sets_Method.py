# Creating a set (duplicates are removed automatically)

fruits = {"apple", "banana", "mango", "apple"}
print(fruits)  # Output: {'banana', 'mango', 'apple'}

''' Useful Set Methods '''

# 1. add() - Add a single new item
fruits.add("orange")
print(fruits)  # Output: {'banana', 'mango', 'apple', 'orange'}

# 2. update() - Add multiple items at once (can take list, tuple, another set)
fruits.update(["grape", "papaya"])
print(fruits)

# 3. remove() - Remove a specific item (gives error if not present)
fruits.remove("banana")
print(fruits)

# 4. discard() - Remove a specific item (does NOT give error if item is missing)
fruits.discard("kiwi")  # kiwi not present, no error
print(fruits)

# 5. pop() - Removes and returns a random item (since sets are unordered)
removed = fruits.pop()
print("Removed:", removed)
print(fruits)

# 6. clear() - Remove everything from the set
temp = fruits.copy()  # making a copy to clear
temp.clear()
print(temp)  # Output: set()

# 7. copy() - Make a copy of a set
new_set = fruits.copy()
print("Copy of fruits:", new_set)

''' Set Operations (very useful) '''

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 8. union() - Combine both sets (no duplicates)
print("Union:", a.union(b))  # Output: {1, 2, 3, 4, 5, 6}

# 9. intersection() - Items common in both sets
print("Intersection:", a.intersection(b))  # Output: {3, 4}

# 10. difference() - Items in a but not in b
print("Difference:", a.difference(b))  # Output: {1, 2}

# 11. symmetric_difference() - Items NOT common in both sets
print("Symmetric Difference:", a.symmetric_difference(b))  # Output: {1, 2, 5, 6}

# 12. issubset() - Checks if all items of one set are in another
small = {1, 2}
big = {1, 2, 3, 4, 5}
print("Is small a subset of big?", small.issubset(big))  # True

# 13. issuperset() - Checks if a set contains all items of another
print("Is big a superset of small?", big.issuperset(small))  # True

# 14. isdisjoint() - Checks if two sets have NO items in common
x = {7, 8}
y = {9, 10}
print("Are x and y disjoint?", x.isdisjoint(y))  # True
