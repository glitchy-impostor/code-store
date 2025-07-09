
import requests
import smtplib
from email.mime.text import MIMEText

def get_worklog_graph():
    # Code to connect to JIRA and retrieve worklogs between two dates
    pass

def plot_worklog_graph(worklogs):
    # Code to plot the graph of worklogs
    pass

def send_email(body):
    msg = MIMEText(body)
    msg['Subject'] = 'Worklog Graph'
    msg['From'] = 'krishtshah21@outlook.com'
    msg['To'] = 'krish.shah@whiteklay.com'
    email = "krishtshah21@outlook.com"
    passkey="Shah#1234"
    rcvr = "krish.shah@whiteklay.com"
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
        server.starttls()
        server.login(email, passkey)
        server.sendmail(email, rcvr,msg.as_string())

def run_sandbox_code(code, *args):
    url = "http://localhost:8000/execute"
    payload = {'code': code, 'command_args': args}
    response = requests.post(url, json=payload)
    result = response.json()
    output_text = "Output: " + result['output'] + "\n\n"
    output_text += "Execution ID: " + str(result['execution_id']) + "\n\n"
    files_ = result['generated_files']
    if(len(files_)>0):
        output_text += "Files Generated: \n"
    else:
        output_text += "Files Generated: None"
    for file_ in files_:
        output_text += file_ + " Located at: http://127.0.0.1:8000/download/" + result['execution_id'] + "/" + file_ + " \n"
    return output_text

#if __name__ == '__main__':
    
graph_code = '''import jira
from datetime import datetime
import matplotlib.pyplot as plt

# Function to fetch worklogs from JIRA between two dates
def get_worklogs(jira_client, start_date, end_date):
    issues = jira_client.search_issues(f'worklogDate >= "{start_date}" AND worklogDate <= "{end_date}"')
    worklogs = {}
    i=0
    for issue in issues:
        i+=1

        if hasattr(issue, 'fields') and issue.fields.assignee is not None:
            assignee_name = issue.fields.assignee.displayName
            if assignee_name not in worklogs:
                worklogs[assignee_name] = 1
            else:
                worklogs[assignee_name] += 1
    print(i)
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
    jira_url = 'https://whiteklay-tech.atlassian.net'
    username = 'rishikesh.kumar@whiteklay.in'
    api_token = 'ATATT3xFfGF0OX9wDe6uyJjiXlsHJChtimXHeoKmZls1zXSd7lIaTL0Qhl-e7Jn13wY228mud5iUy7Rug8YJYIsSqJdTdLNnVcb1l24WLL7CjRV8kMjCNldEuqtmjqLkzZkzODuQlIGRebP0n3lIlbgGSgdbOe1r'

    # Create JIRA client
    jira_client = jira.JIRA(jira_url, auth=(username, api_token))

    # Get worklogs for the last month
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Fetch worklogs and create bar chart
    worklogs = get_worklogs(jira_client, start_date, end_date)
    create_bar_chart(worklogs)

# Run the main function
if __name__ == '__main__':
    main()
'''

    
result = run_sandbox_code(graph_code, '')

email_body = 'Worklog graph data: {}'.format(result)
send_email(email_body)
