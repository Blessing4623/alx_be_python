def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
            return result
        case "subtract":
            result = num1 - num2
            return result
        case "multiply":
            result = num1 * num2
            return result
        case "divide":
            result = num1 / num2
            return result
        case _:
            print("Invalid Operator")