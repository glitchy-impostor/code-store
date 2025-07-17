
import argparse
from typing import Tuple, Optional
import time

def divide_product_by_sum(numbers: Tuple[int, int, int]) -> float:
    """
    Divides the product of three numbers by their sum.
    
    Args:
        numbers (Tuple[int, int, int]): A tuple containing three integers.
        
    Returns:
        float: The result of dividing the product by the sum of the numbers.
        
    Raises:
        ValueError: If the sum of the numbers is zero.
    """
    product = numbers[0] * numbers[1] * numbers[2]
    sum_of_numbers = sum(numbers)
    
    if sum_of_numbers == 0:
        raise ValueError("Cannot divide by zero")

    return product / sum_of_numbers

def get_numbers() -> Tuple[int, int, int]:
    """
    Retrieves numbers from command line arguments or current time components.
    
    Returns:
        Tuple[int, int, int]: A tuple containing three integers.
        
    Raises:
        SystemExit: If no valid input is provided.
    """
    parser = argparse.ArgumentParser(description='Get numbers from command line or current time.')
    parser.add_argument('--hour', type=int, help='Use hour as one of the numbers')
    parser.add_argument('--minute', type=int, help='Use minute as one of the numbers')
    parser.add_argument('--second', type=int, help='Use second as one of the numbers')

    args = parser.parse_args()

    if (args.hour is None) and (args.minute is None) and (args.second is None):
        current_time = time.localtime()
        return (current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
    else:
        return (args.hour, args.minute, args.second) if all([args.hour, args.minute, args.second]) else None

def driver_function(hour: Optional[int] = None, minute: Optional[int] = None, second: Optional[int] = None):
    """
    Driver function to call other functions and handle errors.
    
    Args:
        hour (Optional[int]): The hour component to use as a number.
        minute (Optional[int]): The minute component to use as a number.
        second (Optional[int]): The second component to use as a number.
        
    Returns:
        dict: A dictionary containing the result or error message.
    """
    numbers = get_numbers()

    if numbers is None or len(numbers) != 3:
        return {"error": "Invalid input. Please provide exactly three numbers."}

    try:
        result = divide_product_by_sum(numbers)
        return {"result": result}
    except ValueError as e:
        return {"error": str(e)}

# Example usage of the driver function
if __name__ == "__main__":
    result = driver_function(2, 3, 4)  # Replace with actual arguments if running from script
    print(result)
