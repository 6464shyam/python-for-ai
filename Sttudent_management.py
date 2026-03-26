Students = []

while True:
    print("\nstudent management system")
    print("1.Add student")
    print("2.View students")
    print("3.search student")
    print("4.delete student")
    print("5.exit")

    choice = input("enter your choice: ")
    if choice == "1":
        name = input("enter student name: ")
        Students.append(name) 
        print("student added successfully")
    elif choice == "2":
        if len(Students) == 0:
            print("No students found.")
        else:
            for student in Students:
                print(f"Name: {student}")
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found_students = [student for student in Students if student == search_name]
        if found_students:
            for student in found_students:
                print(f"Name: {student}")
        else:
            print("Student not found.")     

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        Students = [student for student in Students if student != delete_name]
        print("Student deleted successfully.")
    elif choice == "5":
        print("Exiting student management system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
