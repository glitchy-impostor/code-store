
import sys
from datetime import datetime

def calculate_product(a, b, c):
    """Calculate the product of three numbers."""
    return a * b * c

def get_numbers_from_args(args):
    """Extract three numbers from command line arguments."""
    if len(args) == 4:
        try:
            return [int(arg) for arg in args[1:]]
        except ValueError:
            print("Please provide valid integers as command line arguments.")
            sys.exit(1)
    else:
        print("Usage: python script.py <num1> <num2> <num3>")
        sys.exit(1)

def get_numbers_from_time():
    """Get current time components as numbers."""
    now = datetime.now()
    return [now.hour, now.minute, now.second]

def driver(args):
    """Driver function to execute the program logic."""
    if args:
        nums = get_numbers_from_args(args)
    else:
        nums = get_numbers_from_time()

    product = calculate_product(*nums)
    print(f"The product of {nums} is: {product}")

if __name__ == "__main__":
    driver(sys.argv)
