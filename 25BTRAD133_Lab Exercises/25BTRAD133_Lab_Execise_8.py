# USN: 25BTRAD133
# Lab Exercise 8: Contact Book Using Lists and Dictionaries
# Description: Develop a Python program to add, search, update, delete, and display contact details.

def contact_book():
    contacts = {}
    
    while True:
        print("\n" + "=" * 35)
        print("       CONTACT BOOK SYSTEM       ")
        print("=" * 35)
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contacts[name] = {"phone": phone, "email": email}
            print(f"Success: Contact '{name}' added successfully!")
            
        elif choice == '2':
            name = input("Enter name to search: ")
            # Using dictionary get() method to handle missing keys gracefully[cite: 13]
            contact = contacts.get(name)
            if contact:
                print(f"\n[Found] Name: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
            else:
                print(f"Error: Contact '{name}' not found in the contact book.")
                
        elif choice == '3':
            name = input("Enter name of contact to update: ")
            if name in contacts:
                phone = input("Enter new phone number: ")
                email = input("Enter new email address: ")
                contacts[name] = {"phone": phone, "email": email}
                print(f"Success: Contact '{name}' updated successfully!")
            else:
                print(f"Error: Contact '{name}' does not exist.")
                
        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Success: Contact '{name}' deleted successfully!")
            else:
                print(f"Error: Contact '{name}' not found.")
                
        elif choice == '5':
            if contacts:
                print("\n" + "-" * 40)
                print(f"{'Name':<15} {'Phone':<12} {'Email':<15}")
                print("-" * 40)
                for name, details in contacts.items():
                    print(f"{name:<15} {details['phone']:<12} {details['email']:<15}")
                print("-" * 40)
            else:
                print("Contact book is currently empty.")
                
        elif choice == '6':
            print("Exiting Contact Book Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 6.")

if __name__ == "__main__":
    contact_book()