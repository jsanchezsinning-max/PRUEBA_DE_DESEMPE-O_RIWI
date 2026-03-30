student_dictionary = [] #This is a dictionary where each student's information will be stored.

def menu(): # This function contains the main menu, indicating what options the user can use.
    option = ""
    
    # The while loop is used to validate that the user chooses an option between 1 and 6.
    while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6": 
        print("MENU")
        print("""
            1. Add new student
            2. View the Students list
            3. Search for a student
            4. Update a student's information
            5. Delete student
            6. Exit
                """)
        option = input("Choose an Option: ").strip() # The variable "option" will store the option that the user chooses.

        if option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6":
            print("Invalid option, try again.\n")
            # This "if" sends a message if the option is incorrect.
    return option

# This function is to validate that the user only enters text.
def validate_str(message):
    text = input(message).strip()

    while not text or not text.replace(" ", "").isalpha():
        print("Error: Only letters allowed.")
        text = input(message).strip()

    return text

# This function is to validate that the user only enters numbers.
def validate_int(message):
    value = input(message).strip()

    while not value.isdigit() or int(value) <= 0:
        print("Error: Enter a positive number.")
        value = input(message).strip()

    return int(value)

# When the program asks for the student's status, this function is to validate that the user can only write between 2 options, active and inactive.
def validate_state(message):
    state = input(message).strip().lower()

    while state not in ["active", "inactive"]:
        print("Error: Only 'active' or 'inactive' allowed.")
        state = input(message).strip().lower()

    return state

# This function is to notify the user that the student has already been registered.
def id_exists(student_dictionary, id_student):
    for student in student_dictionary:
        if student["Id"] == id_student:
            return True
    return False

# This function is for adding a new student, who will be stored in the "student_dictionary" dictionary.
def add_new_student(student_dictionary):
    print("\n=============== ADD A NEW STUDENT ===============")

    id_student = validate_int("Enter Student ID: ")

    while id_exists(student_dictionary, id_student): # Here we use the "id_exist" function
        print("Error: This ID already exists.")
        id_student = validate_int("Enter a different Student ID: ")

    name = validate_str("Enter the Student name: ")
    age = validate_int("Enter the Student Age: ")
    program = validate_str("What program is the student studying? ")
    state = validate_state("State (active/inactive): ")

    student = {
        "Id": id_student,
        "name": name,
        "age": age,
        "program": program,
        "state": state
    }

    student_dictionary.append(student)
    print("Student added successfully!\n")

# This function allows the user to see all students saved up to that point.
def view_students(student_dictionary):
    print("\n=============== STUDENTS LIST ===============")

    if not student_dictionary:
        print("No students registered yet.\n")
        return

    for student in student_dictionary:
        print("ID:", student["Id"],
              "| Name:", student["name"],
              "| Age:", student["age"],
              "| Program:", student["program"],
              "| State:", student["state"])
    print()

# This function allows you to search for a student by name and access all their information.
def search_student(student_dictionary):
    print("\n=============== SEARCH FOR A STUDENT ===============")

    if not student_dictionary:
        print("No students registered.\n")
        return None

    name = validate_str("Enter the Student name: ")

    for student in student_dictionary:
        if student["name"].lower() == name.lower():
            print("Student found:")
            print(student, "\n")
            return student

    print("Student not found.\n")
    return None

# This function updates the student's information if the user so desires.
def update_student(student_dictionary):
    print("\n================ UPDATE STUDENT INFORMATION ===============")

    if not student_dictionary:
        print("No students to update.\n")
        return

    student = search_student(student_dictionary)

    if student: # The function allows leaving blank spaces if the user does not wish to update that field.
        print("Leave blank if you don't want to change something.") 

        age_input = input("New age: ").strip()
        program_input = input("New program: ").strip()
        state_input = input("New state (active/inactive): ").strip().lower()

        if age_input.isdigit() and int(age_input) > 0:
            student["age"] = int(age_input)

        if program_input and program_input.replace(" ", "").isalpha():
            student["program"] = program_input

        if state_input in ["active", "inactive"]:
            student["state"] = state_input

        print("Student updated successfully!\n")

# This function removes any student from the dictionary
def delete_student(student_dictionary):
    print("\n================ DELETE STUDENT ===============")

    if not student_dictionary:
        print("No students to delete.\n")
        return

    name = validate_str("Enter the student name to delete: ")

    for student in student_dictionary:
        if student["name"].lower() == name.lower():
            student_dictionary.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


# This is the main loop; the program will run until the user decides to exit with option 6.
running = True # This variable will be true until the user decides to exit, at which point it will become false and the user will exit the program.

while running:
    option = menu() # The menu will continue to print until the program finishes.

    if option == "1":
        add_new_student(student_dictionary)

    elif option == "2":
        view_students(student_dictionary)

    elif option == "3":
        search_student(student_dictionary)

    elif option == "4":
        update_student(student_dictionary)

    elif option == "5":
        delete_student(student_dictionary)

    elif option == "6":
        print("See you soon!")
        running = False
