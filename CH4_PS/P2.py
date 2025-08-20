#Write a program to accept marks of 6 students and display them in a sorted manner.
mark=[]

f1=int(input('Enter student mark: '))
mark.append(f1)
f2=int(input('Enter student mark: '))
mark.append(f2)
f3=int(input('Enter student mark: '))
mark.append(f3)
f4=int(input('Enter student mark: '))
mark.append(f4)
f5=int(input('Enter student mark: '))
mark.append(f5)
f6=int(input('Enter student mark: '))
mark.append(f6) 
f7=int(input('Enter student mark: '))
mark.append(f7)
mark.sort() # this prints mark in sorted manner .
print(mark)