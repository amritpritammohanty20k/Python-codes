all_students = {}  # outer dictionary to hold all students

n = int(input("How many students do you want to enter? "))

for i in range(n):
    print(f"\n--- Enter details for Student {i+1} ---")
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")

    marks = {
        "MTH": int(input("Enter Math marks (out of 100): ")),
        "PHY": int(input("Enter Physics marks (out of 100): ")),
        "CHEM": int(input("Enter Chemistry marks (out of 100): ")),
        "ENG": int(input("Enter English marks (out of 100): ")),
        "GEO": int(input("Enter Geography marks (out of 50): ")),
        "GAMES": int(input("Enter Games marks (out of 50): ")),
        "HIST": int(input("Enter History marks (out of 50): ")),
        "ARTS": int(input("Enter Arts marks (out of 50): "))
    }

    student_info = {
        "name": name,
        "marks": marks
    }

    all_students[student_id] = student_info

print("\nAll students entered successfully!\n")

# ---- Lookup section (now repeats) ----
while True:
    search_id = int(input("\nEnter Student ID to view result: "))

    if search_id in all_students:
        student = all_students[search_id]
        scored = sum(student["marks"].values())
        total_marks = 600
        percentage = (scored / total_marks) * 100

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        elif percentage >= 50:
            grade = "E"
        elif percentage >= 45:
            grade = "F"
        else:
            grade = "Fail"

        result = "Pass" if percentage >= 45 else "Fail"

        print("\nName:", student["name"])
        print("Marks:")
        for subject, mark in student["marks"].items():
            print(f"  {subject}: {mark}")
        print("Total Scored:", scored)
        print("Percentage:", round(percentage, 2))
        print("Grade:", grade)
        print("Result:", result)
    else:
        print("Student ID not found.")

    choice = input("\nDo you want to search another student? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Exiting program. Goodbye!")
        break