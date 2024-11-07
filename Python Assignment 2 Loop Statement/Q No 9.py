#  Write a program to print the first 10 Fibonacci numbers.

# Initialize the first two Fibonacci numbers
a, b = 0, 1

print("The first 10 Fibonacci numbers are:")
for _ in range(10):
    print(a)
    a, b = b, a + b


# A Fibonacci number is a number in the Fibonacci sequence, a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence typically goes as follows:

# 0 (the first Fibonacci number)
# 1 (the second Fibonacci number)
# 1 (the third Fibonacci number, 0 + 1)
# 2 (the fourth Fibonacci number, 1 + 1)
# 3 (the fifth Fibonacci number, 1 + 2)
# 5 (the sixth Fibonacci number, 2 + 3)
# 8 (the seventh Fibonacci number, 3 + 5)
# 13 (the eighth Fibonacci number, 5 + 8)
# 21 (the ninth Fibonacci number, 8 + 13)
# 34 (the tenth Fibonacci number, 13 + 21)
