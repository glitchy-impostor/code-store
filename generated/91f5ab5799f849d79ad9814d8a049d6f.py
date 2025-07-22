
import sys

def calculate_mean(numbers):
    """
    Calculate the mean of a list of numbers.
    
    If the list is empty or contains only zeros, return 0.
    Otherwise, return the sum of the numbers divided by their count.
    
    :param numbers: List of integers or floats
    :return: Mean of the numbers as a float
    """
    if not numbers or all(num == 0 for num in numbers):
        return 0.0
    return sum(numbers) / len(numbers)

def driver_function(*args):
    """
    Driver function to handle command line arguments and calculate the mean.
    
    :param args: Command line arguments (expected to be numbers)
    """
    try:
        # Convert command line arguments to floats
        numbers = [float(arg) for arg in args]
        
        # Calculate the mean
        mean_value = calculate_mean(numbers)
        
        # Print the result
        print(f"The mean is: {mean_value}")
    
    except ValueError as e:
        print(f"Error: All inputs must be valid numbers. {e}", file=sys.stderr)

# Call the driver function with command line arguments (excluding the script name)
if __name__ == "__main__":
    driver_function(*sys.argv[1:])
