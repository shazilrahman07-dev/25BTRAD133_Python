name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
height = float(input("Enter Height (in meters): "))

# 2. Arithmetic Operators
age_in_5_years = age + 5
squared_age = age ** 2

# 3. Relational / Logical Operators
is_adult = age >= 18

# 4. Output Display using f-strings
print("\n" + "=" * 30)
print("        STUDENT PROFILE REPORT        ")
print("=" * 30)
print(f"Name                : {name}")
print(f"Current Age         : {age} years")
print(f"Height              : {height:.2f} m")
print(f"Age in 5 Years      : {age_in_5_years}")
print(f"Age Squared         : {squared_age}")
print(f"Eligible Adult      : {is_adult}")
print("=" * 30)