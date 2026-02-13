# Useful Python List Methods

# APPEND()
unknown=[' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ']
unknown.append("7") # it add a new datatype to a list 
print(unknown) 

# SORT()
x=[1,4,5,8,2,0,54] # sort the values in assending order
x.sort()
print(x)

# REVERSE()
x.reverse() # reverse the text
print(x)


# INSERT()
x.insert(3,325851651) # insert a vlaue at '3' index
print(x)


# POP()
x.pop(2) # pop out the index
print(x)
value=x.pop(2)

print(value) # prints the value 

# REMOVE()
x.remove(2) #remove the no 
print()
''' ............................................................................................................................................................''' 

# clear() - removes all elements from the list
x1 = [1, 2, 3]
x1.clear()
print(x1)  # []

# count() - returns number of times a value appears
x2= [1, 2, 2, 3, 2]
print(x2.count(2))  # 3

# index() - returns the index of the first occurrence of a value
x3 = [10, 20, 30, 20]
print(x3.index(20))  # 1

# copy() - returns a shallow copy of the list
x4= [1, 2, 3]
y = x4.copy()
print(y)  # [1, 2, 3]

# extend() - extends the list by appending elements from another iterable
x5 = [1, 2]
x5.extend([3, 4])
print(x5)  # [1, 2, 3, 4]
