
import argparse
from datetime import datetime
import jira
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description='Analyze completed issues in JIRA and generate a bar chart.')
    
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

def fetch_completed_issues(jira_instance, start_date, end_date):
    query = f'closed >= {start_date.strftime("%Y-%m-%d")} AND closed <= {end_date.strftime("%Y-%m-%d")}'
    issues = jira_instance.search_issues(query)
    print(f"Found {len(issues)} completed issues between {start_date} and {end_date}.")
    return issues

def count_completed_issues_per_assignee(completed_issues):
    assignee_counts = {}
    
    for issue in completed_issues:
        if hasattr(issue, 'fields') and issue.fields.assignee is not None:
            assignee_name = issue.fields.assignee.displayName
            if assignee_name not in assignee_counts:
                assignee_counts[assignee_name] = 1
            else:
                assignee_counts[assignee_name] += 1
    
    return assignee_counts

def plot_and_save(completed_assignee_counts, start_date, end_date):
    labels = list(completed_assignee_counts.keys())
    values = list(completed_assignee_counts.values())
    
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values, color='skyblue')
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
    
    ax.set_xlabel('Assignee')
    ax.set_ylabel('Number of Completed Issues')
    ax.set_title(f'Completed Issues Between {start_date.strftime("%Y-%m-%d")} and {end_date.strftime("%Y-%m-%d")}')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    output_filename = f"completed_issues_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved as {output_filename}")

def main():
    args = parse_args()
    
    jira_instance = authenticate_jira(args.url, args.username, args.password)
    completed_issues = fetch_completed_issues(jira_instance, args.start_date, args.end_date)
    completed_assignee_counts = count_completed_issues_per_assignee(completed_issues)
    
    plot_and_save(completed_assignee_counts, args.start_date, args.end_date)

if __name__ == "__main__":
    main()
