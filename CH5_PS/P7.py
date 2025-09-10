#Can you change the values inside a list which is contained in set S
s = {4, 6, 9, "Amrit",[4,9]}

'''ans=No, you cannot have a list as an element of a set in Python.

* Reason:

Set elements must be immutable (hashable).

A list is mutable (can be changed), so trying to add a list into a set will raise a TypeError.
'''