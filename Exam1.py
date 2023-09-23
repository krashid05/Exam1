# Exam1.py
# Course: IT1114/
# Student Name: Keshawn Rashid
# Due Date: 09/24/ 2023
# Purpose: Tax laws are incredibly complicated. To help cope, you will write a program to do some
# of the heavy lifting.

income = float(input("Enter made income:$ "))
if income < 10000:
    tax = 2.3 * income / 100
elif income <= 500000:
    tax = 4.5 * income / 100
else:
    tax = 6.1 * income / 100

maritalStatus = input('Enter marital status married?(y/n): ')
if maritalStatus.lower() == 'y':
    tax -= 24.62
    input("How long you have been married: ")
elif maritalStatus.lower()== 'n':
    tax += 0

elevation = input('Enter current elevation (below/at/above sea level): ')
if elevation.lower() == 'below' or elevation.lower() == 'below sea level':
    tax += 18.32
elif elevation.lower() == 'above' or elevation.lower() == 'above sea level':
    bedrooms = float(input("How many bedrooms do you have: "))
    tax += 5.00 * bedrooms
else:
    tax *= 1.6

total_tax = float(tax)
print("Total tax", total_tax)

