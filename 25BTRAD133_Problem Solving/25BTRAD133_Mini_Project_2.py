
# Student Grading Automation System

# Function to calculate grade
def calculate_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F (Fail)"


# Function to process student details
def process_student_data():

    print("=" * 45)
    print("       STUDENT GRADING AUTOMATION SYSTEM")
    print("=" * 45)

    # Get student details
    student_name = input("Enter Student Name: ")
    student_usn = input("Enter Student USN: ")

    # Get number of subjects
    while True:
        num_subjects = int(input("Enter number of subjects: "))

        if num_subjects > 0:
            break
        else:
            print("Please enter at least one subject!")

    total_marks = 0

    print("\n--- ENTER SUBJECT MARKS ---")

    # Collect marks for each subject
    for i in range(1, num_subjects + 1):

        while True:

            marks = float(input(f"Enter marks for Subject {i} (0-100): "))

            if 0 <= marks <= 100:
                total_marks += marks
                break

            else:
                print("Invalid marks! Enter a value between 0 and 100.")

    # Calculate average
    average = total_marks / num_subjects

    # Calculate overall grade
    overall_grade = calculate_grade(average)

    # Display report card
    print("\n")
    print("=" * 45)
    print("              OFFICIAL REPORT CARD")
    print("=" * 45)

    print("Student Name   :", student_name)
    print("Student USN    :", student_usn)
    print("Total Subjects :", num_subjects)
    print("Total Marks    :", f"{total_marks:.2f}",
          "/", num_subjects * 100)
    print("Average Score  :", f"{average:.2f}%")
    print("Final Grade    :", overall_grade)

    print("=" * 45)

    # Display final result
    if average >= 50:
        print("Result         : PASS")
    else:
        print("Result         : FAIL")

    print("=" * 45)
    print("       THANK YOU FOR USING THE SYSTEM!")
    print("=" * 45)


# Main program
if __name__ == "__main__":
    process_student_data()
