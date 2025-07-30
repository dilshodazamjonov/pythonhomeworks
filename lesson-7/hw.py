import json
import csv
import os
import math

# ## Generalized `Vector` Class  

# **Objective**: Create a Python class `Vector` that represents a mathematical vector in an n-dimensional space, capable of handling any number of dimensions.

# ### **Task Description**

# 1. **Create a `Vector` class** that represents a vector in an n-dimensional space.  
#    - The class should support vectors of any number of dimensions, defined by an arbitrary number of components provided during initialization.

# 2. The class should provide functionality to:
#    - Perform vector operations such as addition, subtraction, and dot product.
#    - Handle scalar multiplication.
#    - Compute the magnitude (length) of the vector.
#    - Normalize the vector (return the unit vector).

# 3. The class should have methods for:
#    - Representing the vector as a string for easy display.
#    - Handling operations between vectors of the same dimension and raising appropriate errors when vectors of different dimensions are involved.

# ### **Example Usage**
# python
# # Create vectors
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)

# # Print the vector
# print(v1)          # Output: Vector(1, 2, 3)

# # Addition
# v3 = v1 + v2
# print(v3)          # Output: Vector(5, 7, 9)

# # Subtraction
# v4 = v2 - v1
# print(v4)          # Output: Vector(3, 3, 3)

# # Dot product
# dot_product = v1 * v2
# print(dot_product) # Output: 32

# # Scalar multiplication
# v5 = 3 * v1
# print(v5)          # Output: Vector(3, 6, 9)

# # Magnitude
# print(v1.magnitude())  # Output: 3.7416573867739413

# # Normalization
# v_unit = v1.normalize()
# print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)



class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions.")

    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[x / mag for x in self.components])


# === Example Usage ===
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)            # Output: Vector(1, 2, 3)
print(v1 + v2)       # Output: Vector(5, 7, 9)
print(v2 - v1)       # Output: Vector(3, 3, 3)
print(v1 * v2)       # Output: 32 (dot product)
print(3 * v1)        # Output: Vector(3, 6, 9)
print(v1.magnitude())# Output: 3.7416573867739413
print(v1.normalize())# Output: Vector(0.267..., 0.534..., 0.801...)



# ---

# ## Employee Records Manager (OOP Version)
# **Objective**: Create a program to manage employee records using classes and file handling.

# ### **Tasks and Requirements**

# 1. **Class Design**  
#    - Create a class `Employee` to represent individual employees with the following attributes:
#      - `employee_id`
#      - `name`
#      - `position`
#      - `salary`
#    - Create a class `EmployeeManager` to handle operations such as adding, viewing, searching, updating, and deleting employee records. This class will manage the file **"employees.txt"**.

# 2. **File Handling**  
#    - All employee records should be stored in **"employees.txt"**.  
#    - Each operation (add, view, update, delete) should interact with the file to ensure data persistence.

# 3. **Menu Options**  
#    Implement a menu within the `EmployeeManager` class with the following options:
   

#    1. Add new employee record
#    2. View all employee records
#    3. Search for an employee by Employee ID
#    4. Update an employee's information
#    5. Delete an employee record
#    6. Exit
   


# 4. **Functional Requirements**  
#    - **Option 1**: Add a new employee by creating an `Employee` object and appending it to **"employees.txt"**.  
#    - **Option 2**: Read all records from **"employees.txt"** and display them.  
#    - **Option 3**: Search for an employee by **Employee ID** and display their details.  
#    - **Option 4**: Update an employee's information (name, position, or salary) based on the Employee ID.  
#    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
#    - **Option 6**: Exit the program.


# ### **Example Usage**  
# plaintext
# Welcome to the Employee Records Manager!
# 1. Add new employee record
# 2. View all employee records
# 3. Search for an employee by Employee ID
# 4. Update an employee's information
# 5. Delete an employee record
# 6. Exit

# Enter your choice: 1
# Enter Employee ID: 1001
# Enter Name: John Doe
# Enter Position: Software Engineer
# Enter Salary: 75000
# Employee added successfully!

# Enter your choice: 2
# Employee Records:
# 1001, John Doe, Software Engineer, 75000

# Enter your choice: 3
# Enter Employee ID to search: 1001
# Employee Found:
# 1001, John Doe, Software Engineer, 75000

# Enter your choice: 6
# Goodbye!


# ### **Additional Instructions**
# 1. Use the `Employee` class to encapsulate individual employee data and functionality (e.g., a `__str__` method for displaying employee details).  
# 2. Use the `EmployeeManager` class for managing operations such as file handling, record searching, and updates.  
# 3. Ensure your code is modular, with methods for each operation (e.g., `add_employee`, `view_all_employees`).  


