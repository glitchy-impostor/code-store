
import argparse
from jira import JIRA
import datetime as dt
import matplotlib.pyplot as plt

def parse_arguments():
    parser = argparse.ArgumentParser(description="Ticket analysis for the past week from JIRA")
    parser.add_argument('--server', required=True, help='JIRA server URL')
    parser.add_argument('--username', required=True, help='JIRA username')
    parser.add_argument('--token', required=True, help='JIRA API token')
    return parser.parse_args()

def connect_to_jira(args):
    options = {
        'server': args.server
    }
    return JIRA(options, basic_auth=(args.username, args.token))

def get_last_week():
    today = dt.date.today()
    start_date = today - dt.timedelta(days=today.weekday() + 7)
    end_date = start_date + dt.timedelta(days=6)
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')

def fetch_tickets(jira, start_date, end_date):
    jql_query = f"project = NPM AND status in ('Pending', 'Completed') AND created >= '{start_date}' AND created <= '{end_date}'"
    return jira.search_issues(jql_query)

def categorize_tickets(tickets):
    pending = [ticket for ticket in tickets if ticket.fields.status.name != 'Done']
    completed = [ticket for ticket in tickets if ticket.fields.status.name == 'Done']
    return pending, completed

def count_tickets_per_person(tickets):
    from collections import defaultdict
    counts = defaultdict(int)
    for ticket in tickets:
        counts[ticket.fields.reporter.displayName] += 1
    return counts

def plot_results(data):
    people = list(data.keys())
    pending_counts = [data[person]['pending'] if 'pending' in data[person] else 0 for person in people]
    completed_counts = [data[person]['completed'] if 'completed' in data[person] else 0 for person in people]

    x_pos = [i for i, _ in enumerate(people)]
    
    plt.bar(x_pos, pending_counts, color='red', align='center', alpha=0.75, label='Pending')
    plt.bar([x + 0.3 for x in x_pos], completed_counts, color='green', align='center', alpha=0.75, label='Completed')

    plt.xticks(x_pos, people)
    plt.xlabel('Person')
    plt.ylabel('Number of Tickets')
    plt.title('Ticket Status Over the Last Week')
    plt.legend()

    plt.show()
    plt.savefig("saved.png")

def driver_function(args):
    jira = connect_to_jira(args)
    
    start_date, end_date = get_last_week()
    tickets = fetch_tickets(jira, start_date, end_date)
    
    pending, completed = categorize_tickets(tickets)
    
    pending_counts = count_tickets_per_person(pending)
    completed_counts = count_tickets_per_person(completed)

    result = {person: {'pending': pending_counts.get(person, 0), 'completed': completed_counts.get(person, 0)} for person in set(pending_counts) | set(completed_counts)}

    plot_results(result)

if __name__ == "__main__":
    args = parse_arguments()
    driver_function(args)
