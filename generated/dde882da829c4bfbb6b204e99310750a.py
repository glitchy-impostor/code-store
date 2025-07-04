
from datetime import datetime

# Original datetime string
dt_str = "T19:26:48.579+0530"

# Adjust the format string to include microseconds
format_str = "%Y-%m-%dT%H:%M:%S.%f%z"

# Parse the datetime string with the updated format
parsed_dt = datetime.strptime(dt_str, format_str)

print(parsed_dt)
