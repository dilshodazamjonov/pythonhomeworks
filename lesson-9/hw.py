import csv
import json
import os

# #### Task 1: Create a Library Management System with Custom Exceptions
# 1. Create a Python program to manage a small library system. 
# 2. Define custom exceptions for specific scenarios:
#    - **`BookNotFoundException`**: Raised when trying to borrow a book that doesn’t exist in the library.
#    - **`BookAlreadyBorrowedException`**: Raised when a book is already borrowed.
#    - **`MemberLimitExceededException`**: Raised when a member tries to borrow more books than allowed.
# 3. Implement classes for:
#    - **`Book`**: Attributes include `title`, `author`, and `is_borrowed`.
#    - **`Member`**: Attributes include `name`, `borrowed_books` (limit to 3 books per member).
#    - **`Library`**: Manages books and members, including borrowing and returning books.
# 4. Test your program with the following scenarios:
#    - Adding books and members.
#    - Borrowing and returning books.
#    - Handling exceptions when rules are violated.

class BookAlreadyBorrowedException(Exception):
    """Raised when a book is already borrowed."""
    pass

class BookNotFoundException(Exception):
    """Raised when a requested book is not found in the library."""
    pass

class MemberLimitExceededException(Exception):
    """Raised when a member tries to borrow more than 3 books."""
    pass

class MemberNotFoundException(Exception):
    """Raised when a requested member is not found in the library."""
    pass


class Book:
    """Represents a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    """Represents a library member."""
    BORROW_LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book: Book):
        """Borrow a book if limit not exceeded."""
        if len(self.borrowed_books) >= self.BORROW_LIMIT:
            raise MemberLimitExceededException(
                f"{self.name} has reached the borrowing limit ({self.BORROW_LIMIT} books)."
            )
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        """Return a borrowed book."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:
    """Represents a library system with members and books."""
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        """Add a new book to the library."""
        self.books.append(Book(title, author))

    def add_member(self, name):
        """Register a new member."""
        self.members.append(Member(name))

    def find_book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in library.")

    def find_member(self, name):
        """Find a member by name."""
        for member in self.members:
            if member.name == name:
                return member
        raise MemberNotFoundException(f"Member '{name}' not found in library.")

    def borrow_book(self, title, member_name):
        """Allow a member to borrow a book if available."""
        book = self.find_book(title)
        member = self.find_member(member_name)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{title}' is already borrowed.")
        member.borrow(book)
        book.is_borrowed = True
        print(f"{member_name} borrowed '{title}'.")

    def return_book(self, title, member_name):
        """Allow a member to return a book."""
        book = self.find_book(title)
        member = self.find_member(member_name)
        member.return_book(book)
        book.is_borrowed = False
        print(f"{member_name} returned '{title}'.")


# --- Testing ---
if __name__ == "__main__":
    library = Library()
    library.add_book("1984", "George Orwell")
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.add_book("Dune", "Frank Herbert")
    library.add_book("Book 4", "Author 4")
    library.add_member("Alice")
    library.add_member("Bob")

    # Borrowing books
    library.borrow_book("1984", "Alice")
    try:
        library.borrow_book("1984", "Bob")
    except Exception as e:
        print(e)

    library.borrow_book("The Hobbit", "Alice")
    library.borrow_book("Dune", "Alice")
    try:
        library.borrow_book("Book 4", "Alice")
    except Exception as e:
        print(e)

    # Returning a book
    library.return_book("1984", "Alice")

        

# ---

# #### Task 2: Student Grades Management
# 1. Create a CSV file named `grades.csv` with the following structure:
   
# csv
#    Name,Subject,Grade
#    Alice,Math,85
#    Bob,Science,78
#    Carol,Math,92
#    Dave,History,74
   

# 2. Write a Python program to:
#    - Read data from `grades.csv` and store it in an appropriate data structure (e.g., a list of dictionaries).
#    - Calculate the average grade for each subject.
#    - Write a new CSV file named `average_grades.csv` with the following structure:
     
# csv
#      Subject,Average Grade
#      Math,88.5
#      Science,78
#      History,74
     

# 3. Use the `csv` module for reading and writing the CSV files.


