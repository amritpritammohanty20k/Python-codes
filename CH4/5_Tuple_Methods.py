# Use count() to find how many times the value 2 appears
a=(1,2,3,4,5,2,2,2,False,"Amrit")
print(a)
no=a.count(2)
print(no)

# 1. index(): Find the position of the value 2
index_2 = a.index(2)
print(index_2)  # Output: 1

# 2. len(): Get the number of elements in the tuple
length = len(a)
print(length)  # Output: 10

# 3. max() and min(): Find max and min values
a1=(1,2,3,4,5,6,7,8,9)
print(max(a1))  # Output: 9
print(min(a1))  # Output: 1

# 4. in keyword: Check if 2 and 60 are in the tuple
print(2 in a1)  # Output: True
print(60 in a1)  # Output: False

# 5. Tuple unpacking
a = (1, 2, 3, 4, 5, 2, 2, 2, False, "Amrit")

a1, b, c, d, e, *rest = a

print(a1, b, c, d, e)    # Prints first 5 values
print(rest)              # Prints the rest of the values 

# 6. Convert to list to modify, then back to tuple { this for changeing somthing in tuple}
x = list(a)
x.append(60)            # Add a new item
modified_tuple = tuple(x)
print("Modified tuple:", modified_tuple)  # Output: (10, 20, 30, 40, 50, 60)