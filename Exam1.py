# Exam1.py
# Course: IT1114/
# Student Name: Keshawn Rashid
# Due Date: 09/24/ 2023
# Purpose: Tax laws are incredibly complicated. To help cope, you will write a program to do some
# of the heavy lifting.
income = float(input("Enter annual income: $"))

# Calculate income tax based on income
if income < 10000:
    tax = 0.023 * income
elif income <= 50000:
    tax = 0.045 * income
else:
    tax = 0.061 * income

# marital status
marital_status = input("Are you married (y/n): ").lower()


if marital_status == "y":
    years_married = int(input("How many years have you been married: "))
    tax -= 1.62 * years_married

#current elevation
elevation = input("Enter current elevation (below-1/at-2/above sea level-3): ").lower()


if "1" in elevation:
    tax += 18.32
elif "2" in elevation:
    tax += 0.016 * income
elif "3" in elevation:
    bedrooms = int(input("How many bedrooms do you have: "))
    tax += 5.00 * bedrooms

# Display the total tax amount
total_tax = float(tax)
print("Total tax owed for the year: $", total_tax)

