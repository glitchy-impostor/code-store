
import argparse
from datetime import datetime
import jira
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description='Analyze issues in JIRA and generate a bar chart.')
    
    parser.add_argument('url', type=str, help='JIRA instance URL')
    parser.add_argument('username', type=str, help='JIRA username')
    parser.add_argument('password', type=str, help='JIRA password')
    parser.add_argument('--start_date', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end_date', type=lambda s: datetime.strptime(s, '%Y-%m-%d'), required=True, help='End date (YYYY-MM-DD)')
    
    return parser.parse_args()

def authenticate_jira(url, username, password):
    try:
        jira_options = {'server': url}
        jira_auth = (username, password)
        jira_instance = jira.JIRA(options=jira_options, basic_auth=jira_auth)
        print("Successfully authenticated with JIRA.")
        return jira_instance
    except Exception as e:
        print(f"Failed to authenticate: {e}")
        exit(1)

def fetch_issues(jira_instance, start_date, end_date):
    query = f'resolutionDate >= {start_date.strftime("%Y-%m-%d")} AND resolutionDate <= {end_date.strftime("%Y-%m-%d")}'
    issues = jira_instance.search_issues(query)
    print(f"Found {len(issues)} issues between {start_date} and {end_date}.")
    return issues

def count_issues_per_assignee(issues):
    assignee_counts = {}
    
    for issue in issues:
        if hasattr(issue, 'fields') and issue.fields.assignee is not None:
            assignee_name = issue.fields.assignee.displayName
            if assignee_name not in assignee_counts:
                assignee_counts[assignee_name] = 1
            else:
                assignee_counts[assignee_name] += 1
    
    return assignee_counts

def plot_results(assignee_counts):
    labels, counts = zip(*assignee_counts.items())
    plt.bar(labels, counts)
    plt.xlabel('Assignee')
    plt.ylabel('Number of Completed Tickets')
    plt.title('Completed Tickets by Assignee')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.savefig("figureReturned.png")

if __name__ == "__main__":
    args = parse_args()
    jira_instance = authenticate_jira(args.url, args.username, args.password)
    issues = fetch_issues(jira_instance, args.start_date, args.end_date)
    assignee_counts = count_issues_per_assignee(issues)
    plot_results(assignee_counts)
