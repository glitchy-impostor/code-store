
import jira
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import argparse

def get_jira_client(username, password, jira_url):
    """Create a JIRA client using basic authentication."""
    return jira.JIRA(options={'server':jira_url}, basic_auth=(username, password))

def get_completed_tickets_in_timeframe(jira_client, project_key, start_date, end_date):
    """Retrieve tickets that were worked on and completed within the given timeframe."""
    query = f'project = {project_key} AND created >="{start_date}" AND created <= "{end_date}" AND status=Done'
    issues = jira_client.search_issues(query)
    return issues

def count_tickets_per_assignee(issues):
    """Count the number of tickets each assignee has completed."""
    ticket_count = {}
    for issue in issues:
        if issue.fields.assignee:
            assignee_name = issue.fields.assignee.displayName
            ticket_count[assignee_name] = ticket_count.get(assignee_name, 0) + 1
    return ticket_count

def plot_ticket_counts(ticket_count):
    """Plot the number of tickets each assignee has completed."""
    names = list(ticket_count.keys())
    counts = list(ticket_count.values())

    plt.figure(figsize=(12, 8))
    plt.bar(names, counts, color='blue')
    plt.xlabel('Assignee Name')
    plt.ylabel('Number of Tickets Closed')
    plt.title('Tickets Completed by Assignee')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('tickets_closed_by_assignee.png')

def driver_function(username, password, jira_url):
    """Driver function to execute the entire process."""
    project_key = 'NPM'
    
    # Calculate the timeframe (last month from today)
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    jira_client = get_jira_client(username, password, jira_url)
    issues = get_completed_tickets_in_timeframe(jira_client, project_key, start_date, end_date)
    ticket_count = count_tickets_per_assignee(issues)
    plot_ticket_counts(ticket_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a graph showing the number of tickets completed by each assignee.")
    parser.add_argument("username", help="JIRA username")
    parser.add_argument("password", help="JIRA password")
    parser.add_argument("jira_url", help="JIRA URL")
    
    args = parser.parse_args()
    driver_function(args.username, args.password, args.jira_url)
