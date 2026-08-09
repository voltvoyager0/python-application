# ==========================================
# STUDENT GRADE MANAGER
# Demonstrates:
# Input Statements
# Lists
# Conditional Statements
# Loops
# Functions
# ==========================================

students = []

# -------------------------------
# Function to calculate grade
# -------------------------------
def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


# -------------------------------
# Function to add student
# -------------------------------
def add_student():
    print("\n===== Add Student =====")

    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty!")
        return

    try:
        mark = float(input("Enter marks (0-100): "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    grade = calculate_grade(mark)

    students.append([name, mark, grade])

    print(f"{name} added successfully!")
    print("Grade:", grade)


# -------------------------------
# View students
# -------------------------------
def view_students():

    if len(students) == 0:
        print("\nNo student records found.")
        return

    print("\n========== Student Records ==========")

    print("{:<5} {:<20} {:<10} {:<10}".format("No", "Name", "Marks", "Grade"))

    for i in range(len(students)):
        print("{:<5} {:<20} {:<10} {:<10}".format(
            i + 1,
            students[i][0],
            students[i][1],
            students[i][2]
        ))


# -------------------------------
# Search student
# -------------------------------
def search_student():

    if len(students) == 0:
        print("No records available.")
        return

    search = input("Enter student name: ").lower()

    found = False

    for student in students:
        if student[0].lower() == search:
            print("\nStudent Found")
            print("Name :", student[0])
            print("Marks:", student[1])
            print("Grade:", student[2])
            found = True
            break

    if not found:
        print("Student not found.")


# -------------------------------
# Update student
# -------------------------------
def update_student():

    if len(students) == 0:
        print("No records available.")
        return

    name = input("Enter student name to update: ").lower()

    for student in students:
        if student[0].lower() == name:

            try:
                new_mark = float(input("Enter new marks: "))

                if new_mark < 0 or new_mark > 100:
                    print("Invalid marks.")
                    return

            except ValueError:
                print("Invalid number.")
                return

            student[1] = new_mark
            student[2] = calculate_grade(new_mark)

            print("Record updated successfully!")
            return

    print("Student not found.")


# -------------------------------
# Delete student
# -------------------------------
def delete_student():

    if len(students) == 0:
        print("No records available.")
        return

    name = input("Enter student name to delete: ").lower()

    for student in students:
        if student[0].lower() == name:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# -------------------------------
# Class Summary
# -------------------------------
def class_summary():

    if len(students) == 0:
        print("No records available.")
        return

    total = 0
    highest = students[0]
    lowest = students[0]

    for student in students:

        total += student[1]

        if student[1] > highest[1]:
            highest = student

        if student[1] < lowest[1]:
            lowest = student

    average = total / len(students)

    print("\n========== CLASS SUMMARY ==========")

    print("Total Students :", len(students))
    print("Average Marks  :", round(average, 2))

    print("\nTop Student")
    print(highest[0], "-", highest[1], "-", highest[2])

    print("\nLowest Student")
    print(lowest[0], "-", lowest[1], "-", lowest[2])

    # Creative Feature
    print("\nPerformance Badge")

    if average >= 85:
        print("🏆 Excellent Class!")
    elif average >= 70:
        print("⭐ Good Performance!")
    elif average >= 50:
        print("👍 Keep Improving!")
    else:
        print("📚 More Practice Needed!")


# -------------------------------
# Progress Tracker
# -------------------------------
def progress_tracker():

    if len(students) == 0:
        print("No records available.")
        return

    print("\n========== Progress Tracker ==========")

    for student in students:

        bars = int(student[1] // 5)

        print(student[0])
        print("[" + "#" * bars + "-" * (20 - bars) + "]", student[1])


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n===================================")
    print("     STUDENT GRADE MANAGER")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Summary")
    print("7. Progress Tracker")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        class_summary()

    elif choice == "7":
        progress_tracker()

    elif choice == "8":
        print("\n===================================")
        print("Thank you for using")
        print("Student Grade Manager")
        print("Have a wonderful day!")
        print("===================================")
        break

    else:
        print("Invalid menu choice! Please try again.")





        # 9810350585 viber, whatsapp
        # name, class, school, message 