# Student Management System

## Description
This project is a simple Student Management System developed in Python. It allows users to manage student information through a console-based interface.

The system supports basic operations such as adding, viewing, searching, updating, and deleting students. All data is stored in memory using Python data structures.

## Features
- Add new students  
- View all students  
- Search for a student by name  
- Update student information  
- Delete a student  
- Input validation (text, numbers, and state)  
- Prevent duplicate student IDs  
- Error handling for empty lists  

## Data Structure
The system uses a list of dictionaries to store student data.

Each student contains the following fields:

{
    "Id": int,
    "name": str,
    "age": int,
    "program": str,
    "state": str
}

## How to Run
1. Make sure Python is installed on your system.
2. Save the program file as "student_system.py".
3. Open Visual Studio Code
4. Run the program.


## Example Usage
MENU
1. Add new student
2. View the Students list
3. Search for a student
4. Update a student's information
5. Delete student
6. Exit

Example flow:
- The user selects option 1
- The user enters student data (ID, name, age, program, state)
- The student is stored in the system

## Validations Implemented
- Only letters are allowed for text fields  
- Only positive numbers are allowed for numeric fields  
- State must be "active" or "inactive"  
- Duplicate student IDs are not allowed  
- The program handles empty lists without crashing  

## Code Structure
The program is organized using functions:
- menu(): Displays the menu options  
- add_new_student(): Adds a new student  
- view_students(): Displays all students  
- search_student(): Searches for a student  
- update_student(): Updates student information  
- delete_student(): Deletes a student  
- Validation functions for input control  

## Possible Improvements
- Add file persistence using .txt, .csv, or .json  
- Allow search by ID  
- Add additional fields such as email  
- Create a graphical user interface  

## Author
JHONATAN SANCHEZ
