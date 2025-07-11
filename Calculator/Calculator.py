def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Cannot divide by zero")
                    continue
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue

            print(f"{num1} {op} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        again = input("Do you want to calculate again? (y/n): ")
        if again.lower() != 'y':
            print("Thanks for using the calculator. Goodbye!")
            break

calculator()

