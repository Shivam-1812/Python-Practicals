# Input marks for 5 subjects
print("Enter marks for 5 subjects out of 100:")

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

# Display total and percentage
print(f"\nTotal Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")

# Determine grade
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")
