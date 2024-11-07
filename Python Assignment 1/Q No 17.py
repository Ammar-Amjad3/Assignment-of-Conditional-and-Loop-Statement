#  Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

number = int(input("Enter an integer: "))

is_divisible_by_2 = number % 2 == 0
is_divisible_by_3 = number % 3 == 0


if is_divisible_by_2 and is_divisible_by_3:
    print(f"{number} is divisible by both 2 and 3.")
elif is_divisible_by_2:
    print(f"{number} is divisible by 2.")
elif is_divisible_by_3:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 2 or 3.")
