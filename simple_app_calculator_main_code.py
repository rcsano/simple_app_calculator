
print("-" * 40)
print("\033[031m         SIMPLE APP CALCULATOR\033[0m")
print("-" * 40)

class InvalidOperationError(Exception):
    pass

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    try:
        print("\n[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division")

        user_choice = input("Choose (1-4): ")

        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        if user_choice == "1":
            result = add(num_1, num_2)
        elif user_choice == "2":
            result = subtract(num_1, num_2)
        elif user_choice == "3":
            result = multiply(num_1, num_2)
        elif user_choice == "4":
            result = divide(num_1, num_2)

        print("Result:", result)

    except ValueError:
        print("Invalid input. Numbers only. Please try again.")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    retry = input("Try again? (y/n): ")
    if retry != 'y':
        print("Thank you!")
        break


