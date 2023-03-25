# ASS 1
# WRITE A PROGRAM THAT PROMPT THE USER TO ENTER A POSITIVE INTEGER
# AND THEN USES A WHILE LOOP TO PRINT OUT ALL THE NUMBERS BETWEEN 0 AND THAT INTEGER

user = int(input("Enter your number here: "))
i = 0
while i <= user:
    print(i)
    i += 1
    
# ASS 2
# WRITE A PROGRAM THAT USES A WHILE LOOP TO COMPUTE THE SUM OF THE FIRST
# N POSITIVE, WHERE N IS INTEGER ENTERED BY THE USER

# Get input from user
n = int(input("Enter a positive integer: "))

# Initialize variables
sum = 0
i = 1

# Use a while loop to compute the sum
while i <= n:
    sum += i
    i += 1

# # Output the result
print(f"The sum of the first {n} positive integers is {sum}.")


# ASS 3
# WRITE A PROGRAM THAT USES A WHILE LOOP TO PRINT OUT THE FIRST 
# FIBONACCI NUMBERS, WHERE N IS A POSITIVE INTERGER ENTERED BY THE USER. 
# (THE FIBONACCI SEQUENCE IS A SEQUENCE OF NUMBERS IN WHICH EACH NUMBER IS THE 
# SUM OF TWO PRECEEDING ONES: 0,1,1,2,3,5,8,13,21,..)

n = int(input("Enter a positive integer: "))

# initialize the first two numbers in the Fibonacci sequence
a, b = 0, 1

# print the first n Fibonacci numbers
count = 0
while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1


# ASS 4
# WRITE A PROGRAM THAT USES A WHILE LOOP TO SIMULATE A SIMPLE GUESSING GAME. THE PROGRAM
# SHOULD GENERATE A RANDOM NUMBER BETWEEN 1 TO 100, AND THEN PROMPT THE USER TO GUESS 
# WHAT THE NUMBER IS. AFTER EACH GUESS, THE PROGRAM SHOULD PROVIDE FEEDBACK ("TOO HIGH", "TOO LOW")
# AND KEEP TRACK OF HOW MANY GUESSES THE USER HAS MADE. THE LOOP SHOULD CONTINUE UNTIL THE USER
# GUESSES THE CORRECT NUMBER

import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# initialize guess count to 0
guess_count = 0

# loop until the user guesses the correct number
while True:
    # prompt the user to enter their guess
    try:
        guess = int(input("Guess the number (between 1 and 100): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # increment the guess count
    guess_count += 1

    # check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", guess_count, "guesses.")
        break
    
    # provide feedback to the user
    if guess > number:
        print("Too high.")
    else:
        print("Too low.")


# ASS 5
# WRITE A PROGRAM THAT PROMPTS THE USER TO ENTER A STRING, AND THEN USES A WHILE LOOP TO PRINT 
# OUR EACH CHARACTER OF THE STRING ON A SEPERATE LINE

string = input("Enter a string: ")

# initialize the index to 0
index = 0

# use a while loop to print out each character of the string on a separate line
while index < len(string):
    print(string[index])
    index += 1
    
# ASS 6
# WRITE A PROGRAM THAT USES A WHILE LOOP TO COMPUTE THE FACTORIAL OF A POSITIVE INTEGER ENTERED BY THE USER

# get input from user
n = int(input("Enter a positive integer: "))

# check if input is positive
if n < 0:
    print("Input must be a positive integer.")
else:
    # initialize variables
    factorial = 1
    i = 1
    
    # loop through all numbers from 1 to n
    while i <= n:
        factorial *= i
        i += 1
    
    # print the result
    print(f"The factorial of {n} is {factorial}.")


# # ASS 7
# # WRITE A PROGRAM THAT USES A WHILE LOOP TO PRINT OUT THE FIRST N PERFECT SQUARES, WHERE N IS A POSITIVE 
# # INTEGER ENTERED BY THE USER. 
# (A PERFECT SQUARE IS A NUMBER THAT CAN BE EXPRESSED AS THE PRODUCT OF TWO  EQUAL INTEGERS, E.G 4,9,16)


num = int(input("Input your number here. "))
i = 1

while i <= num:
    print(num*num)
    break

n = int(input("Enter a positive integer: "))
i = 1
count = 0

while count < n:
    square = i * i
    print(square)
    count += 1
    i += 1

# ASS 8
# WRITE A PROGRAM THAT PROMPTS THE USER TO ENTER A LIST OF NUMBERS (SEPEARATED BY SPACES), AND THEN
# USES A WHILE LOOP TO COMPUTE AND PRINT OUT THE SUM OF THOSE NUMBERS. THE PROGRAM SHOULD KEEP PROMPTING THE 
# USER UNTIL THEY ENTER A BLANK LINE (I.E. PRESS ENTER WITHOUT TYPING ANYTHING)
                                                                   
numbers = input("Enter a list of numbers separated by spaces: ")

total = 0
while numbers != "":
    # Split the input string into a list of individual numbers
    numbers_list = numbers.split()
    
    # Iterate over the list and add each number to the total
    for number in numbers_list:
        total += int(number)
    
    # Prompt the user to enter another list of numbers or to exit
    numbers = input("Enter another list of numbers or press enter to exit: ")

# Print out the final total
print("The total sum of the entered numbers is:", total)