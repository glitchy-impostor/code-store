
import sys

def sum_of_five_numbers(a, b, c, d, e):
    """
    Function to calculate the sum of five numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    c (int): The third number.
    d (int): The fourth number.
    e (int): The fifth number.
    
    Returns:
    int: The sum of the five numbers.
    """
    return a + b + c + d + e

def main():
    # Check if exactly 5 arguments are provided
    if len(sys.argv) != 6:
        print("Usage: python script.py num1 num2 num3 num4 num5")
        sys.exit(1)
    
    try:
        # Convert command line arguments to integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        num3 = int(sys.argv[3])
        num4 = int(sys.argv[4])
        num5 = int(sys.argv[5])
        
        # Calculate the sum
        result = sum_of_five_numbers(num1, num2, num3, num4, num5)
        
        # Print the result
        print(f"The sum of the five numbers is: {result}")
    
    except ValueError:
        print("All arguments must be integers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
