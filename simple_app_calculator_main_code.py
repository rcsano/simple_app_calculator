
title = "SIMPLE APP CALCULATOR"
print("-" * 40)
print(f"\033[031m{title.center(40)}\033[0m")
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


class CalculatorMaangasApp(ArithmeticOperations):
    def execute_calculation(self):
        print("\n[1] Addition"
              "\n[2] Subtraction"
              "\n[3] Multiplication"
              "\n[4] Division")

        user_choice = input("Please choose an operation (1-4): ")

        if user_choice not in ("1", "2", "3", "4"):
            raise InvalidOperationError("Invalid choice")

        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))

        operations_dictionary = {
            "1": self.add,
            "2": self.subtract,
            "3": self.multiply,
            "4": self.divide
        }

        result = operations_dictionary[user_choice](num_1, num_2)
        print(f"Result: {result:.2f}")

    def run(self):
        is_running = True

        while is_running:
            try:
                self.execute_calculation()

            except ValueError:
                print("Invalid input. Numbers only. Please try again.")

            except ZeroDivisionError:
                print("Cannot divide by zero.")

            except InvalidOperationError as error_message:
                print("Error:", error_message)

            except Exception as unexpected_error:
                print("Error:", unexpected_error)

            retry = input("Try again? (y/n): ").strip().lower()

            if retry != 'y':
                print("\nThank you for using the Maangas Calculator. See you next time!")
                is_running = False


if __name__ == '__main__':
    calculator_app = CalculatorMaangasApp()
    calculator_app.run()
