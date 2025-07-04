
import sys

def add_numbers(a, b, c, d):
    """Add four numbers."""
    return a + b + c + d

def multiply_numbers(a, b, c, d):
    """Multiply four numbers."""
    return a * b * c * d

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <number1> <number2> <number3> <number4>")
        sys.exit(1)
    
    try:
        # Convert command line arguments to integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        num3 = int(sys.argv[3])
        num4 = int(sys.argv[4])
        
        # Calculate the sum and product
        total_sum = add_numbers(num1, num2, num3, num4)
        total_product = multiply_numbers(num1, num2, num3, num4)
        
        # Display the results
        print(f"The sum of {num1}, {num2}, {num3}, and {num4} is: {total_sum}")
        print(f"The product of {num1}, {num2}, {num3}, and {num4} is: {total_product}")
    
    except ValueError:
        print("All arguments must be integers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
