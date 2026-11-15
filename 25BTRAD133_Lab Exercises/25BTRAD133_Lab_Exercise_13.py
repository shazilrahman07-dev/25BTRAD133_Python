# USN: 25BTRAD133
# Lab Exercise 13: CSV-Based Payroll Management System

import csv

def process_payroll(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            print(f"{'Name':<12} {'Basic':<8} {'Gross Salary'}")
            print("-" * 32)
            for row in reader:
                basic = float(row['Basic'])
                hra = float(row['HRA'])
                deduction = float(row['Deduction'])
                gross = basic + hra - deduction
                print(f"{row['Name']:<12} {basic:<8.1f} {gross:<10.1f}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if __name__ == "__main__":
    process_payroll("payroll.csv")