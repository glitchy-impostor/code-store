
import json

def main(github_url, cmd_send_value, email_address, github_token):
    try:
        file_content = fetch_file_content(github_url, github_token)
        post_url = "http://127.0.0.1:8000/execute"
        payload = {
            'code': file_content,
            'working_directory': None,
            'command_args': cmd_send_value
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
        
        response = requests.post(post_url, data=json.dumps(payload), headers=headers)
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
