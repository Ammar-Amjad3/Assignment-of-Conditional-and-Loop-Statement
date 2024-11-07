#  Print the reverse of a given number.

number = int(input("Enter an integer: "))

reverse = 0


is_negative = number < 0
number = abs(number)  # Work with the absolute value


while number > 0:
    digit = number % 10          # Get the last digit
    reverse = reverse * 10 + digit  # Add the digit to the reversed number
    number //= 10                # Remove the last digit

if is_negative:
    reverse = -reverse

print("The reverse of the number is:", reverse)
