# Check the marks of the student.
# Total subjects = 3, each has 100 marks
# Full marks = 300
# Passing percentage = 45%
# Passing mark for each subject = 40



x = int(input("Enter the marks of Mathematics  : "))
y = int(input("Enter the marks Physics : "))
z =int(input("Enter the marks Chemistry : "))

if x>=40 and y>=40 and z>=40 :
    print("Status: PASSED")
else:
    print("Status: FAIL")

full_mark = 300
total = x+y+z
percentage = (total/full_mark*100)
print("\n---Result---")
print("Total_Marks : ",total)
print("PERCENTAGE : ",round(percentage,2))



''' Write a program that accepts marks for 5 subjects, each out of 100.
 Calculate total, average, and percentage.
 Grade system:
 A: 85% and above
 B: 70%-84%
 C: 55%-69%
 D: 45%-54%
 F: Below 45% or any subject below 40 marks
 Show the grade and result (Pass/Fail).'''

# Subject Declaration ....

a = int(input("Enter the marks of Mathematics : "))
b = int(input("Enter the marks of Physics : "))
c = int(input("Enter the marks of Chemistry : "))
d = int(input("Enter the marks of I.T : "))
e = int(input("Enter the marks of Sanskrit : ")) 

# Marks Calculation...

Full_marks = 500
Total_marks = a + b + c + d + e
Avarage = Total_marks/5
Percentage = (Total_marks/Full_marks)*100

# Grade distribution...

if (Percentage >= 85 ):
    print("Grade: 'A' ")
elif (Percentage >= 70 or Percentage <= 84 ):
    print("Grade: 'B' ")
elif (Percentage >= 55 or Percentage <= 69 ):
    print("Grade: 'C' ")
elif (Percentage >= 45 or Percentage <= 54 ):
    print("Grade: 'D' ")
elif (Percentage < 45 ):
    print()


