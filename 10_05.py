"""
Assignment -> 10
Topic -> Operators
05  ||  Write a python script which takes a three digit number from the user and displays only its middle digit.
"""

a = int(input("Enter a three digit number: "))
b = a//10
print("Middle Digit -", b%10)