
print("-" * 40)
print("\033[031m         SIMPLE APP CALCULATOR\033[0m")
print("-" * 40)

class InvalidOperationError(Exception):
    pass

class ArithmeticOperations:
    def add(self, num_1, num_2):
        return num_1 + num_2

    def subtract(self, num_1, num_2):
        return num_1 - num_2

    def multiply(self, num_1, num_2):
        return num_1 * num_2

    def divide(self, num_1, num_2):
        return num_1 / num_2

while True:
    try:
        print("\n[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division")

        user_choice = input("Choose (1-4): ")

        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        math_operations = ArithmeticOperations()

        if user_choice == "1":
            result = math_operations.add(num_1, num_2)
        elif user_choice == "2":
            result = math_operations.subtract(num_1, num_2)
        elif user_choice == "3":
            result = math_operations.multiply(num_1, num_2)
        elif user_choice == "4":
            result = math_operations.divide(num_1, num_2)

        print("Result:", result)

    except Exception as unexpected_error:
        print("Error:", unexpected_error)

    retry = input("Try again? (y/n): ")
    if retry != 'y':
        print("Thank you!")
        break


