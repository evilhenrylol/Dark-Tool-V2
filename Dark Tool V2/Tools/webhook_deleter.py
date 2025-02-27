import requests

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("Webhook deleted successfully!")
    else:
        print(f"Failed to delete webhook. Status Code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    webhook_url = input("Enter Webhook URL: ")
    delete_webhook(webhook_url)
