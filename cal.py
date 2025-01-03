def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            # Get user input for operation
            operation = input("Enter the operation you want to perform (+, -, *, /) or 'q' to quit: ").strip()
            if operation.lower() == 'q':
                print("Goodbye!")
                break
            
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please choose from +, -, *, /.")
                continue
            
            # Get numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            
            # Display the result
            print(f"The result of {num1} {operation} {num2} is: {result}")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
