import calendar

# Function to display the calendar for the given month and year
def display_calendar(year, month):
    print(calendar.month(year, month))

# Take input from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
display_calendar(year, month)
