def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None  # Handle division by zero
    return a / b

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    operator = input("Enter an operator (+, -, *, /): ")

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
        if result is None:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operator! Please use one of +, -, *, /.")
        return

    print(f"The result of {num1} {operator} {num2} is {result}")

if __name__ == "__main__":
    calculator()
