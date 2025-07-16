
import sys

def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def add_three_numbers(a, b, c):
    """Add three numbers and return the result."""
    return a + b + c

def divide_result(dividend, divisor):
    """Divide the dividend by the divisor and return the result.
    
    Handles division by zero.
    """
    if divisor == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)
    return dividend / divisor

def main(args):
    try:
        # Convert command line arguments to floats
        num1 = float(args[1])
        num2 = float(args[2])
        num3 = float(args[3])
        num4 = float(args[4])
        num5 = float(args[5])
        
        # Compose the functions as required
        result_multiplication = multiply_numbers(num1, num2)
        result_addition = add_three_numbers(num3, num4, num5)
        final_result = divide_result(result_multiplication, result_addition)
        
        print(f"The result of division is: {final_result}")
    
    except (IndexError, ValueError):
        print("Error: Please provide exactly five floating point numbers as command line arguments.")
        sys.exit(1)

# Example usage:
# python script.py 4.5 2.0 1.0 2.0 3.0
if __name__ == "__main__":
    main(sys.argv)
