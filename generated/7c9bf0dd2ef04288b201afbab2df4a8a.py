
import random

def main():
    # Generate random numbers
    number1 = random.randint(7, 21)
    number2 = random.randint(3, 8)

    # Calculate the sum of the two numbers
    result = number1 + number2

    # Display the result
    print(f"The sum of {number1} and {number2} is: {result}")

if __name__ == "__main__":
    main()
