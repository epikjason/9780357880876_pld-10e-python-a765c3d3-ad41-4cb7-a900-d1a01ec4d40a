"""Program Name: BadDate.py
Function: This program determines if a date entered by the user is valid.
Input:  Interactive
Output: Valid date is printed or user is alerted that an invalid date was entered.
"""
# Declare variables
valid_date = True
min_year, min_month, max_month, min_day, max_day = 0, 1, 12, 1, 31

# This is the work of the housekeeping() method
# Get the year, then the month, then the day

year_str = input("Enter year: ")
month_str = input("Enter month: ")
day_str = input("Enter day: ")

# Convert Strings to integers
year = int(year_str)
month = int(month_str)
day = int(day_str)

# This is the work of the detailLoop() method
# Check to be sure date is valid
if year <= min_year:  # invalid year
   valid_date = False
elif month < min_month and month > max_month:  # invalid month
   valid_date = False
elif day < min_day or day > max_day: # invalid day
   valid_date = False


# This is the work of the endOfJob() method
# Test to see if date is valid and output date and whether it is valid or not
if valid_date:
   # Output statement
   print(month, "/", day, "/", year, " is a valid date")
else:
   # Output statement
   print(month, "/", day, "/", year, " is an invalid date")