from bs4 import BeautifulSoup
import requests
import sqlite3
import csv

# ### Task 1

# Scrape weather information from an HTML file and process it using Python and BeautifulSoup.

# <h4>5-Day Weather Forecast</h4>
# <table>
#     <thead>
#         <tr>
#             <th>Day</th>
#             <th>Temperature</th>
#             <th>Condition</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Monday</td>
#             <td>25°C</td>
#             <td>Sunny</td>
#         </tr>
#         <tr>
#             <td>Tuesday</td>
#             <td>22°C</td>
#             <td>Cloudy</td>
#         </tr>
#         <tr>
#             <td>Wednesday</td>
#             <td>18°C</td>
#             <td>Rainy</td>
#         </tr>
#         <tr>
#             <td>Thursday</td>
#             <td>20°C</td>
#             <td>Partly Cloudy</td>
#         </tr>
#         <tr>
#             <td>Friday</td>
#             <td>30°C</td>
#             <td>Sunny</td>
#         </tr>
#     </tbody>
# </table>


# Assume you are given the following HTML structure (you can save it as `weather.html`):

# html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Weather Forecast</title>
# </head>
# <body>
#     <h4>5-Day Weather Forecast</h4>
#     <table>
#         <thead>
#             <tr>
#                 <th>Day</th>
#                 <th>Temperature</th>
#                 <th>Condition</th>
#             </tr>
#         </thead>
#         <tbody>
#             <tr>
#                 <td>Monday</td>
#                 <td>25°C</td>
#                 <td>Sunny</td>
#             </tr>
#             <tr>
#                 <td>Tuesday</td>
#                 <td>22°C</td>
#                 <td>Cloudy</td>
#             </tr>
#             <tr>
#                 <td>Wednesday</td>
#                 <td>18°C</td>
#                 <td>Rainy</td>
#             </tr>
#             <tr>
#                 <td>Thursday</td>
#                 <td>20°C</td>
#                 <td>Partly Cloudy</td>
#             </tr>
#             <tr>
#                 <td>Friday</td>
#                 <td>30°C</td>
#                 <td>Sunny</td>
#             </tr>
#         </tbody>
#     </table>

# </body>
# </html>


# 1. **Parse the HTML File**:
#    - Load the `weather.html` file using BeautifulSoup and extract the weather forecast details.

# 2. **Display Weather Data**:
#    - Print the **day**, **temperature**, and **condition** for each entry in the forecast.

# 3. **Find Specific Data**:
#    - Identify and print the day(s) with:
#      - The highest temperature.
#      - The "Sunny" condition.

# 4. **Calculate Average Temperature**:
#    - Compute and print the **average temperature** for the week.

# with open('weather.html', 'r', encoding='utf-8') as file:
#     soup = BeautifulSoup(file.read(), 'lxml') 

# rows = soup.find('tbody').find_all('tr')   # type: ignore

# weather_data = []
# for row in rows:
#     cols = row.find_all('td')
#     day = cols[0].text
#     temp = int(cols[1].text.replace('°C', ''))
#     condition = cols[2].text
#     weather_data.append({'day': day, 'temp': temp, 'condition': condition})

# print("Weather Forecast:")
# for entry in weather_data:
#     print(f"{entry['day']}: {entry['temp']}°C, {entry['condition']}")

# max_temp = max(weather_data, key=lambda x: x['temp'])
# sunny_days = [entry['day'] for entry in weather_data if entry['condition'].lower() == 'sunny']
# print(f"\nHottest Day: {max_temp['day']} ({max_temp['temp']}°C)")
# print("Sunny Days:", ", ".join(sunny_days))


# avg_temp = sum(entry['temp'] for entry in weather_data) / len(weather_data)
# print(f"\nAverage Temperature: {avg_temp:.1f}°C")

# ---

# ### Task 2

# Scrape job listings from the website https://realpython.github.io/fake-jobs and store the data into an SQLite database.

# 1. **Scraping Requirements**:
#    - Extract the following details for each job listing:
#      - **Job Title**
#      - **Company Name**
#      - **Location**
#      - **Job Description**
#      - **Application Link**

# 2. **Data Storage**:
#    - Store the scraped data into an SQLite database in a table named `jobs`.

