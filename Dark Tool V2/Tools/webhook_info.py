import requests
import json

def get_webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_info = response.json()
            print("Webhook Information:")
            for key, value in webhook_info.items():
                print(f"{key}: {value}")
        else:
            print(f"Error: Received status code {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    webhook_url = input("Enter the webhook URL: ").strip()
    get_webhook_info(webhook_url)
    input("Press Enter to exit...")

