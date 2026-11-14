num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is NOT a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print(f"The factorial of {num} is {factorial}.")