student_dict = {}

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student_dict[name] = marks
    print("Student added successfully!\n")

def update_marks():
    name = input("Enter student name to update: ")
    if name in student_dict:
        marks = int(input("Enter new marks: "))
        student_dict[name] = marks
        print("Marks updated successfully!\n")
    else:
        print("Student not found!\n")

def search_student():
    name = input("Enter student name to search: ")
    if name in student_dict:
        print(f"{name}'s marks: {student_dict[name]}\n")
    else:
        print("Student not found!\n")

def display_student():
    if not student_dict:
        print("No students available!\n")
    else:
        print("---- Student List ----")
        for name, marks in student_dict.items():
            print(f"{name} : {marks}")
        print()

# Main loop
while True:
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    ch = input("Enter your choice: ").upper()

    if ch == 'A':
        add_student()
    elif ch == 'B':
        update_marks()
    elif ch == 'C':
        search_student()
    elif ch == 'D':
        display_student()
    elif ch == 'E':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.\n")