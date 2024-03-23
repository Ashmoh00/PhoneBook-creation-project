def save_contact(contacts, name, number):
    contacts[name] = number
    print("Contact saved successfully.")

def retrieve_contact(contacts, name):
    if name in contacts:
        print(f"Number for {name}: {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    contacts = {}

    while True:
        print("\n1. Save Contact")
        print("2. Retrieve Contact")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            save_contact(contacts, name, number)
        elif choice == "2":
            name = input("Enter name to retrieve number: ")
            retrieve_contact(contacts, name)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
