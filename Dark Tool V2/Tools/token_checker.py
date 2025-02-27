import requests
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def check_token(token):
    headers = {"Authorization": token}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    
    if response.status_code == 200:
        print(Fore.GREEN + "Token is valid!")
    else:
        print(Fore.RED + "Token is invalid!")
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    token = input("Enter Token: ")
    check_token(token)
