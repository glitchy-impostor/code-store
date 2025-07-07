
import argparse
from github import Github
import requests
import smtplib
from email.mime.text import MIMEText

def fetch_file_content(github_url, github_token):
    g = Github(github_token)
    repo_name = github_url.split('/')[-2]
    file_path = '/'.join(github_url.split('/')[-1].split('/')[:-1])
    
    try:
        repo = g.get_repo(repo_name)
        content = repo.get_contents(file_path)
        return content.decoded_content.decode('utf-8')
    except Exception as e:
        raise Exception(f"Failed to fetch file from GitHub: {e}")

def send_result_via_email(result, email_address):
    sender_email = "your-email@example.com"
    receiver_email = email_address
    password = "your-email-password"

    message = MIMEText(result)
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Sandbox Execution Result"

    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def main(github_url, cmd_send_value, email_address, github_token):
    try:
        file_content = fetch_file_content(github_url, github_token)
        post_url = "https://example.com/sandbox"
        payload = {
            'code': file_content,
            'command': cmd_send_value
        }
        
        response = requests.post(post_url, data=payload)
        if response.status_code == 200:
            result = response.text
            send_result_via_email(result, email_address)
            print("Result sent via email successfully.")
        else:
            print(f"Failed to send code to sandbox: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process GitHub file and send result via email.")
    parser.add_argument("github_url", type=str, help="URL of the GitHub file to fetch")
    parser.add_argument("cmd_send_value", type=str, help="Command value to be sent to the sandbox")
    parser.add_argument("email_address", type=str, help="Email address to send the result to")
    parser.add_argument("github_token", type=str, help="GitHub token for authentication")
    
    args = parser.parse_args()
    main(args.github_url, args.cmd_send_value, args.email_address, args.github_token)
