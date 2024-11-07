# Print all prime numbers between 1 and 50.

for num in range(1, 51):
    if num > 1:  # Check if the number is greater than 1
        is_prime = True  # Assume the number is prime
        for i in range(2, num):  # Check divisors from 2 to num-1
            if (num % i) == 0:  # If num is divisible by i
                is_prime = False  # Set is_prime to False
                break  # Exit the inner loop if a divisor is found
        if is_prime:  # If no divisors were found
            print(num)  # Print the prime number
