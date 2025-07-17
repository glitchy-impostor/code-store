
import sys
from datetime import datetime

def parse_numbers(args):
    """Parse command line arguments into a list of integers or use current time as default."""
    if args:
        return [int(arg) for arg in args]
    else:
        now = datetime.now()
        return [now.hour, now.minute, now.second]

def sum_numbers(numbers):
    """Calculate and return the sum of numbers."""
    return sum(numbers)

def driver(args):
    """Driver function to orchestrate the program logic."""
    numbers = parse_numbers(args)
    total_sum = sum_numbers(numbers)
    print(f"The sum is: {total_sum}")

if __name__ == "__main__":
    driver(sys.argv[1:])
