def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "devide":
        return num1 / num2
    elif num2 == 0:
        print("Cannot be divided by 0.")
    else:
        print("Numbers Invalid")
