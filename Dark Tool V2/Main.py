import os
import time
from colorama import init

init()

ascii_art = """
       \033[35m       
                                    https://discord.gg/MBcQXZPf
        ▄▄▄▄▄▄  ▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄   ▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄           ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
       █      ██      █   ▄  █ █   █ █ █  █       █       █       █   █         █  █ █  █       █
       █  ▄    █  ▄   █  █ █ █ █   █▄█ █  █▄     ▄█   ▄   █   ▄   █   █         █  █▄█  █▄▄▄▄   █    
       █ █ █   █ █▄█  █   █▄▄█▄█      ▄█    █   █ █  █ █  █  █ █  █   █         █       █▄▄▄▄█  █ 
       █ █▄█   █      █    ▄▄  █     █▄     █   █ █  █▄█  █  █▄█  █   █▄▄▄      █       █ ▄▄▄▄▄▄█     
       █       █  ▄   █   █  █ █    ▄  █    █   █ █       █       █       █      █     ██ █▄▄▄▄▄ 
       █▄▄▄▄▄▄██▄█ █▄▄█▄▄▄█  █▄█▄▄▄█ █▄█    █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█       █▄▄▄█ █▄▄▄▄▄▄▄█
       """

menu_items = [
    ["[01] Server Nuker (CMD)   ", "[10] Ip Info        ", "[19] ##########"],
    ["[02] Server Nuker (SELF)  ", "[11] Ip Logger      ", "[20] ##########"],
    ["[03] Webhook Spammer      ", "[12] DDOS Tool      ", "[21] ##########"],
    ["[04] Webhook Deleter      ", "[13] Raider         ", "[22] ##########"],
    ["[05] Webhook Info         ", "[14] Bot Info       ", "[23] ##########"],
    ["[06] Token Checker        ", "[15] ##########     ", "[24] ##########"],
    ["[07] Token Info           ", "[16] ##########     ", "[25] ##########"],
    ["[08] Token Nuker (SOON)   ", "[17] ##########     ", "[26] ##########"],
    ["[09] Roblox Info          ", "[18] ##########     ", "[00] EXIT      "]
]

script_files = {
    "2": "Tools/SELF_Nuker.py",
    "1": "Tools/CMD_Nuker.py",
    "3": "Tools/webhook_spammer.py",
    "4": "Tools/webhook_deleter.py",
    "5": "Tools/webhook_info.py",
    "6": "Tools/token_checker.py",
    "7": "Tools/token_info.py",
    "8": "Tools/token_nuker.py",
    "9": "Tools/roblox_info.py",
    "10": "Tools/ip_info.py",
    "11": "Tools/ip_logger.py",
    "12": "Tools/ddos_tool.py",
    "13": "Tools/Raider/raider.py",
    "14": "Tools/bot_info.py"
}

def get_gradient_color(index, total):
    ratio = index / total
    r = int(191 + (255 - 191) * ratio)
    g = int(64 + (255 - 64) * ratio)
    b = int(191 + (255 - 191) * ratio)
    return f"\033[38;2;{r};{g};{b}m"

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("title Dark Tool V2 - BETA")
    print(ascii_art)
    
    total_items = sum(len(row) for row in menu_items)
    index = 0
    spacing = "       "

    for row in menu_items:
        for item in row:
            color = get_gradient_color(index, total_items - 1)
            print(f"{spacing}{color}{item}", end=" ")
            index += 1
        print()

    print("\033[0m")  

def main():
    while True:
        print_menu()
        choice = input("\nEnter option: ").strip()

        if choice == "0":
            print("Exiting...")
            break
        
        if choice in script_files:
            script_path = script_files[choice]
            if os.path.exists(script_path):
                os.system(f"python {script_path}")
            else:
                print(f"\033[31mError: {script_path} not found!\033[0m")
        else:
            print("\033[31mInvalid option!\033[0m")
        
        time.sleep(2)

if __name__ == "__main__":
    main()


