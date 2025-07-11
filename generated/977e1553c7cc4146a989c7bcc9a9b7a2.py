
import os
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def driver_function(code_details):
    """
    This function represents the driver function that should be called instead of running a code string in a sandbox.
    
    :param code_details: Dictionary containing details about the code to be executed
    :return: A tuple (details, files) where 'details' is a dictionary with logged information and 'files' is a list of file paths
    """
    # Example driver function logic
    details = {
        "status": "success",
        "message": "Code execution completed successfully"
    }
    
    files = [
        "/path/to/output1.txt",
        "/path/to/output2.csv"
    ]
    
    return details, files

def send_email(body):
    """
    Send an email with the given body.

    :param body: The content of the email
    """
    msg = MIMEMultipart()
    msg['From'] = 'your-email@example.com'
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'Code Execution Results'

    msg.attach(MIMEText(body, 'plain'))

    # Send the email (this part depends on your email setup)
    import smtplib
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(msg['From'], "your-password")
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'], text)
    server.quit()

def execute_code(code_details):
    """
    Execute the code and send an email with the results.

    :param code_details: Dictionary containing details about the code to be executed
    :return: The same as the original execute_code function
    """
    # Call the driver function directly
    details, files = driver_function(code_details)
    
    # Log the details
    logger.info("Code Execution Details:")
    for key, value in details.items():
        logger.info(f"{key}: {value}")
    
    # Build the email body
    email_body = f"Code Execution Results:\n"
    for key, value in details.items():
        email_body += f"{key}: {value}\n\n"
    
    # Add file paths to the email body
    if files:
        email_body += "Generated Files:\n"
        for file_path in files:
            email_body += f"- {file_path}\n"
    
    # Send the email
    send_email(email_body)
    
    return details, files

# Example usage
code_details = {
    "code": "print('Hello, world!')"
}

execute_code(code_details)
