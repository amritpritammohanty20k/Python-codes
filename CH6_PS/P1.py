# Find greatest of 3 number entered by the user 

n1=int(input("Enter the number 1:  "))       # type:ignore
n2=int(input("Enter the number 2:  "))    # type:ignore
n3=int(input("Enter the number 3:  "))       # type:ignore

if (n1>n2 and n1>n3):
    print("N1 is Greatest")
elif(n2>n1 and n2>n3):
    print("N2 is gratest")
else:
    print("N3 is greatest")

