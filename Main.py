import Calculator

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ("add", "subtract", "multiply", "divide"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if user_input == "add":
            print(Calculator.add(x, y))
        elif user_input == "subtract":
            print(Calculator.subtract(x, y))
        elif user_input == "multiply":
            print(Calculator.multiply(x, y))
        elif user_input == "divide":
            print(Calculator.divide(x, y))