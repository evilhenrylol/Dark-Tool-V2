import requests
import time
import threading

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def print_banner():
    print("""
                                                       https://discord.gg/MBcQXZPf
                                              ____        _     __             _    _____ 
                                             / __ \____ _(_)___/ /__  _____   | |  / /__ \\
                                            / /_/ / __ `/ / __  / _ \/ ___/   | | / /__/ /
                                           / _, _/ /_/ / / /_/ /  __/ /       | |/ // __/  
                                          /_/ |_|\__,_/_/\__,_/\___/_/        |___//____/ 
                                                    
    """)

def send_message(webhook_url, message, i, delay):
    while True:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print(f"{GREEN}                         [+] Message {i+1} sent successfully!{RESET}")
            break
        elif response.status_code == 429:
            print(f"{RED}                         [-] Rate limited. Waiting before retrying...{RESET}")
            retry_after = int(response.headers.get("Retry-After", 5)) 
            time.sleep(retry_after)
        else:
            print(f"{RED}                         [-] Failed to send message {i+1}. Status Code: {response.status_code}{RESET}")
            break
        
        if delay > 0:
            time.sleep(delay / 1000)  

def send_webhook_message(webhook_url, message, count, delay):
    threads = []
    for i in range(count):
        thread = threading.Thread(target=send_message, args=(webhook_url, message, i, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def main():
    print_banner()
    webhook_url = input("                                           Enter Webhook > ")
    message = input("                                           Enter Message > ")
    count = int(input("                                           How Many Messages > "))
    delay = int(input("                                           Delay (Ms) 0 = no delay > "))
    
    send_webhook_message(webhook_url, message, count, delay)

if __name__ == "__main__":
    main()