try:
    with open('grades.csv', newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
except FileNotFoundError:
    print("Error: grades.csv file not found.")
    data = []

# Step 2: Calculate averages
grade_average = {}

for d in data:
    subject = d['subject']
    try:
        grade = int(d['grade'])
    except ValueError:
        print(f"Invalid grade value for subject {subject}: {d['grade']}")
        continue

    if subject not in grade_average:
        grade_average[subject] = {'sum': 0, 'count': 0}

    grade_average[subject]['sum'] += grade
    grade_average[subject]['count'] += 1

averages = {
    subject: (info['sum'] / info['count'])
    for subject, info in grade_average.items()
    if info['count'] > 0
}

# Step 3: Write to average_grades.csv
with open('average_grades.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Subject", "Average Grade"])
    for sub, avg in averages.items():
        writer.writerow([sub, round(avg, 2)])  # Rounded for neatness

# ---

# ### **Task 3: JSON Handling**

# #### **Load and Save Tasks (JSON)**
# 1. Create a JSON file named `tasks.json` with the following structure:
   
# json
#    [
#        {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
#        {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
#        {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
#    ]
   
# 2. Write a Python program to:
#    - Load the tasks from `tasks.json`.
#    - Display all tasks with the following fields: ID, Task Name, Completed Status, Priority.
#    - Save any changes back to the `tasks.json` file (e.g., after modifying a task).

# #### **Calculate Task Completion Stats**
# 1. Write a Python function to calculate the following statistics:
#    - **Total tasks**: Count the total number of tasks.
#    - **Completed tasks**: Count the number of completed tasks.
#    - **Pending tasks**: Count the number of tasks that are not completed.
#    - **Average priority**: Calculate the average priority level of all tasks.
   
#    Display these statistics after loading the tasks.

# #### **Convert JSON Data to CSV**
# 1. Write a function to convert the task data in `tasks.json` to a CSV file named `tasks.csv`. The CSV should have the following columns:
#    - ID
#    - Task Name
#    - Completed Status
#    - Priority

#    For example:
   
# csv
#    ID,Task,Completed,Priority
#    1,Do laundry,False,3
#    2,Buy groceries,True,2
#    3,Finish homework,False,1
   

TASKS_JSON = "data.json"
TASKS_CSV = "tasks.csv"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_JSON):
        print("No tasks file found. Starting with an empty task list.")
        return []
    with open(TASKS_JSON, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks back to the JSON file."""
    with open(TASKS_JSON, "w") as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    """Print all tasks in a formatted way."""
    print("\nTasks:")
    for t in tasks:
        print(f"ID: {t['id']}, Task: {t['task']}, Completed: {t['completed']}, Priority: {t['priority']}")

def calculate_stats(tasks):
    """Print total, completed, pending tasks and average priority."""
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    avg_priority = sum(t['priority'] for t in tasks) / total if total else 0
    print("\nStatistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority:.2f}")

def update_task(tasks, task_id, completed=None, new_priority=None):
    """Update a task's completion status or priority."""
    for t in tasks:
        if t['id'] == task_id:
            if completed is not None:
                t['completed'] = completed
            if new_priority is not None:
                t['priority'] = new_priority
            save_tasks(tasks)
            print(f"\nTask {task_id} updated and saved.")
            return
    print(f"Task with ID {task_id} not found.")

def add_task(tasks, task_name, priority):
    """Add a new task."""
    new_id = max([t['id'] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "task": task_name, "completed": False, "priority": priority})
    save_tasks(tasks)
    print(f"\nTask '{task_name}' added with ID {new_id}.")

def delete_task(tasks, task_id):
    """Delete a task by ID."""
    for t in tasks:
        if t['id'] == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(f"\nTask {task_id} deleted.")
            return
    print(f"Task with ID {task_id} not found.")

def tasks_to_csv(tasks):
    """Export tasks to CSV."""
    with open(TASKS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Task", "Completed", "Priority"])
        writer.writeheader()
        for t in tasks:
            writer.writerow({
                "ID": t['id'],
                "Task": t['task'],
                "Completed": t['completed'],
                "Priority": t['priority']
            })
    print(f"\nTasks exported to {TASKS_CSV}.")

# --- Main Program ---
if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)

    add_task(tasks, "Write Python report", 2)
    update_task(tasks, task_id=1, completed=True)
    delete_task(tasks, task_id=2)

    display_tasks(tasks)
    tasks_to_csv(tasks)