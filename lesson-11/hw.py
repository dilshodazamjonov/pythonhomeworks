import sqlite3

# ### Task 1

# 1. **Database Creation**:
#    - Create a new SQLite database named `roster.db`.
#    - Define a table called **Roster** with the following schema:
#      - **Name**: TEXT
#      - **Species**: TEXT
#      - **Age**: INTEGER

database = sqlite3.connect('roster.db')
cursor = database.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster(
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

# 2. **Insert Data**:
#    - Populate the **Roster** table with the following entries:

# | Name           | Species  | Age |
# |----------------|----------|-----|
# | Benjamin Sisko | Human    | 40  |
# | Jadzia Dax     | Trill    | 300 |
# | Kira Nerys     | Bajoran  | 29  |

data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

cursor.executemany('''
    INSERT INTO Roster(Name, Species, Age)
    VALUES (?, ?, ?)
''', data)

# 3. **Update Data**:
#    - Update the `Name` of **Jadzia Dax** to **Ezri Dax**.

cursor.execute('''
    UPDATE Roster
    SET Name = ? WHERE Name = 'Jadzia Dax'
''', ('Ezri Dax',))
database.commit()

# 4. **Query Data**:
#    - Retrieve and display the **Name** and **Age** of all characters where the `Species` is **Bajoran**.

data = cursor.execute('''
    SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
''')
print(list(data))

# 5. **Delete Data**:
#    - Remove all characters aged over 100 years from the table.

cursor.execute('''
    DELETE FROM Roster WHERE Age > 100
''')
database.commit()

# 6. **Bonus Task**:
#    - Add a new column called `Rank` to the **Roster** table and update the data with the following values:
   
# | Name           | Rank       |
# |----------------|------------|
# | Benjamin Sisko | Captain    |
# | Ezri Dax       | Lieutenant |
# | Kira Nerys     | Major      |

try:
    cursor.execute('''
        ALTER TABLE Roster
        ADD COLUMN Rank TEXT
    ''')
except sqlite3.OperationalError:
    pass

ranks = [
    ('Benjamin Sisko', 'Captain'),
    ('Ezri Dax', 'Lieutenant'),
    ('Kira Nerys', 'Major')
]

for name, rank in ranks:
    cursor.execute('''
        UPDATE Roster
        SET Rank = ?
        WHERE Name = ?
    ''', (rank, name))
database.commit()

# 7. **Advanced Query**:
#    - Retrieve all characters sorted by their `Age` in descending order.

data = cursor.execute('''
    SELECT * FROM Roster ORDER BY Age DESC
''')
print(list(data))

database.close()


# ### Task 2

# 1. **Database Creation**:
#    - Create a new SQLite database named `library.db`.
#    - Define a table called **Books** with the following schema:
#      - **Title**: TEXT
#      - **Author**: TEXT
#      - **Year_Published**: INTEGER
#      - **Genre**: TEXT

database2 = sqlite3.connect('library.db')
cursor2 = database2.cursor()

cursor2.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
''')

# 2. **Insert Data**:
#    - Populate the **Books** table with the following entries:

# | Title                  | Author          | Year_Published | Genre      |
# |------------------------|-----------------|----------------|------------|
# | To Kill a Mockingbird  | Harper Lee      | 1960           | Fiction    |
# | 1984                   | George Orwell   | 1949           | Dystopian  |
# | The Great Gatsby       | F. Scott Fitzgerald | 1925        | Classic    |

books_data = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]

cursor2.executemany('''
    INSERT INTO Books (Title, Author, Year_Published, Genre)
    VALUES (?, ?, ?, ?)
''', books_data)
database2.commit()

# 3. **Update Data**:
#    - Update the `Year_Published` of **1984** to **1950**.
cursor2.execute('''
    UPDATE Books
    SET Year_Published = 1950 
    WHERE Title = '1984'
''')
database2.commit()

# 4. **Query Data**:
#    - Retrieve and display the **Title** and **Author** of all books where the `Genre` is **Dystopian**.
data2 = cursor2.execute('''
    SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
''')
print("Dystopian books:", list(data2))

# 5. **Delete Data**:
#    - Remove all books published before the year 1950 from the table.
cursor2.execute('''
    DELETE FROM Books WHERE Year_Published < 1950
''')
database2.commit()

# 6. **Bonus Task**:
#    - Add a new column called `Rating` to the **Books** table and update the data with the following values:
# | Title                  | Rating |
# |------------------------|--------|
# | To Kill a Mockingbird  | 4.8    |
# | 1984                   | 4.7    |
# | The Great Gatsby       | 4.5    |

try:
    cursor2.execute('ALTER TABLE Books ADD COLUMN Rating REAL')
except sqlite3.OperationalError:
    pass  # If the column already exists

ratings = [
    ('To Kill a Mockingbird', 4.8),
    ('1984', 4.7),
    ('The Great Gatsby', 4.5)
]
for title, rating in ratings:
    cursor2.execute('''
        UPDATE Books
        SET Rating = ?
        WHERE Title = ?
    ''', (rating, title))
database2.commit()

# 7. **Advanced Query**:
#    - Retrieve all books sorted by their `Year_Published` in ascending order.
data2 = cursor2.execute('''
    SELECT * FROM Books ORDER BY Year_Published ASC
''')
print("Books sorted by Year:", list(data2))

database2.close()
