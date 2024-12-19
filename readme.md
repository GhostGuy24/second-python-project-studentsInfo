# Student Management System

A simple Python-based console application to manage student records. This project allows you to:

- Add students
- Find students
- Delete students
- Display all students

## Features

1. **Add Student**:
   - Collect student details such as name, age, and gender and store them in a JSON file.

2. **Find Student**:
   - Search for a student by name and display their details if found.

3. **Delete Student**:
   - Remove a student's record by name from the system.

4. **Update Student**:
   - Edit user name, age or gender with inputing the assigned id.
5. **Display Students**:
   - Show all stored student records in a formatted manner.

6. **Save and Load**:
   - All records are saved in a `students.json` file and loaded upon program start.

## Prerequisites

- Python 3.x
- Required packages listed in `requirements.txt`.

## Installation

1. Clone this repository or download the source code.

   ```bash
   git clone https://github.com/GhostGuy24/second-python-project-studentsInfo.git
   
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Execute the main script:

   ```bash
   python app.py
   ```

2. Follow the on-screen menu to perform actions.

## File Structure

```
|-- app.py                 # Main entry point of the application
|-- students_operations.py # Contains all the core functionality
|-- students.json          # JSON file where student data is stored
|-- requirements.txt       # Required Python packages
|-- README.md              # Documentation
```

## Technologies Used

- **Python**: Core programming language
- **JSON**: Data storage format
- **Colorama**: For colorful terminal output

## Example Usage

1. **Add a Student**:
   - Input the student's name, age, and gender.

2. **Find a Student**:
   - Enter the name of the student to search for their details.

3. **Delete a Student**:
   - Enter the name of the student to delete their record.

4. **Display Students**:
   - View all stored student records.

## Requirements

Ensure the following packages are installed (also listed in `requirements.txt`):

- `colorama`

## Future Enhancements

- Add the ability to update student records.
- Enhance the menu with more interactive options.
- Add validation for inputs (e.g., valid age).

## Author

- **Guy**

---

This project is a beginner-friendly Python application to practice working with files, enums, and terminal-based applications. Contributions and suggestions are welcome!
