contacts = []

def addContact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added")

def deleteContact():
    name = input("Enter Name: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted")
            return
    print("Contact not found")

def getAllContacts():
    if not contacts:
        print("No contacts found")
    else:
        for contact in contacts:
            print(contact)

def searchContact():
    userchoice = input("Search by Name or Phone Number (N/P): ").upper()

    if userchoice == "N":
        name = input("Enter Name: ")
        for contact in contacts:
            if contact["name"] == name:
                print("Contact found:", contact)
                return
        print("Contact not found")

    elif userchoice == "P":
        phone = input("Enter Phone Number: ")
        for contact in contacts:
            if contact["phone"] == phone:
                print("Contact found:", contact)
                return
        print("Contact not found")
