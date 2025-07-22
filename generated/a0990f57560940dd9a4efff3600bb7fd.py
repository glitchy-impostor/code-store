
import sys

def add_numbers_from_args(args):
    """
    Adds numbers passed as command line arguments.
    Returns 0 if no valid numbers are provided.
    """
    total = 0
    for arg in args:
        try:
            total += float(arg)
        except ValueError:
            # Ignore non-numeric arguments
            continue
    return total

def main(args):
    result = add_numbers_from_args(args)
    print(result)

if __name__ == "__main__":
    # Pass all command line arguments except the script name
    main(sys.argv[1:])
