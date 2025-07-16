
import sys

def parse_arguments(args):
    """
    Parses command line arguments and returns three integers.
    
    Parameters:
        args (list): A list of command line arguments.
        
    Returns:
        tuple: Three integers parsed from the command line arguments.
    """
    if len(args) != 4:
        raise ValueError("Usage: python multiply.py <num1> <num2> <num3>")
    return int(args[1]), int(args[2]), int(args[3])

def multiply_numbers(num1, num2, num3):
    """
    Multiplies three integers.
    
    Parameters:
        num1 (int): The first integer.
        num2 (int): The second integer.
        num3 (int): The third integer.
        
    Returns:
        int: The product of the three integers.
    """
    return num1 * num2 * num3

def main_driver(args):
    """
    Driver function to execute the multiplication of three numbers.
    
    Parameters:
        args (list): A list of command line arguments.
    """
    try:
        num1, num2, num3 = parse_arguments(args)
        result = multiply_numbers(num1, num2, num3)
        print(f"The product of {num1}, {num2}, and {num3} is {result}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main_driver(sys.argv)
