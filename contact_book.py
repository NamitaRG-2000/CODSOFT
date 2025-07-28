contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contacts():
    if contacts:
        print("=== Contact List ===")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"No contact found with name '{name}'.")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '4':
        print("Exiting Contact Book. Bye!")
        break
    else:
        print("Invalid choice. Please try again.")
