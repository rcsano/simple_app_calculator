
print("-" * 40)
print("\033[031m         SIMPLE APP CALCULATOR\033[0m")
print("-" * 40)

while True:
    try:
        print("\n[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division")

        user_choice = input("Choose (1-4): ")

        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))

        if user_choice == "1":
            result = first_num + second_num
        elif user_choice == "2":
            result = first_num - second_num
        elif user_choice == "3":
            result = first_num * second_num
        elif user_choice == "4":
            result = first_num / second_num

        print("Result:", result)

    except ValueError:
        print("Invalid input. Numbers only. Please try again.")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    retry = input("Try again? (y/n): ")
    if retry != 'y':
        print("Thank you!")
        break


