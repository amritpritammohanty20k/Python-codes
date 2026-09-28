#  TYPE

a = 10
# print(type(a))

# CONVERSION 


# print(type(str(a)))

# ID - It gives a identity number to a object for rest of it lifetime
# that number is not neceserrily means smt.
 
x = 45
y = 89
z = [1,2,3]
xi = z

z.append(4)  # for refference 

# print(id(x))
# print(id(y))
# print(id(z))
# print(id(xi))

# ISINSTANCE()

# it cheacks if a object belongs to a perticular class/type
# retuns value in T/F

# n = "Amrit"
# print(isinstance(n, str))

# m = 93
# print(isinstance(m, int))

# j = [1,8,6]
# print(isinstance(j, tuple))

# INPUT IS INT OR NOT

# age = input("Enter ur age: ")

# if isinstance(age, int):
#     print("\nAge is an integer")
# else:
#     print("\nNot an integer")
    # This code does not work because input type always returns in str

# ....>
age = int(input("Enter ur age"))
if isinstance(age, int):
    print("Valid integer")