# Write a program to find the largest of three numbers.

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
num3 = float(input("Enter third number"))
if num1 > num2 and num1 > num3:
    print("Largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is", num2)
elif num3 >= num1 and num3 > num2:
    print("larget number is", num3)
else:
    print("All numbers are equal")

