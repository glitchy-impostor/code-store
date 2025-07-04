
from datetime import datetime

# Assuming 'input_string' is the string you want to parse
input_string = "T19:26:48.579+0530"

# Update the format string to match the input string's structure
format_string = "%H:%M:%S.%f%z"

try:
    parsed_datetime = datetime.strptime(input_string, format_string)
    print("Parsed datetime:", parsed_datetime)
except ValueError as e:
    print(f"Error parsing datetime: {e}")
