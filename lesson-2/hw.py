# 1. Create a program that takes a float number as input and rounds it to 2 decimal places.

res = float(input('Input Float number: '))
print(round(res, 2))

# 2. Write a Python file that asks for three numbers and outputs the largest and smallest.

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

list_num = [num1, num2, num3]
print(max(list_num), min(list_num))


# 3. Create a program that converts kilometers to meters and centimeters.

km = float(input("Enter distance in kilometers: "))

meters, centimeters = int(km * 1000), int(km * 100000)
print(f'{meters} meters, {centimeters} centimeters')


# 4. Write a program that takes two numbers and prints out the result of integer division and theremainder.

num1 = int(input("Enter the first number (dividend): "))
num2 = int(input("Enter the second number (divisor): "))

quotient = 0
remainder = 0

try:
    quotient = num1 // num2
    remainder = num1 % num2
    print(quotient, remainder)
except ZeroDivisionError:
    print("devision by 0 cant be performed")


# 5. Make a program that converts a given Celsius temperature to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# 6. Create a program that accepts a number and returns the last digit of that number.

num = int(input("Enter your number"))

last_digit = abs(num) % 10
print(last_digit)


# 7. Create a program that takes a number and checks if it’s even or not.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

### String Questions:

# 1. Create a program to ask name and year of birth from user and tell them their age.

name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))

current_year = 2025
age = current_year - year_of_birth

print(f"Hello, {name}! You are {age} years old.")


# 2. Extract car names from this text:


txt = 'LMaasleitbtui'
car_names = ['Lamborghini', 'Maserati', 'Tesla', 'BMW', 'Audi']

found_cars = []

for car in car_names:
    idx = 0
    for char in txt.lower():
        if idx < len(car) and char == car.lower()[idx]:
            idx += 1
    if idx == len(car):
        found_cars.append(car)

print("Cars found in the text:", found_cars)


# 3. Write a Python program to:
#    - Take a string input from the user.
#    - Print the length of the string.
#    - Convert the string to uppercase and lowercase.

user_input = input("Enter a string: ")

print("Length of the string:", len(user_input))

print("Uppercase:", user_input.upper())

print("Lowercase:", user_input.lower())

# 4. Write a Python program to check if a given string is `palindrome` or not.
# > What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.

text = str(input("Enter a string: "))

if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 5. Write a program that counts the number of vowels and consonants in a given string.

text = input("Enter a string: ")

vowels = 0
consonants = 0
vowel_set = "aeiouAEIOU"

for char in text:
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)



# 6. Write a Python program to check if one string contains another.

string1 = input("Enter the main string: ")
string2 = input("Enter the string to search for: ")

if string2 in string1:
    print("Yes, the main string contains the searched string.")
else:
    print("No, the main string does not contain the searched string.")


# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
#    - Input sentence: "I love apples."  
#    - Replace: "apples"  
#    - With: "oranges"  
#    - Output: "I love oranges."

sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")

new_sentence = sentence.replace(word_to_replace, replacement_word)
print("Updated sentence:", new_sentence)

# 8. Write a program that asks the user for a string and prints the first and last characters of the string.  

text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])

# 9. Ask the user for a string and print the reversed version of it.

text = str(input("Enter a string: "))
print(text[::-1])

# or 

print(''.join(reversed(text)))


# 10. Write a program that asks the user for a sentence and prints the number of words in it.  

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))


# 11. Write a program to check if a string contains any digits.  

text = input("Enter a string: ")

contains_digit = any(char.isdigit() for char in text)

if contains_digit:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")

# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`). 

words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator (e.g., - or ,): ")

joined_string = separator.join(words)

print("Joined string:", joined_string) 

# 13. Ask the user for a string and remove all spaces from it.  

text = input("Enter a string: ")

no_spaces = text.replace(" ", "")

print("String without spaces:", no_spaces)


# 14. Write a program to ask for two strings and check if they are equal or not.  

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if str1 == str2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

# 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
#     Example:  
#     - Input: "World Health Organization"  
#     - Output: "WHO"  

sentence = input("Enter a sentence: ")
words = sentence.split()
acronym = ''.join(word[0].upper() for word in words)
print("Acronym:", acronym)

# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  

text = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
result = text.replace(char_to_remove, "")
print("Result:", result)


# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
for vowel in vowels:
    text = text.replace(vowel, "*")
print("Result:", text)


# 18. Write a program that checks if a string starts with one word and ends with another.  
#     Example:  
#     - Input: "Python is fun!"  
#     - Starts with: "Python"  
#     - Ends with: "fun!"  

text = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")

if text.startswith(start_word) and text.endswith(end_word):
    print("The string starts with", start_word, "and ends with", end_word)
else:
    print("The string does not match the given start and end words.")


# Booleans 

# 1. Write a program that accepts a username and password and checks if both are not empty.

username = input("Enter username: ")
password = input("Enter password: ")

if username and password:
    print("Username and password accepted.")
else:
    print("Username and password cannot be empty.")

# 2. Create a program that checks if two numbers are equal and outputs a message if they are.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")


# 3. Write a program that checks if a number is positive and even.

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not both positive and even.")


# 4. Write a program that takes three numbers and checks if all of them are different.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and b != c and a != c:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")


# 5. Create a program that accepts two strings and checks if they have the same length.

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) == len(str2):
    print("The strings have the same length.")
else:
    print("The strings have different lengths.")


# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")


# 7. Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x + y > 50:
    print("The sum is greater than 50.")
else:
    print("The sum is not greater than 50.")


num = int(input("Enter a number: "))

if 10 <= num <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not in the range 10 to 20.")