# ### **Bonus Challenge**
# 1. Add validation to ensure unique Employee IDs.  
# 2. Implement error handling for invalid inputs and file operations.  
# 3. Allow users to sort employee records (e.g., by salary or name) before displaying them.  

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_line(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        return Employee(parts[0], parts[1], parts[2], parts[3])


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def _load_all(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r") as f:
            return [Employee.from_line(line) for line in f if line.strip()]

    def _save_all(self, employees):
        with open(self.FILE_NAME, "w") as f:
            for emp in employees:
                f.write(emp.to_line())

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        employees = self._load_all()
        if any(emp.employee_id == emp_id for emp in employees):
            print("Error: Employee ID already exists.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        employee = Employee(emp_id, name, position, salary)
        with open(self.FILE_NAME, "a") as f:
            f.write(employee.to_line())
        print("Employee added successfully!")

    def view_all(self, sort_by=None):
        employees = self._load_all()
        if sort_by == "salary":
            employees.sort(key=lambda x: float(x.salary))
        elif sort_by == "name":
            employees.sort(key=lambda x: x.name)
        print("\nEmployee Records:")
        for emp in employees:
            print(emp)

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        employees = self._load_all()
        for emp in employees:
            if emp.employee_id == emp_id:
                print("Employee Found:\n", emp)
                return
        print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        employees = self._load_all()
        for i, emp in enumerate(employees):
            if emp.employee_id == emp_id:
                emp.name = input("New Name: ")
                emp.position = input("New Position: ")
                emp.salary = input("New Salary: ")
                employees[i] = emp
                self._save_all(employees)
                print("Employee updated.")
                return
        print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        employees = self._load_all()
        new_employees = [emp for emp in employees if emp.employee_id != emp_id]
        if len(new_employees) != len(employees):
            self._save_all(new_employees)
            print("Employee deleted.")
        else:
            print("Employee not found.")

    def menu(self):
        print("Welcome to the Employee Records Manager!")
        while True:
            print("\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                sort = input("Sort by (name/salary/none): ").strip().lower()
                self.view_all(sort_by=sort if sort in ("name", "salary") else None)
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
                
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()




# ---

# ## To-Do Application

# **Objective**: Create a flexible To-Do application to manage tasks with support for different file storage formats (e.g., CSV, JSON). The application should be designed such that adding support for a new file format requires minimal changes to the code.


# ### **Task Description**

# #### 1. Functional Requirements:
# Your To-Do application should provide the following features:
# 1. **Add a task**: Allow users to add tasks with the following details:
#    - `Task ID`
#    - `Title`
#    - `Description`
#    - `Due Date` (optional)
#    - `Status` (e.g., Pending, In Progress, Completed)
# 2. **View tasks**: Display all tasks with their details.
# 3. **Update a task**: Allow users to modify a task's details using its Task ID.
# 4. **Delete a task**: Remove a task by its Task ID.
# 5. **Filter tasks**: Filter tasks by status (e.g., Pending or Completed).
# 6. **Save and load tasks**: Save tasks to a file and load them from the file on startup.

# #### 2. Design Requirements:
# 1. **Separation of Concerns**:
# 2. **Support for Multiple Formats**:
# 3. **Minimal Code Changes**:

# #### 3. Example Usage:
# plaintext
# Welcome to the To-Do Application!
# 1. Add a new task
# 2. View all tasks
# 3. Update a task
# 4. Delete a task
# 5. Filter tasks by status
# 6. Save tasks
# 7. Load tasks
# 8. Exit

# Enter your choice: 1
# Enter Task ID: 101
# Enter Title: Finish Homework
# Enter Description: Complete math and science homework.
# Enter Due Date (YYYY-MM-DD): 2024-12-31
# Enter Status (Pending/In Progress/Completed): Pending
# Task added successfully!

# Enter your choice: 2
# Tasks:
# 101, Finish Homework, Complete math and science homework., 2024-12-31, Pending



class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class StorageHandler:
    def save(self, tasks, filename): pass
    def load(self, filename): pass


class JSONStorage(StorageHandler):
    def save(self, tasks, filename):
        with open(filename, "w") as f:
            json.dump([task.to_dict() for task in tasks], f)

    def load(self, filename):
        if not os.path.exists(filename): return []
        with open(filename, "r") as f:
            data = json.load(f)
        return [Task(**item) for item in data]


class CSVStorage(StorageHandler):
    def save(self, tasks, filename):
        with open(filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, filename):
        if not os.path.exists(filename): return []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            return [Task(**row) for row in reader]


class ToDoApp:
    def __init__(self, storage_handler, filename):
        self.storage = storage_handler
        self.filename = filename
        self.tasks = self.storage.load(filename)

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("New Title: ")
                task.description = input("New Description: ")
                task.due_date = input("New Due Date: ")
                task.status = input("New Status: ")
                print("Task updated.")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        original_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        if len(self.tasks) < original_count:
            print("Task deleted.")
        else:
            print("Task not found.")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        for task in filtered:
            print(task)

    def save_tasks(self):
        self.storage.save(self.tasks, self.filename)
        print("Tasks saved.")

    def load_tasks(self):
        self.tasks = self.storage.load(self.filename)
        print("Tasks loaded.")

    def menu(self):
        while True:
            print("\n1. Add a new task\n2. View all tasks\n3. Update a task\n4. Delete a task\n5. Filter tasks by status\n6. Save tasks\n7. Load tasks\n8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1": self.add_task()
            elif choice == "2": self.view_tasks()
            elif choice == "3": self.update_task()
            elif choice == "4": self.delete_task()
            elif choice == "5": self.filter_tasks()
            elif choice == "6": self.save_tasks()
            elif choice == "7": self.load_tasks()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

# === Example Usage ===
if __name__ == "__main__":
    # Change to CSVStorage("tasks.csv") for CSV support
    storage = JSONStorage()
    app = ToDoApp(storage, "tasks.json")
    app.menu()


# ### **Deliverables**
# 1. Python scripts with classes and methods implemented as described.
# 2. Clear comments and documentation.
# 3. A brief explanation of how you ensured minimal code changes when adding support for new file formats.