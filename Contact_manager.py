contacts =[]

while True:
    print("\nContact Manager")
    print("1.Add Contact")
    print("2.show Contacts")
    print("3.search Contact")
    print("4.delete Contact")
    print("5.exit")
    choice = input("Enter your choice: ")

    if choice =='1':
        name = input("enter name:")
        phone = input("enter phone:")

        contact = {'name': name, 'phone': phone}
        contacts.append(contact)         

        print("contact added successfully")
    elif choice =='2':
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    elif choice =='3':
        search_name = input("Enter name to search: ")
        found_contacts = [contact for contact in contacts if contact['name'] == search_name]
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        else:
            print("Contact not found.") 
    elif choice =='4':
        delete_name = input("Enter name to delete: ")
        contacts = [contact for contact in contacts if contact['name'] != delete_name]
        print("Contact deleted successfully.")
    elif choice =='5':
        print("Exiting Contact Manager. Goodbye!")
        break   
    else:
        print("Invalid choice. Please try again.")                            
