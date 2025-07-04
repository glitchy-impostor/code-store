
from jira import JIRA
import matplotlib.pyplot as plt
from datetime import timedelta, datetime

# Connect to Jira
jira = JIRA('your_jira_url', basic_auth=('username', 'password'))

# Define start date and end date
start_date = '2023-10-01'  # Replace with your actual start date
end_date = '2023-10-31'    # Replace with your actual end date

# Fetch all tickets between the given dates
issues = jira.search_issues(f'created >= "{start_date}" AND created <= "{end_date}"')

# Create a dictionary to store number of issues per day
date_dict = {}

for issue in issues:
    date = issue.fields.created.date()
    if date not in date_dict:
        date_dict[date] = 1
    else:
        date_dict[date] += 1

# Convert date_dict to sorted list of tuples (date, count)
sorted_date_list = sorted(date_dict.items())

# Extract dates and counts into separate lists
dates = [x[0] for x in sorted_date_list]
counts = [x[1] for x in sorted_date_list]

# Plot data
plt.figure(figsize=(12, 6))
plt.plot(dates, counts, marker='o', linestyle='-', color='b')

# Format x-axis labels to be readable
date_format = '%m-%d'
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter(date_format))

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Number of tickets worked on')
plt.title('Number of Jira tickets worked on per day')

# Set the x-axis limits to match the dates
ax.set_xlim(min(dates), max(dates))

plt.show()
