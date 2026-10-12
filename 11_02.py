"""
Assignment -> 11
Topic -> More on Operators
02  ||  Write a python script to input two strings from the user and display whether the two variables referred to the same object or not. print True or False.
"""

a = input("Enter a String: ")
b = input("Enter another String: ")
print(b is a)