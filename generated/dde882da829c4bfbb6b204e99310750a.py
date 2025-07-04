
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from jira import JIRA

# JIRA credentials and configuration
jira_url = 'https://whiteklay-tech.atlassian.net'
username = 'rishikesh.kumar@whiteklay.in'
api_token = ''  # You can generate an API token from your JIRA account settings

# Project key
project_key = 'NPM'

# Dates
start_date = datetime(2025, 6, 3)
end_date = datetime(2025, 7, 3)

# Connect to JIRA
auth = (username, api_token)
jira_options = {'server': jira_url}
jira = JIRA(options=jira_options, basic_auth=auth)

# Fetch worklogs for the project between the given dates
worklog_issues = []
for issue in jira.search_issues(f'project={project_key} AND worklogDate >= {start_date.strftime("%Y-%m-%d")} AND worklogDate <= {end_date.strftime("%Y-%m-%d")}', maxResults=None):
    for worklog in issue.fields.worklog.worklogs:
        if start_date <= datetime.strptime(worklog.started, '%Y-%m-%d') <= end_date:
            worklog_issues.append({
                'issue_key': issue.key,
                'started': datetime.strptime(worklog.started, '%Y-%m-%dT%H:%M:%S.%f%z'),
                'time_spent_seconds': worklog.timeSpentSeconds
            })

# Convert the data into a pandas DataFrame for easier processing and plotting
df = pd.DataFrame(worklog_issues)
df['date'] = df['started'].dt.date

# Group by date to get the number of issues worked on each day
daily_workload = df.groupby('date').size().reset_index(name='num_issues')

# Plotting the data
plt.figure(figsize=(12, 6))
plt.bar(daily_workload['date'], daily_workload['num_issues'], color='skyblue')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Issues Completed', fontsize=14)
plt.title('Worklog Completion by Date for Project NPM', fontsize=18)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('workload_vs_date.png')

print("Graph saved as 'workload_vs_date.png'")
