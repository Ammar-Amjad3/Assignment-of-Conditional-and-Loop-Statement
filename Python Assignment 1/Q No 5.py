#  Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F)

# Method 1

# percentage = float(input("Enter your grade percentage"))
# # Conditional checks for letter grade
# if percentage >= 90:
#     print("Grade: A")
# elif percentage >= 80:
#     print("Grade: B")
# elif percentage >= 70:
#     print("Grade C")
# elif percentage <=33:
#     print("Grade: F")

# Method 2

percentage = float(input("Enter your grade percentage: "))

# Conditional checks for letter grade
if 90 <= percentage <= 100:
    print("Your grade is: A")
elif 80 <= percentage < 90:
    print("Your grade is: B")
elif 70 <= percentage < 80:
    print("Your grade is: C")
elif 60 <= percentage < 70:
    print("Your grade is: D")
else:
    print("Your grade is: F")

