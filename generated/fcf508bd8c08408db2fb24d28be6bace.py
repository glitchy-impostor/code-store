
import sys

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.
    
    Returns:
    int/float: The sum of the two numbers.
    """
    return a + b

def main(args):
    """
    Driver function to handle command line arguments and call the add_numbers function.
    
    Parameters:
    args (list[str]): Command line arguments, excluding the script name.
    
    Usage:
    python script.py 5 3
    This will output: 8
    """
    if len(args) != 2:
        print("Usage: python script.py <number1> <number2>")
        sys.exit(1)
    
    try:
        num1 = float(args[0])
        num2 = float(args[1])
        
        result = add_numbers(num1, num2)
        print(f"The sum is: {result}")
    
    except ValueError:
        print("Please provide valid numbers as arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
