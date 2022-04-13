"""
Coding Question 1: Password Please!
-----------------------------------
Write a Python script that asks the user, "Please enter your password: ". 

If the user incorrectly guesses the password, print a message that says: 
>>> "Incorrect password"
>>> "Please enter your password: " 

After three incorrect guesses, print a message saying: "Access denied" then end the program. 
If the user enters the correct password, print a message saying "Access granted" and end the program. 

Set the correct password to be your student number.
"""
# This is just one possible solution!

# How can this be refactored? Is there any duplication?
# Why did I decide to use a while loop?
# Is there a way to fit all input statements into the while loop?
# Why did I set password as a string?

password = "12345678"
user_input = input("Please enter your password: ")
attempts = 1

while user_input != password and attempts < 3:
    print("Incorrect password")
    user_input = input("Please enter your password: ")
    attempts += 1

if user_input == password:
    print("Access granted")
else:
    print("Access denied")