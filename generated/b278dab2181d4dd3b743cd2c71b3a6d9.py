
import sys

def calculate_mean(numbers):
    """
    Calculates the mean of a list of numbers.
    
    :param numbers: List of numbers (integers or floats)
    :return: Mean of the numbers as a float. Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def driver_function(args):
    """
    Driver function to calculate the mean of entered numbers from command line arguments.
    
    :param args: Command line arguments excluding the script name
    """
    # Convert command line arguments to a list of floats
    numbers = [float(arg) for arg in args]
    
    # Calculate and print the mean
    mean = calculate_mean(numbers)
    print(f"The mean is: {mean}")

if __name__ == "__main__":
    driver_function(sys.argv[1:])
