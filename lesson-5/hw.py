# ### Task 1

# Write a script called temperature.py that defines two functions:

# 1. _convert_cel_to_far()_ which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:
#    _F = C \* 9/5 + 32_
# 2. _convert_far_to_cel()_ which take one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:
#    _C = (F - 32) \* 5/9_

# The script should first prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius. Then prompt the user to enter a temperature in degrees Celsius and display the temperature converted to Fahrenheit. All converted temperatures should be rounded to 2 decimal places.

# Here’s a sample run of the program:


# Enter a temperature in degrees F: 72
# 72 degrees F = 22.22 degrees C

# Enter a temperature in degrees C: 37
# 37 degrees C = 98.60 degrees F

def convert_cel_to_far(celsius):
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

# Prompt for Fahrenheit
f = float(input("Enter a temperature in degrees F: "))
print(f"{f} degrees F = {convert_far_to_cel(f)} degrees C")

# Prompt for Celsius
c = float(input("\nEnter a temperature in degrees C: "))
print(f"{c} degrees C = {convert_cel_to_far(c)} degrees F")


# <hr />

# ### Task 2

# In this challenge, you will write a program called invest.py that tracks the growing amount of an investment over time.

# An initial deposit, called the principal amount, is made. Each year, the amount increases by a fixed percentage, called the annual rate of return.

# For example, a principal amount of \$100 with an annual rate of return of 5% increases the first year by \$5. The second year, the increase is 5% of the new amount \$105, which is \$5.25.

# Write a function called invest with three parameters: the principal amount, the annual rate of return, and the number of years to calculate. The function signature might look something like this:

# python
# def invest(amount, rate, years):


# The function then prints out the amount of the investment, rounded to 2 decimal places, at the end of each year for the specified number of years.

# For example, calling _invest(100, .05, 4)_ should print the following:


# year 1: $105.00
# year 2: $110.25
# year 3: $115.76
# year 4: $121.55


# To finish the program, prompt the user to enter an initial amount, an annual percentage rate, and a number of years. Then call invest() to display the calculations for the values entered by the user.

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

# Get user input
principal = float(input("Enter initial amount: "))
annual_rate = float(input("Enter annual rate (as percent): ")) / 100
years = int(input("Enter number of years: "))

# Call function
invest(principal, annual_rate, years)



# <hr />

# ### Task 3

# A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.

# For example, 3 is a factor of 12 because 12 divided by 3 is 4, with no remainder. However, 5 is not a factor of 12 because 5 goes into 12 twice with a remainder of 2.

# Write a script factors.py that asks the user to input a positive integer and then prints out the factors of that number. Here’s a sample run of the program with output:


# Enter a positive integer: 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12

n = int(input("Enter a positive integer: "))
print()

for i in range(1, n + 1):
    if n % i == 0:
        print(f"{i} is a factor of {n}")


# ### Task 4

# Write a program that contains the following lists of lists:

# python
# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]


# Define a function, _enrollment_stats()_, that akes, as an input, a list of lists where each individual list contains three elements: (a) the name of a university, (b) the total number of enrolled students, and (c) the annual tuition fees.

# _enrollment_stats()_ should return two lists: the first containing all of the student enrollment values and the second containing all of the tuition fees.

# Next, define a _mean()_ and a _median()_ function. Both functions should take a single list as an argument and return the mean and median of the values in each list.

# Using universities, _enrollment_stats()_, _mean()_, and _median()_, calculate the total number of students, the total tuition, the mean and median of the number of students, and the mean and median tuition values.

# Finally, output all values, and format the output so that it looks like this:


# ******************************
# Total students: 77,285
# Total tuition: $ 271,905

# Student mean: 11,040.71
# Student median: 10,566

# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
# ******************************

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(univ_list):
    students = [u[1] for u in univ_list]
    tuitions = [u[2] for u in univ_list]
    return students, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    values = sorted(values)
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]

students, tuitions = enrollment_stats(universities)

print("******************************")
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuitions):,}")

print(f"\nStudent mean: {mean(students):,.2f}")
print(f"Student median: {int(median(students))}")

print(f"\nTuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {int(median(tuitions))}")
print("******************************")

# ---

# ### Task 5
# Define a function `is_prime(n)` which returns `True` if the given $n$ ($n$ > 0) is _prime number_, otherwise returns `False`.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example use
num = int(input("Enter a number: "))
print(f"{num} is prime? {is_prime(num)}")