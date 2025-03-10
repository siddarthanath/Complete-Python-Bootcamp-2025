"""This file mimics a simple Calculator, which can sum numbers."""

# Using Python's in-built 'print' function, which prints information to the terminal when file is run
print("Welcome to the Sum Calculator!")
print("Enter numbers one per line. Enter 'done' to finish.")
# Storing/assigning values to variable names (LEFT HAND SIDE is the variable and RIGHT HAND SIDE is the value)
total = 0
count = 0
# While
while True:
    # Read input from the user (this will come up in the terminal for the user to interact with)
    user_input = input()  
    # Exit condition i.e., when the user types the work done, the program ends
    if user_input == "done":  
        break
    try:
        number = float(user_input)  
        total += number
        count += 1
    # Handle invalid input
    except ValueError:  
        print(f"Invalid input: {user_input}. Please enter a number.")
# Checks validity of program execution
if count > 0:
    print(f"Sum of numbers: {total}")
else:
    print("No valid numbers entered.")