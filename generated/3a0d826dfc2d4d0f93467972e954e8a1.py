
# Import necessary libraries
import jira
from datetime import datetime
import matplotlib.pyplot as plt

# Function to fetch worklogs from JIRA between two dates
def get_worklogs(jira_client, start_date, end_date):
    issues = jira_client.search_issues(f'worklogDate >= "{start_date}" AND worklogDate <= "{end_date}"')
    worklogs = {}
    for issue in issues:
        for comment in issue.fields.comment.comments:
            if 'Work logged' in comment.body:
                user = comment.author.displayName
                if user not in worklogs:
                    worklogs[user] = 1
                else:
                    worklogs[user] += 1
    return worklogs

# Function to create and save a bar chart of worklogs
def create_bar_chart(worklogs):
    users = list(worklogs.keys())
    issues_completed = list(worklogs.values())

    plt.figure(figsize=(10, 6))
    plt.bar(users, issues_completed, color='skyblue')
    plt.xlabel('Individuals')
    plt.ylabel('Number of Issues Completed')
    plt.title('Worklog Completion by Individuals')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('worklog_completion.png')

# Main function to execute the process
def main():
    # JIRA credentials and URL
    jira_url = 'https://your-jira-instance.atlassian.net'
    username = 'your-email@example.com'
    api_token = 'your-api-token'

    # Create JIRA client
    jira_client = jira.JIRA(jira_url, auth=(username, api_token))

    # Define date range
    start_date = datetime(2023, 1, 1).strftime('%Y-%m-%d')
    end_date = datetime(2023, 12, 31).strftime('%Y-%m-%d')

    # Get worklogs between the specified dates
    worklogs = get_worklogs(jira_client, start_date, end_date)

    # Create and save bar chart
    create_bar_chart(worklogs)

# Run the main function
if __name__ == '__main__':
    main()
