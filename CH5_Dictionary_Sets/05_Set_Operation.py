# 1. UNION
s1={1,2,58}
s2={1,8,65,10}
print(s1.union(s2)) # Returns the merged value of two sets except the common one!

# 2. INTERSECTION
s3={2,4,8,10}
s4={2,4,9,3,7}
print(s3.intersection(s4)) # Returns the common value only .


# Example sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 3. difference() - Items in 'a' but NOT in 'b'
print("Difference (a - b):", a.difference(b))  # Output: {1, 2}

# 4. symmetric_difference() - Items NOT common in both sets
print("Symmetric Difference:", a.symmetric_difference(b))  # Output: {1, 2, 5, 6}

# 5. issubset() - Check if all items of 'a' are inside 'b'
small = {1, 2}
big = {1, 2, 3, 4}
print("Is small inside big?", small.issubset(big))  # Output: True

# 6. issuperset() - Check if 'big' contains all items of 'small'
print("Is big covering small?", big.issuperset(small))  # Output: True

# 7. isdisjoint() - Check if two sets have NO items in common
x = {7, 8}
y = {9, 10}
print("Are x and y completely different?", x.isdisjoint(y))  # Output: True
