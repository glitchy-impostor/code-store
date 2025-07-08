
import schedule
import time
import requests
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jira import JIRA

# Setup email details
sender_email = 'your_email@example.com'
receiver_email = 'receiver_email@example.com'
password = 'your_password'

def send_mail(subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def get_jira_data():
    jira_options = {'server': 'https://your-jira-url'}
    jira = JIRA(options=jira_options, auth=('username', 'password'))

    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()
    
    worklogs = [worklog for issue in jira.search_issues(jql_query=f"project=YourProject AND updated > {start_date} AND updated < {end_date}") 
                for worklog in issue.fields.worklog.worklogs]
                
    # create a dictionary to store worklog data
    worklog_dict = {'date': [], 'hours': []}
    for log in worklogs:
        worklog_dict['date'].append(log.created)
        worklog_dict['hours'].append(log.timeSpentSeconds/3600)
    
    return worklog_dict

def plot_graph(worklog_data):
    # Use matplotlib or any other library to plot the graph
    pass
    
def send_to_sandbox():
    code = get_jira_data()
    response = requests.post('http://localhost:8000/execute', data=code)
    
    # Send result via email
    send_mail("Result", str(response.content))
    
schedule.every().day.at("10:30").do(send_to_sandbox)

while True:
    schedule.run_pending()
    time.sleep(1)
