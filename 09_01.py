"""
Assignment -> 09
Topic -> Simple Calculations on user data
01  ||  Write a python script to calculate simple interest.
"""

p = int(input("Enter Principal Amount: "))
r = float(input("Enter Rate: "))
t = int(input("Enter Time(in years): "))
SI = (p*r*t)/100
print("Simple Interest = ",SI) 