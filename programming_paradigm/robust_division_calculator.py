# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division robustly, handling ZeroDivisionError and ValueError 
    for non-numeric inputs.

    :param numerator: The number to be divided (can be a string).
    :param denominator: The number to divide by (can be a string).
    :return: A string containing the result or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den

        return f"The result of the division is {result}"

    except ValueError:
        # Catches exceptions if float() conversion fails (e.g., input is "ten")
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Catches exceptions if the division operation has a denominator of zero
        return "Error: Cannot divide by zero."

# End of robust_division_calculator.py