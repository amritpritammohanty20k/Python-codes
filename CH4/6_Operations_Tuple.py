# Tuple Operations in Python

# 1. Creating a tuple
t = (1, 2, 3, 4, 5)
print(t)

# 2. Indexing - Access elements by position
print(t[0])
print(t[-1])

# 3. Slicing - Get a part of the tuple
print(t[1:4])

# 4. Length - Total number of elements
print(len(t))

''' 5. Concatenation/Addition - Combine two tuples'''
t1 = (10, 20)
t2 = (30, 40)
combined = t1 + t2
print(combined)

# 6. Repetition - Repeat a tuple
print(t1 * 3)

# 7. Membership - Check if item exists
print(3 in t)
print(100 in t)

# 8. Iteration - Loop through tuple items
print()
for item in t:
    print(item)

# 9. Tuple Packing and Unpacking
packed = (100, 200, 300)
a, b, c = packed  # Unpacking
print( a, b, c)

# 10. Unpacking with *
t3 = (1, 2, 3, 4, 5, 6)
x, y, *rest = t3
print(x)
print(y)
print(rest)

# 11. count() - Count occurrences of an item
t4 = (1, 2, 2, 3, 4, 2)
print(t4.count(2))  # How many times 2 appears

# 12. index() - Get first index of an item
print(t4.index(2))

# 13. max() and min() - Maximum and minimum values
numeric_tuple = (10, 20, 5, 40, 15)
print( max(numeric_tuple))
print(min(numeric_tuple))

# 14. sum() - Add all numbers in tuple
print(sum(numeric_tuple))

# 15. sorted() - Returns a sorted list (does not change original tuple)
print(sorted(numeric_tuple))
print(numeric_tuple)

# 16. Convert tuple to list to modify it, then back to tuple
mod_tuple = (1, 2, 3)
temp_list = list(mod_tuple)  # Convert to list
temp_list.append(4)          # Modify list
mod_tuple = tuple(temp_list)  # Convert back to tuple
print(mod_tuple)

# 17. A nested tuple (tuple inside another tuple)
t2 = (1, (4, 5, 6), 2, (7, 8))

print(t2[0])       # → 1 (first element)
print(t2[1])       # → (4, 5, 6) (second element is a tuple)
print(t2[1][2])    # → 6 (third element of the inner tuple)
print(t2[3][0])    # → 7 (first element of the last inner tuple)
