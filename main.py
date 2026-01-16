from contact import addContact, searchContact, deleteContact, getAllContacts

def main():
    while True:
        choice = input(
            "\n1 Add\n2 Search\n3 Show All\n4 Delete\n5 Exit\nChoose: "
        )

        if choice == "1":
            addContact()
        elif choice == "2":
            searchContact()
        elif choice == "3":
            getAllContacts()
        elif choice == "4":
            deleteContact()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
