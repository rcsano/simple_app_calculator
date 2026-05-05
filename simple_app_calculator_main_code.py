
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

        if user_choice not in ("1", "2", "3", "4"):
            raise InvalidOperationError("Invalid choice")

        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        math_operations = ArithmeticOperations()

        operations_dictionary = {
            "1": math_operations.add,
            "2": math_operations.subtract,
            "3": math_operations.multiply,
            "4": math_operations.divide
        }

        result = math_operations[user_choice](num_1, num_2)

        print("Result:", result)

    except ValueError:
        print("Invalid input. Numbers only. Please try again.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as unexpected_error:
        print("Error:", unexpected_error)

    retry = input("Try again? (y/n): ")
    if retry != 'y':
        print("Thank you!")
        break


