from collections import Counter
import random




### Questions:

# 1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
# 2.  What is the difference between the continue and break statements in Python?

# break: Exits the loop entirely. while the continue skips the current element only and moves to the next one.

# 3. Can you explain the difference between for loop and while loop?

# for: Used when the number of iterations is known.

# while: Used when the loop continues based on a condition.

# 4. How would you implement a nested for loop system? Provide an example.

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# ## Homeworks:

# **1.** Return uncommon elements of lists. Order of elements does not matter.

# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]



# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]



# input:
#     list1 = [1, 1, 2, 3, 4, 2]
#     list2 = [1, 3, 4, 5]
# output: [2, 2, 5]

def uncommon(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = list((c1 - c2).elements()) + list((c2 - c1).elements())
    return result

print(uncommon([1, 1, 2], [2, 3, 4]))        # [1, 1, 3, 4]
print(uncommon([1, 2, 3], [4, 5, 6]))        # [1, 2, 3, 4, 5, 6]
print(uncommon([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]


# **2.** Print the square of each number which is less than `n` on a separate line.


# input: n = 5
# output:
#     1
#     4
#     9
#     16

n = 5
for i in range(1, n):
    print(i * i)


# **3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

def insert_underscores(txt):
    result = ""
    vowels = "aeiou"
    i = 0
    while i < len(txt):
        result += txt[i]
        if i + 1 < len(txt):
            if (i + 1) % 3 == 0 and txt[i] not in vowels:
                result += "_"
            elif txt[i] in vowels:
                result += "_"
        i += 1
    return result

print(insert_underscores("hello"))
print(insert_underscores("assalom")) 
print(insert_underscores("abcabcdabcdeabcdefabcdefg"))


# input: hello
# output: hel_lo



# input: assalom
# output: ass_alom



# input: abcabcdabcdeabcdefabcdefg
# output: abc_abcd_abcdeab_cdef_abcdefg



# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.


# > Hint: Use Python’s `random.randint()` to generate the number.



def play_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10

        while attempts > 0:
            guess = int(input("Guess the number between (1–100): "))
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("You guessed it right!")
                break
            attempts -= 1

        if attempts == 0:
            print("You lost. Want to play again?")
        again = input("Play again? (Y/YES/ok): ").lower()
        if again not in ['y', 'yes', 'ok']:
            break

play_game()


# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."

password = input("Enter your password: ")

if len(password) < 8:
    print("Password is too short.")
elif not any(c.isupper() for c in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")


# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

# ---


for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.


choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    player = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score => You: {player_score}, Computer: {computer_score}\n")

if player_score == 5:
    print("You won the game!")
else:
    print("Computer won the game!")