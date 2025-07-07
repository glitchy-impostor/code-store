
# Importing required module for reading command line arguments
import sys

def add_numbers(a, b, c, d, e, f):
    """
    Function to add six numbers.

    Args:
        a (int/float): First number.
        b (int/float): Second number.
        c (int/float): Third number.
        d (int/float): Fourth number.
        e (int/float): Fifth number.
        f (int/float): Sixth number.

    Returns:
        int/float: Sum of the six numbers.
    """
    return a + b + c + d + e + f

if __name__ == "__main__":
    # Checking if exactly six command line arguments are provided
    if len(sys.argv) != 7:
        print("Usage: python script.py num1 num2 num3 num4 num5 num6")
        sys.exit(1)

    # Parsing command line arguments to integers or floats
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        num3 = float(sys.argv[3])
        num4 = float(sys.argv[4])
        num5 = float(sys.argv[5])
        num6 = float(sys.argv[6])
    except ValueError:
        print("All arguments must be numbers.")
        sys.exit(1)

    # Calling the function and storing the result
    result = add_numbers(num1, num2, num3, num4, num5, num6)

    # Printing the result
    print(f"The sum of {num1}, {num2}, {num3}, {num4}, {num5}, and {num6} is: {result}")
