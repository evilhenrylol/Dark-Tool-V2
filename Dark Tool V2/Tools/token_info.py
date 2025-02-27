import requests

DISCORD_TOKEN = input("Enter your Discord token: ").strip()

HEADERS = {
    "Authorization": DISCORD_TOKEN,
    "User-Agent": "Mozilla/5.0"
}

def get_user_info():
    response = requests.get("https://discord.com/api/v9/users/@me", headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return {
            "User ID": data["id"],
            "Username": data["username"],
            "Display Name": data.get("global_name", "N/A")  
        }
    else:
        return {"Error": "Failed to get user info."}

def get_nitro():
    response = requests.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return "Nitro Active" if data else "No Nitro"
    else:
        return "Failed to get Nitro status."

def get_friends_count():
    response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=HEADERS)
    if response.status_code == 200:
        return len(response.json())
    else:
        return "Failed to get friends count."

def get_servers():
    response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=HEADERS)
    if response.status_code == 200:
        servers = response.json()
        return [f"{server['name']} ({server['id']})" for server in servers]
    else:
        return ["Failed to get servers."]

if __name__ == "__main__":
    user_info = get_user_info()
    nitro_status = get_nitro()
    friends_count = get_friends_count()
    servers = get_servers()

    print("\n=== Discord Account Info ===")
    if "Error" in user_info:
        print(user_info["Error"])
    else:
        print(f"User ID: {user_info['User ID']}")
        print(f"Username: {user_info['Username']}")
        print(f"Display Name: {user_info['Display Name']}")
    print(f"Nitro Status: {nitro_status}")
    print(f"Friends Count: {friends_count}")

    print("\n=== Servers You're In ===")
    for server in servers:
        print(server)

    input("\nPress Enter to exit...")  
