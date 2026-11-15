# USN: 25BTRAD133
# Lab Exercise 12: Student Data Manager Using Files

def manage_students():
    while True:
        ch = input("\n1. Add 2. View 3. Exit\nChoice: ")
        if ch == '1':
            rec = f"{input('USN: ')},{input('Name: ')},{input('Marks: ')}\n"
            with open("students.txt", "a") as f: f.write(rec)
            print("Saved!")
        elif ch == '2':
            try:
                with open("students.txt", "r") as f:
                    print("\n--- Records ---\n" + "".join(f.readlines()).replace(",", " | "))
            except FileNotFoundError: print("No records.")
        elif ch == '3': break

if __name__ == "__main__": manage_students()