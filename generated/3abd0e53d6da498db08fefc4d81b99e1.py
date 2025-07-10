
import time
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def execute_code(code, command_args):
    """Sandbox the code and send a POST request to execute it."""
    url = "http://localhost:8000/execute"
    payload = {
        'code': code,
        'command_args': command_args
    }
    response = requests.post(url, json=payload)
    result = response.json()
    
    output_text = "Output: " + result['output'] + "\n\n"
    output_text += "Execution ID: " + str(result['execution_id']) + "\n\n"
    files_ = result['generated_files']
    if(len(files_) > 0):
        output_text += "Files Generated: \n"
    else:
        output_text += "Files Generated: None"
    for file_ in files_:
        output_text += file_ + " Located at: http://127.0.0.1:8000/download/" + result['execution_id'] + "/" + file_ + " \n"
    
    return output_text

def send_email(subject, body, to_email):
    """Send an email via Gmail's SMTP server."""
    from_email = "your-email@gmail.com"
    password = "your-password"  # Be careful with storing passwords in code

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def driver_function(code, command_args, schedule_time):
    """
    Driver function to handle scheduling and executing the code.
    
    :param code: str, the code string to execute
    :param command_args: str, any additional command arguments for the code
    :param schedule_time: int, the time in seconds from now to schedule the execution
    """
    # Schedule the code execution
    scheduler = BackgroundScheduler()
    scheduler.add_job(execute_code, 'date', run_date=time.time() + schedule_time, args=[code, command_args], callback=lambda x: send_email("Code Execution Result", str(x), "recipient@example.com"))
    scheduler.start()

def recurring_driver_function(code, command_args, interval):
    """
    Driver function to handle recurring scheduling and executing the code.
    
    :param code: str, the code string to execute
    :param command_args: str, any additional command arguments for the code
    :param interval: int, the time in seconds between each execution
    """
    # Schedule the code execution
    scheduler = BackgroundScheduler()
    scheduler.add_job(execute_code, 'interval', seconds=interval, args=[code, command_args], callback=lambda x: send_email("Code Execution Result", str(x), "recipient@example.com"))
    scheduler.start()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Schedule and execute code.")
    subparsers = parser.add_subparsers(dest='command')

    # Command for one-time scheduling
    schedule_parser = subparsers.add_parser('schedule', help="Schedule a one-time execution of the code")
    schedule_parser.add_argument('code', type=str, help='The code string to execute')
    schedule_parser.add_argument('command_args', type=str, help='Any additional command arguments for the code')
    schedule_parser.add_argument('schedule_time', type=int, help='Time in seconds from now to schedule the execution (between 60 and 604800)')

    # Command for recurring scheduling
    recurring_parser = subparsers.add_parser('recurring', help="Schedule a recurring execution of the code")
    recurring_parser.add_argument('code', type=str, help='The code string to execute')
    recurring_parser.add_argument('command_args', type=str, help='Any additional command arguments for the code')
    recurring_parser.add_argument('interval', type=int, help='Time in seconds between each execution (between 60 and 604800)')

    args = parser.parse_args()

    if args.command == 'schedule':
        driver_function(args.code, args.command_args, args.schedule_time)
    elif args.command == 'recurring':
        recurring_driver_function(args.code, args.command_args, args.interval)