# 3. **Incremental Load**:
#    - Ensure that your script performs **incremental loading**:
#      - Scrape the webpage and add only **new job listings** to the database.
#      - Avoid duplicating entries. Use `Job Title`, `Company Name`, and `Location` as unique identifiers for comparison.

# 4. **Update Tracking**:
#    - Add functionality to detect if an existing job listing has been updated (e.g., description or application link changes) and update the database record accordingly.

# 5. **Filtering and Exporting**:
#    - Allow filtering job listings by **location** or **company name**.
#    - Write a function to export filtered results into a CSV file.


# database = sqlite3.connect('job_listing.db')
# cursor = database.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS jobs (
#         job_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         company TEXT NOT NULL,
#         location TEXT NOT NULL,
#         description TEXT,
#         link TEXT,
#         last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         UNIQUE(title, company, location)
#     )
# ''')
# database.commit()

# # --- Helper to get job description ---
# def get_description(url):
#     try:
#         detail_page = requests.get(url, timeout=5)
#         detail_page.raise_for_status()
#     except requests.RequestException:
#         return ""  # if fail, skip
#     detail_soup = BeautifulSoup(detail_page.text, 'html.parser')
#     desc_tag = detail_soup.find('div', class_='content')
#     if desc_tag:
#         paragraphs = desc_tag.find_all('p')
#         return "\n".join([p.text.strip() for p in paragraphs])
#     return ""


# # --- Scrape jobs ---
# data = requests.get('https://realpython.github.io/fake-jobs')
# soup = BeautifulSoup(data.text, 'html.parser')
# jobs = soup.find_all('div', class_='column is-half')

# job_data = []
# for job in jobs:
#     title = job.find('h2', class_='title is-5').text.strip()
#     company = job.find('h3', class_='subtitle is-6 company').text.strip()
#     location = job.find('p', class_='location').text.strip()

#     a_tags = job.find_all('a', class_='card-footer-item')
#     apply_link = a_tags[1]['href'] if len(a_tags) > 1 else None
#     description = get_description(apply_link) if apply_link else ""


#     job_data.append((title, company, location, description, apply_link))

# # --- Insert or update in DB ---
# for title, company, location, desc, link in job_data:
#     cursor.execute('''
#         INSERT OR REPLACE INTO jobs (title, company, location, description, link, last_updated)
#         VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
#     ''', (title, company, location, desc, link))
# database.commit()

# # --- Filtering ---
# def filter_jobs(location=None, company=None):
#     query = "SELECT * FROM jobs WHERE 1=1"
#     params = []
#     if location:
#         query += " AND location=?"
#         params.append(location)
#     if company:
#         query += " AND company=?"
#         params.append(company)
#     cursor.execute(query, params)
#     return cursor.fetchall()

# # --- Export to CSV ---
# def export_to_csv(filename, rows):
#     with open(filename, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['ID', 'Title', 'Company', 'Location', 'Description', 'Link', 'Last Updated'])
#         writer.writerows(rows)

# # Example usage
# rows = filter_jobs(location='Brockburgh, AE')
# export_to_csv('filtered_jobs.csv', rows)

# ### Task 3

# You are tasked with scraping laptop data from the "Laptops" section of the [Demoblaze website](https://www.demoblaze.com/) and storing the extracted information in JSON format.

# **Steps:**

# 1. **Navigate to the Website:**
#    - Visit the [Demoblaze homepage](https://www.demoblaze.com/).
#    - Click on the **Laptops** section to view the list of available laptops.

# 2. **Navigate to the Next Page:**
#    - After reaching the Laptops section, locate and click the **Next** button to navigate to the next page of laptop listings.

# 3. **Data to Scrape:**
#    For each laptop on the page, scrape the following details:
#    - **Laptop Name**
#    - **Price**
#    - **Description**

# 4. **Data Storage:**
#    - Save the extracted information in a structured **JSON format** with fields like:
#      json
#      [
#        {
#          "name": "Laptop Name",
#          "price": "Laptop Price",
#          "description": "Laptop Description"
#        },
#        ...
#      ]

data = requests.get('https://www.demoblaze.com/')
print(data.text)