# Name: Shazil Abdul Rahman AIDE-B
# USN: 25BTRAD133
# Mini Project: Supermarket Bill Generator

print("=" * 45)
print("         SUPERMARKET BILL GENERATOR         ")
print("=" * 45)

# Input Customer Information
customer_name = input("Enter Customer Name: ")

# Input Item 1 Details
print("\n--- Item 1 ---")
item1_name = input("Enter name of Item 1: ")
item1_price = float(input("Enter price per unit: "))
item1_qty = int(input("Enter quantity: "))
item1_total = item1_price * item1_qty

# Input Item 2 Details
print("\n--- Item 2 ---")
item2_name = input("Enter name of Item 2: ")
item2_price = float(input("Enter price per unit: "))
item2_qty = int(input("Enter quantity: "))
item2_total = item2_price * item2_qty

# Input Item 3 Details
print("\n--- Item 3 ---")
item3_name = input("Enter name of Item 3: ")
item3_price = float(input("Enter price per unit: "))
item3_qty = int(input("Enter quantity: "))
item3_total = item3_price * item3_qty

# Calculate Total Amount
grand_total = item1_total + item2_total + item3_total

# Print Bill / Invoice
print("\n\n" + "=" * 45)
print("                      INVOICE               ")
print("=" * 45)
print(f"Customer Name: {customer_name}")
print("-" * 45)
print(f"{'Item Name':<15} {'Qty':<8} {'Price':<10} {'Total':<10}")
print("-" * 45)
print(f"{item1_name:<15} {item1_qty:<8} {item1_price:<10.2f} {item1_total:<10.2f}")
print(f"{item2_name:<15} {item2_qty:<8} {item2_price:<10.2f} {item2_total:<10.2f}")
print(f"{item3_name:<15} {item3_qty:<8} {item3_price:<10.2f} {item3_total:<10.2f}")
print("-" * 45)
print(f"Total Amount Payable: {grand_total:.2f}")
print("=" * 45)
print("Thank you for shopping!")
print("=" * 45)
