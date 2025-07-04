
import sys

def add_numbers(a, b, c):
    """Add three numbers."""
    return a + b + c

def multiply_numbers(a, b, c):
    """Multiply three numbers."""
    return a * b * c

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <number1> <number2> <number3>")
        sys.exit(1)
    
    try:
        # Convert command line arguments to integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        num3 = int(sys.argv[3])
        
        # Calculate the sum and product
        total_sum = add_numbers(num1, num2, num3)
        total_product = multiply_numbers(num1, num2, num3)
        
        # Display the results
        print(f"The sum of {num1}, {num2}, and {num3} is: {total_sum}")
        print(f"The product of {num1}, {num2}, and {num3} is: {total_product}")
    
    except ValueError:
        print("All arguments must be integers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
