
import sys

def add_three_numbers(a: int, b: int, c: int) -> int:
    """
    Adds three integers together.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        int: The sum of the three numbers.
    """
    return a + b + c

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <number1> <number2> <number3>")
        sys.exit(1)
    
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        num3 = int(sys.argv[3])
        
        result = add_three_numbers(num1, num2, num3)
        print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
    except ValueError:
        print("Please ensure all arguments are valid integers.")
        sys.exit(1)
