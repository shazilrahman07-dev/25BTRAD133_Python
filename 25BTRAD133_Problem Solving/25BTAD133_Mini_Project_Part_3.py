
# ATTENDANCE TRACKER

students = []
attendance = {}


# Function to add a student
def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
    else:
        students.append(name)
        attendance[name] = []
        print("Student added successfully!")


# Function to record attendance
def mark_attendance():
    if len(students) == 0:
        print("No students available. Add students first.")
        return

    print("\n--- MARK ATTENDANCE ---")

    for name in students:
        while True:
            status = input("Is " + name + " present? (P/A): ").upper()

            if status == "P" or status == "A":
                attendance[name].append(status)
                break
            else:
                print("Invalid input! Enter P or A.")

    print("Attendance recorded successfully!")


# Function to update attendance
def update_attendance():
    name = input("Enter student name: ")

    if name not in students:
        print("Student not found!")
        return

    if len(attendance[name]) == 0:
        print("No attendance records available!")
        return

    session = int(input("Enter session number to update: "))

    if session < 1 or session > len(attendance[name]):
        print("Invalid session number!")
    else:
        status = input("Enter new status (P/A): ").upper()

        if status == "P" or status == "A":
            attendance[name][session - 1] = status
            print("Attendance updated successfully!")
        else:
            print("Invalid status!")


# Function to calculate attendance percentage
def calculate_percentage(name):
    total_classes = len(attendance[name])

    if total_classes == 0:
        return 0

    present_classes = attendance[name].count("P")

    percentage = (present_classes / total_classes) * 100

    return percentage


# Function to display attendance
def display_attendance():
    if len(students) == 0:
        print("No student records available!")
        return

    print("\n========== ATTENDANCE REPORT ==========")

    for name in students:
        total = len(attendance[name])
        present = attendance[name].count("P")
        absent = attendance[name].count("A")
        percentage = calculate_percentage(name)

        print("\nStudent Name:", name)
        print("Attendance:", attendance[name])
        print("Present:", present)
        print("Absent:", absent)
        print("Total Classes:", total)
        print("Attendance Percentage:", round(percentage, 2), "%")


# Function to identify students below the threshold
def check_shortage():
    threshold = float(input("Enter attendance threshold percentage: "))

    print("\n--- STUDENTS BELOW ATTENDANCE THRESHOLD ---")

    found = False

    for name in students:
        percentage = calculate_percentage(name)

        if percentage < threshold:
            print(name, "-", round(percentage, 2), "%")
            found = True

    if found == False:
        print("No students are below the threshold.")


# Main menu
while True:
    print("\n========== ATTENDANCE TRACKER ==========")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Update Attendance")
    print("4. Display Attendance")
    print("5. Check Attendance Shortage")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        update_attendance()

    elif choice == "4":
        display_attendance()

    elif choice == "5":
        check_shortage()

    elif choice == "6":
        print("Thank you for using Attendance Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
