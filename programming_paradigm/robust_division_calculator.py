def safe_divide(numerator, denominator):
    try:
        numerator, denominator = float(numerator), float(denominator)
        result = numerator/denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"