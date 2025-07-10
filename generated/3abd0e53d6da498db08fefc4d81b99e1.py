
import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

def execute_code(code, command_args):
    """Sandbox the code and send a POST request to execute it."""
    url = "http://127.0.0.1:8000/execute"
    payload = {
        'code': code,
        'command_args': command_args,
        'working_directory': None
    }
    response = requests.post(url, json=payload)
    result = response.json()
    try:
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
    except:
        return str(result)
def send_email(subject, body, to_email):
    """Send an email via Gmail's SMTP server."""
    from_email = "oracleofodes@gmail.com"
    password = "viaa ijtk xnlg nkdj"  # Be careful with storing passwords in code

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

def driver_function(code, command_args, schedule_time, recipient_email):
    """
    Driver function to handle scheduling and executing the code.
    
    :param code: str, the code string to execute
    :param command_args: str, any additional command arguments for the code
    :param schedule_time: int, the time in seconds from now to schedule the execution
    :param recipient_email: str, the email address to send the results to
    """
    # Schedule the code execution
    scheduler = BackgroundScheduler()
    loop_control = True
    def job_func():
        #print("True")
        result = execute_code(code, command_args)
        send_email("Code Execution Result", result, recipient_email)
        #print("sent")
        loop_control=False

    run_date = datetime.fromtimestamp(time.time() + schedule_time)
    scheduler.add_job(job_func, 'date', run_date=run_date)
    scheduler.start()
    while(loop_control):
        time.sleep(1)

def recurring_driver_function(code, command_args, interval, recipient_email):
    """
    Driver function to handle recurring scheduling and executing the code.
    
    :param code: str, the code string to execute
    :param command_args: str, any additional command arguments for the code
    :param interval: int, the time in seconds between each execution
    :param recipient_email: str, the email address to send the results to
    """
    # Schedule the code execution
    scheduler = BackgroundScheduler()
    loop_control = True
    def job_func():
        #print("entry")
        result = execute_code(code, command_args)
        send_email("Code Execution Result", result, recipient_email)
        loop_control=False

    scheduler.add_job(job_func, 'interval', seconds=interval)
    scheduler.start()
    while(loop_control):
        time.sleep(1)
    #print("in")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Schedule code execution.')
    parser.add_argument('--code', type=str, default="print('Hello World')", help='Code to execute')
    parser.add_argument('--command_args', type=str, default='', help='Command arguments for the code')
    parser.add_argument('--schedule_time', type=int, default=5, help='Time in seconds from now to schedule the execution')
    parser.add_argument('--recipient_email', type=str, default="krishtshah21@gmail.com", help='Email address to send the results to')
    
    args = parser.parse_args()
    
    if args.schedule_time > 0:
        print(args.code, args.schedule_time)
        driver_function(args.code, args.command_args, args.schedule_time, args.recipient_email)
    else:
        recurring_driver_function(args.code, args.command_args, -args.schedule_time, args.recipient_email)
