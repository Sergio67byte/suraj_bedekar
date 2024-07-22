def calculator():
    operation = input("Enter operation (add, subtract, divide): ").strip().lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operation"

    print(f"The result is: {result}")

# Run the calculator
calculator()
