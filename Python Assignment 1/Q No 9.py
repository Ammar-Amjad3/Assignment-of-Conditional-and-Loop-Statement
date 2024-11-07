# Take three sides of a triangle as input and check if they form a valid triangle.

side1 = float(input("Enter the first side:"))
side2 = float(input("Enter the second side:"))
side3 = float(input("Enter the third side:"))
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("The triangle is valid")
else:
    print("The triangle is not valid")