#  Write a program to check if a number is within a specified range.


number = float(input("Enter a number: "))
lower_bound = float(input("Enter the lower bound of the range: "))
upper_bound = float(input("Enter the upper bound of the range: "))


if lower_bound <= number <= upper_bound:
    print(f"{number} is within the range of {lower_bound} and {upper_bound}.")
else:
    print(f"{number} is not within the range of {lower_bound} and {upper_bound}.")
