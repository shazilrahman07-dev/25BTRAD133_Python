# Simple Calculator Program using Arithmetic Operators

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Calculator Results ---")
print(f"Addition ({num1} + {num2})      = {num1 + num2}")
print(f"Subtraction ({num1} - {num2})   = {num1 - num2}")
print(f"Multiplication ({num1} * {num2}) = {num1 * num2}")

if num2 != 0:
    print(f"Division ({num1} / {num2})     = {num1 / num2:.2f}")
    print(f"Floor Division ({num1} // {num2}) = {num1 // num2}")
    print(f"Modulus ({num1} % {num2})      = {num1 % num2}")
else:
    print("Division by zero is not allowed.")

import math

# 1. Area of a Circle
radius = float(input("Enter radius of the circle: "))
area_circle = math.pi * (radius ** 2)
print(f"Area of Circle: {area_circle:.2f}")

# 2. Area of a Rectangle
length = float(input("\nEnter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_rectangle = length * width
print(f"Area of Rectangle: {area_rectangle:.2f}")

# 3. Area of a Triangle
base = float(input("\nEnter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area_triangle = 0.5 * base * height
print(f"Area of Triangle: {area_triangle:.2f}")