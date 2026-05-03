print("-" * 40)
print("\033[031m         SIMPLE APP CALCULATOR\033[0m")
print("-" * 40)

# simple maangas calculator app
while True:
# show menu (add, subtract, multiply, divide)
    print("\n[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division")

# get user choice
    user_choice = input("Choose (1-4): ")

# ask for 2 numbers
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))

# perform operation
    if user_choice == "1":
        result = first_num + second_num
    elif user_choice == "2":
        result = first_num - second_num
    elif user_choice == "3":
        result = first_num * second_num
    elif user_choice == "4":
        result = first_num / second_num

# print result
    print("Result:", result)

# ask if user wants to try again
    retry = input("Try again? (y/n): ")
    if retry != 'y':
        print("Thank you!")
        break


