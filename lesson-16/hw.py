# import sqlite3
# import pandas as pd

# # ### Homework: Pandas Basics

# # #### Part 1: Reading Files  
# # 1. **`chinook.db`**  
# #    - Use the `sqlite3` library to connect to the database.  
# #    - Read the `customers` table into a pandas DataFrame. Display the first 10 rows.  

# # 2. **`iris.json`**  
# #    - Load the JSON file into a DataFrame. Show the shape of the dataset and the column names.  

# # 3. **`titanic.xlsx`**  
# #    - Load the Excel file into a DataFrame. Use `head` to display the first 5 rows.  

# # 4. **Flights parquet file**  
# #    - Read the Parquet file into a DataFrame and use `info` to summarize it.  

# # 5. **`movie.csv`**  
# #    - Load the CSV file into a DataFrame and display a random sample of 10 rows.

# # 1. SQLite: customers table
# with sqlite3.connect('data/chinook.db') as connection:
#     df_customer = pd.read_sql('SELECT * FROM customers', con=connection)
# print("Customers table (first 10 rows):")
# print(df_customer.head(10))

# # 2. iris.json
# df_json = pd.read_json('data/iris.json')
# print("\nIris dataset shape:", df_json.shape)
# print("Columns:", df_json.columns.tolist())

# # 3. titanic.xlsx
# df_excel = pd.read_excel('data/titanic.xlsx', sheet_name='Sheet1')
# print("\nTitanic dataset (first 5 rows):")
# print(df_excel.head(5))

# # 4. flights parquet
# df_parquet = pd.read_parquet('data/flights')
# print("\nFlights dataset info:")
# print(df_parquet.info())

# # 5. movie.csv
# df_csv = pd.read_csv('data/movie.csv')
# print("\nMovie dataset (random 10 rows):")
# print(df_csv.sample(10))



# # ---

# # #### Part 2: Exploring DataFrames  
# # 1. Using the DataFrame from **`iris.json`**:  
# #    - Rename the columns to lowercase.  
# #    - Select only the `sepal_length` and `sepal_width` columns.  

# # 2. From the **`titanic.xlsx`** DataFrame:  
# #    - Filter rows where the age of passengers is above 30.  
# #    - Count the number of male and female passengers (`value_counts`).  

# # 3. From the **Flights parquet file**:  
# #    - Extract and print only the `origin`, `dest`, and `carrier` columns.  
# #    - Find the number of unique destinations.  

# # 4. From the **`movie.csv`** file:  
# #    - Filter rows where `duration` is greater than 120 minutes.  
# #    - Sort the filtered DataFrame by `director_facebook_likes` in descending order.  

# # 1. Iris: rename columns + select columns

# df_json.columns = [col.lower() for col in df_json.columns]
# res = df_json[['sepallength', 'sepalwidth']]  # Make sure column names match
# print("\nSelected columns from Iris dataset:")
# print(res.head())

# # 2. Titanic: filter age > 30 and count genders
# filtered = df_excel[df_excel['Age'] > 30]
# gender_counts = filtered['Sex'].value_counts()
# print("\nPassengers older than 30:")
# print(filtered)
# print("\nGender counts among passengers older than 30:")
# print(gender_counts)

# # 3. Flights: extract columns + unique destinations
# flights_subset = df_parquet[['origin', 'dest', 'carrier']]
# unique_destinations = df_parquet['dest'].nunique()
# print("\nFlights subset (origin, dest, carrier):")
# print(flights_subset.head())
# print("Number of unique destinations:", unique_destinations)

# # 4. Movies: filter duration > 120 & sort by director_facebook_likes
# filtered_movies = df_csv[df_csv['duration'] > 120]
# sorted_movies = filtered_movies.sort_values(by='director_facebook_likes', ascending=False)
# print("\nMovies longer than 120 minutes, sorted by director Facebook likes:")
# print(sorted_movies.head(10))


# # ---

# # #### Part 3: Challenges and Explorations  
 
# # - From **`iris.json`**: Calculate the mean, median, and standard deviation for each numerical column.  
# # - From **`titanic.xlsx`**: Find the minimum, maximum, and sum of passenger ages.  

# # - From **`movie.csv`**:  
# #     - Identify the director with the highest total `director_facebook_likes`.  
# #     - Find the 5 longest movies and their respective directors.  

# # - From **Flights parquet file**:  
# #     - Check for missing values in the dataset. Fill missing values in a numerical column with the column’s mean.


# # 1st 

# df_json.columns  = [col.lower() for col in df_json.columns]

# mean_values = df_json.mean(numeric_only=True)
# median_values = df_json.median(numeric_only=True)
# standard_deviation = df_json.std(numeric_only=True)

# stats = pd.DataFrame({
#     'mean_values': mean_values,
#     "median_values": median_values,
#     "standard_deviation": standard_deviation
# })

# # print(stats)

# # 2nd

# eldest = df_excel['Age'].max(skipna=True)
# youngest = df_excel['Age'].min(skipna=True)
# all_pass = df_excel['Age'].sum(skipna=True)

# print(eldest, youngest, all_pass)

# # 3rd


# director_likes = df_csv.groupby('director_name')['director_facebook_likes'].sum()
# top_director = director_likes.idxmax()
# top_likes = director_likes.max()

# longest_movies = df_csv[['movie_title', 'director_name', 'duration']].nlargest(5, 'duration')
# print(longest_movies)

# print(f"Director with highest total likes: {top_director} ({top_likes} likes)")


# # Check for missing values in the entire dataset
# missing_values = df_parquet.isnull().sum()
# print("Missing values per column:\n", missing_values)

# # Pick a numerical column (for example: 'dep_delay') and fill NaNs with its mean
# if 'dep_delay' in df_parquet.columns:
#     mean_dep_delay = df_parquet['dep_delay'].mean(skipna=True)
#     df_parquet['dep_delay'] = df_parquet['dep_delay'].fillna(mean_dep_delay)
#     print(f"\nFilled NaNs in 'dep_delay' with mean: {mean_dep_delay}")

import numpy as np

array= np.identity(3)
print(array)