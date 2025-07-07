
import sys

def add_numbers(a: int, b: int, c: int) -> int:
    """
    Adds three integers and returns the result.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int: The sum of the three integers.
    """
    return a + b + c

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <num1> <num2> <num3>")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        num3 = int(sys.argv[3])
    except ValueError:
        print("Please provide valid integers.")
        sys.exit(1)

    result = add_numbers(num1, num2, num3)
    print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
