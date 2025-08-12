# Program Lab5A.py
# Class: CSE 1321L
# Section: W01
# Term: Summer 2025
# Instructor: Milo Wilson
# Name: Tamia Thomas
# Lab: Lab5A


print("Please enter 10 numbers and this program will display the largest.")
largest = 1

for i in range(1, 11):
    number = int(input(f"Please enter number {i}: "))
    if number > largest:
        largest = number

print(f"The largest number was {largest}")
