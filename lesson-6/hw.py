import os
import string
from collections import Counter

# ### Zero Check Decorator

# Write a decorator function called `check` that verifies that the denominator is not equal to 0 and apply it to the following function:

# python
# @check
# def div(a, b):
#    return a / b



# input: div(6, 2)
# output: 3



# input: div(6, 0)
# output: "Denominator can't be zero"

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper
@check
def div(a, b):
    return a / b

print(div(6, 2))  # Output: 3.0
print(div(6, 0)) 

# ---

# ### **Employee Records Manager**
# **Objective**: Create a program to manage employee records using file handling.  

# **Tasks**:  
# 1. **File Creation and Data Entry**  
#    - Create a file named **"employees.txt"**.  
#    - Allow the user to add new employee records. Each record should have the following fields:  
     
#      Employee ID, Name, Position, Salary
     
#      Example of a record:  
     
#      1001, John Doe, Software Engineer, 75000
     

# 2. **Menu Options**  
#    Your program should present the following options:  
   
#    1. Add new employee record
#    2. View all employee records
#    3. Search for an employee by Employee ID
#    4. Update an employee's information
#    5. Delete an employee record
#    6. Exit



FILE_NAME = "employees.txt"

def add_employee():
    with open(FILE_NAME, "a", encoding='utf-8') as f:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        f.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully.\n")

def view_employees():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.\n")
        return
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        print("\nEmployee Records:")
        for line in f:
            print(line.strip())
        print()

def search_employee():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.\n")
        return
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print("Employee Found:", line.strip())
                found = True
                break
    if not found:
        print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    lines = []
    found = False
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        lines = f.readlines()
    with open(FILE_NAME, "w", encoding='utf-8') as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                print("Current:", line.strip())
                name = input("New Name: ")
                position = input("New Position: ")
                salary = input("New Salary: ")
                f.write(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                f.write(line)
    if found:
        print("Employee updated.\n")
    else:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    lines = []
    found = False
    with open(FILE_NAME, "r", encoding='utf-8') as f:
        lines = f.readlines()
    with open(FILE_NAME, "w", encoding='utf-8') as f:
        for line in lines:
            if not line.startswith(emp_id + ","):
                f.write(line)
            else:
                found = True
    if found:
        print("Employee deleted.\n")
    else:
        print("Employee not found.\n")

def menu():
    while True:
        print("1 for - Add new employee record")
        print("2 for - View all employee records")
        print("3 for - Search for an employee by ID")
        print("4 for - Update employee information")
        print("5 for - Delete an employee record")
        print("6 for - Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid choice.\n")

# Run the menu
menu()
   

# 3. **Functional Requirements**  
#    - **Option 1**: Append a new employee record to **"employees.txt"**.  
#    - **Option 2**: Display all employee records from **"employees.txt"**.  
#    - **Option 3**: Allow the user to search for an employee by **Employee ID** and display their details.  
#    - **Option 4**: Update an employee’s information (name, position, or salary) based on the Employee ID.  
#    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
#    - **Option 6**: Exit the program. 

# ---

# ### **Word Frequency Counter**
# **Objective**: Analyze a text file and count how often each word appears.  

# **Tasks**:  
# 1. **File Input**  
#    - Use the file **"sample.txt"**. The file can contain any text (like a paragraph or an article).  
#    - If **"sample.txt"** does not exist, prompt the user to create it by typing in a paragraph.  

# 2. **Count Word Frequency**  
#    - Read the file content and split it into individual words.  
#    - Count the frequency of each word (ignore capitalization, e.g., "The" and "the" should be counted as the same word).  
#    - Ignore punctuation (like commas, periods, etc.).  

# 3. **Output**  
#    - Display the total number of words in the file.  
#    - Display the top 5 most common words with their counts.  
#    - Save the output to a new file called **"word_count_report.txt"**.  

# 4. **Example Output**  
#    **Content of sample.txt**:  
   
#    This is a simple file.
#    This file, is for testing purposes. It is a test file.
   

#    **Console Output**:  
   
#    Total words: 14
#    Top 5 most common words:
#    is - 3 times
#    this - 2 times
#    file - 3 times
#    a - 2 times
#    test - 1 time
   

#    **Content of word_count_report.txt**:  
   
#    Word Count Report
#    Total Words: 14
#    Top 5 Words:
#    is - 3
#    file - 3
#    this - 2
#    a - 2
#    test - 1

def create_sample_file():
    print("sample.txt not found. Please enter text to create it:")
    text = input("Enter paragraph:\n")
    with open("sample.txt", "w", encoding='utf-8') as f:
        f.write(text)

def clean_text(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower().split()

def word_frequency_counter(top_n=5):
    if not os.path.exists("sample.txt"):
        create_sample_file()

    with open("sample.txt", "r") as f:
        words = clean_text(f.read())

    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    most_common = word_counts.most_common(top_n)

    print(f"\nTotal words: {total_words}")
    print("Top", top_n, "most common words:")
    for word, count in most_common:
        print(f"{word} - {count} time{'s' if count > 1 else ''}")

    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top {} Words:\n".format(top_n))
        for word, count in most_common:
            report.write(f"{word} - {count}\n")

# Ask user how many top words to display (bonus)
try:
    top_n = int(input("How many top common words to display? "))
except ValueError:
    top_n = 5  # default if invalid input

# Run the counter
word_frequency_counter(top_n)
   

# **Bonus Task**:  
# - Allow the user to specify how many "top common words" to display (e.g., top 3, top 10, etc.).  
# - Make sure the program ignores case, punctuation, and handles large files efficiently.