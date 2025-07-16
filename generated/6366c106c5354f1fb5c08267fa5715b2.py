
import sys

def parse_arguments(args):
    """
    Parses command line arguments and returns two integers.
    
    Parameters:
        args (list): A list of command line arguments.
        
    Returns:
        tuple: Two integers parsed from the command line arguments.
    """
    if len(args) != 3:
        raise ValueError("Usage: python multiply.py <num1> <num2>")
    return int(args[1]), int(args[2])

def multiply_numbers(num1, num2):
    """
    Multiplies two integers.
    
    Parameters:
        num1 (int): The first integer.
        num2 (int): The second integer.
        
    Returns:
        int: The product of the two integers.
    """
    return num1 * num2

def main_driver(args):
    """
    Driver function to execute the multiplication of two numbers.
    
    Parameters:
        args (list): A list of command line arguments.
    """
    try:
        num1, num2 = parse_arguments(args)
        result = multiply_numbers(num1, num2)
        print(f"The product of {num1} and {num2} is {result}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main_driver(sys.argv)
