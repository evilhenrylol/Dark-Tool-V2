import time
import requests
import os
import threading

script_dir = os.path.dirname(os.path.abspath(__file__))
tokens_path = os.path.join(script_dir, "tokens.txt")

with open(tokens_path, "r") as file:
    tokens = [line.strip() for line in file.readlines()]

channel_id = input("Enter Channel ID: ")
message = input("Enter Message: ")
delay = int(input("Enter Delay (ms): ")) / 1000
count = int(input("Enter Number of Messages per Token: "))

url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

data = {"content": message}

def send_messages(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    for _ in range(count):
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Message sent successfully using token {token[:10]}...")
        else:
            print(f"Failed to send message with token {token[:10]}: {response.text}")
        time.sleep(delay)

threads = []
for token in tokens:
    thread = threading.Thread(target=send_messages, args=(token,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

input("Press Enter to exit...")
