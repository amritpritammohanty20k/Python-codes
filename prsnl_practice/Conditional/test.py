# F StR
# name = "Amrit Pritam Mohanty"
# program = "B.Tech CSE(AI/ML)"
#age = "19"

# x = input("Enter your Student_ID: ")
# # print(f"My name is {name} and I am {age} years old and doing {program}")
# print("My name is {} and I am {} years old and doing {} ".format(name, age, program))
"---------------------------------------------------------------------------------------------"
# if
# age = int(input("Enter your age: "))
# if age>=18:
#    print("You are eligible for vote")
# else:
#    print("Not eligible")
"---------------------------------------------------------------------------------------------"
" if ELif ELSE"

# mark = int(input("Enter your marks: "))

# if mark>=90:
#     print("\nGRADE: A ")
# elif mark>=80: 
#     print("\nGRADE: B")
# elif mark>=70: 
#     print("\nGRADE: C")
# elif mark>=45: 
#     print("\nGRADE: D")
# else:
#     print("FAIL")

" NESTED if"

# age = int(input("\nEnter your age: "))
# license = input("\nDo you have license  (yes/no): ")

# if age>= 18:
#     if license == "\nyes":
#       print("\nYou can Drive")
#     else:
#       print("\nYou need a Driving licese to drive")
# else:
#     print("\nYou are too young to drive")

"Q1 -check  Positive and neg"

# n = int(input("\nEnter a number: "))

# if n >= 0 :
#     print("\nPOSITIVE INTIGER ")
# else:
#     print("NEGATIVE INTIGER")

"Q2" 'Even odd'

# if n%2 == 0:
#     print(f"\n {n}Is EVEN")
# else:
#     print(f"\n {n} Is ODD")

"Q3 Voting ELigibility "

# age = int(input("\n Enter your age: "))
# voter_id = input("\n DO you have voter_id ? (yes/no) ")

# if age >= 18:
#     if voter_id == "yes":
#         print("\n YOU ARE ELIGIBLE TO VOTE.")
#     else:
#         print("\n YOU NEED A VOTER ID.")
# else:

#     print("\n TOO YOUNG TO VOTE ")    

"Q4 Pass Fail" '[For a single student]'

# student_info = {
#     "id": 101,
#     "name": 'Amrit',
#     "marks":{
#         "MTH":85,
#         "PHY":66,
#         "CHEM":88,
#         "ENG":98,
#         "GEO":48,
#         "GAMES":50,
#         "HIST":22,
#         "ARTS":21
#     }
# }

# # Calculations

# total_marks = 600

# secured = sum(student_info["marks"].values())

# percentage = (secured/total_marks)*100

# #Grade 
# if percentage >= 90:
#     GRADE = "A"
# elif percentage >= 80:
#     GRADE = "B"
# elif percentage >= 70:
#     GRADE = "C"
# elif percentage >= 60:
#     GRADE = "D"
# elif percentage >= 50:
#     GRADE = "E"
# elif percentage > 45:
#     GRADE = "F"
# else:
#     GRADE = "FAIL"

# result = 'Pass' if percentage >= 45 else 'Fail'


# print("Name: ",student_info["name"])
# print("Total Percentage: ", round(percentage, 2))
# print("Total_Secured: ",secured)
# print("GRADE: ", GRADE)
# print("RESULT: ", result)



"LEAP YEAR"

# y = int(input("\nEnter the year: "))

# if y%4 == 0 :
#     print(f"{y} is Leap year")
# elif y%400 == 0 : 
#     print(f"{y} is Leap year")
# elif y % 100 == 0 :
#     print(f"{y} is not a Leap year")
# else:
#     print(f"{y} is not a Leap year")

# Q1

attendance = float(input("Enter your attendace : "))

fee_paid = input("Have you pay the acedamic fee ? (yes/no)").strip().lower() == "yes"

if  attendance < 0  or  attendance >= 75 and fee_paid:
    print("\nStudent can give the examination")
else:
    print("\nNOT ALLOWED")