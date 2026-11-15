# USN: 25BTRAD133
# Lab Exercise 9: Student Grading System
# Description: Store student names and marks using dictionaries, calculate grades using conditional statements[cite: 12].

def student_grading_system():
    students = {}
    
    print("=" * 45)
    print("        STUDENT GRADING SYSTEM       ")
    print("=" * 45)
    
    try:
        n = int(input("Enter the number of students to record: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter student name: ")
        
        while True:
            try:
                marks = float(input(f"Enter marks for {name} (0-100): "))
                if 0 <= marks <= 100:
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number for marks.")
        
        # Calculate grade using conditional statements[cite: 12]
        if marks >= 90:
            grade = 'A+'
        elif marks >= 80:
            grade = 'A'
        elif marks >= 70:
            grade = 'B'
        elif marks >= 60:
            grade = 'C'
        elif marks >= 50:
            grade = 'D'
        else:
            grade = 'F'
            
        # Store in dictionary
        students[name] = {"marks": marks, "grade": grade}

    # Display results summary
    print("\n\n" + "=" * 45)
    print("               FINAL GRADE REPORT           ")
    print("=" * 45)
    print(f"{'Student Name':<18} {'Marks':<12} {'Grade':<10}")
    print("-" * 45)
    
    for name, data in students.items():
        print(f"{name:<18} {data['marks']:<12.2f} {data['grade']:<10}")
        
    print("=" * 45)

if __name__ == "__main__":
    student_grading_system()