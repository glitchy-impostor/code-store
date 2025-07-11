
import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import requests

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

def run_code_and_driver(code, driver_function, command_args, schedule_time, recipient_email):
    """
    Generic function to handle scheduling and executing the code.
    
    :param code: str, the code string to execute
    :param driver_function: callable, a function that takes the result of code execution and sends an email with it
    :param command_args: str, any additional command arguments for the code
    :param schedule_time: int, the time in seconds from now to schedule the execution
    :param recipient_email: str, the email address to send results to
    """
    # Schedule the code execution
    scheduler = BackgroundScheduler()
    run_date = datetime.fromtimestamp(time.time() + schedule_time)
    job = scheduler.add_job(execute_code, 'date', run_date=run_date, args=[code, command_args], id="execute_job")
    
    def callback(x):
        driver_function(x, recipient_email)  # Call the driver function with the result and email

    if job:
        job.add_listener(callback, events=['completed'])
    scheduler.start()

def driver_function(result, recipient_email):
    """
    Driver function to handle sending results via email.
    
    :param code: str, the code string
    :param result: dict, the result of code execution
    :param recipient_email: str, the email address to send results to
    """
    subject = "Code Execution Result"
    body = f"Output: {result['output']}\n\nExecution ID: {result['execution_id']}\n\nFiles Generated:\n{', '.join(result.get('generated_files', []))}"
    send_email(subject, body, recipient_email)

def recurring_driver_function(code, driver_function, command_args, interval, recipient_email):
    """
    Generic function to handle recurring scheduling and executing the code.
    
    :param code: str, the code string to execute
    :param driver_function: callable, a function that takes the result of code execution and sends an email with it
    :param command_args: str, any additional command arguments for the code
    :param interval: int, the interval in seconds between executions
    :param recipient_email: str, the email address to send results to
    """
    # Schedule the recurring code execution
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(execute_code, 'interval', seconds=interval, args=[code, command_args], id="execute_job")
    
    def callback(x):
        driver_function(x, recipient_email)  # Call the driver function with the result and email

    if job:
        job.add_listener(callback, events=['completed'])
    scheduler.start()

# Example usage
if __name__ == "__main__":
    code = "print('Hello, World!')"
    command_args = ""
    recipient_email = "recipient@example.com"
    
    run_code_and_driver(code, driver_function, command_args, 10, recipient_email)
