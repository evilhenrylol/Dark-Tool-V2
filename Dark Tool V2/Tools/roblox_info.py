import requests

ROBLOX_COOKIE = input("Enter your Roblox cookie: ").strip()

HEADERS = {
    "Cookie": f".ROBLOSECURITY={ROBLOX_COOKIE}",
    "User-Agent": "Mozilla/5.0"
}

def get_user_info():
    response = requests.get("https://users.roblox.com/v1/users/authenticated", headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return {
            "User ID": data["id"],
            "Username": data["name"],
            "Display Name": data["displayName"]
        }
    else:
        return {"Error": "Failed to get user info. Check your cookie."}

def get_robux():
    response = requests.get("https://economy.roblox.com/v1/user/currency", headers=HEADERS)
    if response.status_code == 200:
        return {"Robux": response.json()["robux"]}
    else:
        return {"Error": "Failed to get Robux balance."}

def get_friends_count(user_id):
    response = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends/count", headers=HEADERS)
    if response.status_code == 200:
        return {"Friends Count": response.json()["count"]}
    else:
        return {"Error": "Failed to get friends count."}

if __name__ == "__main__":
    user_info = get_user_info()
    
    if "User ID" in user_info:
        robux = get_robux()
        friends = get_friends_count(user_info["User ID"])

        print("\n=== Roblox Account Info ===")
        print(f"User ID: {user_info['User ID']}")
        print(f"Username: {user_info['Username']}")
        print(f"Display Name: {user_info['Display Name']}")
        print(f"Robux: {robux.get('Robux', 'N/A')}")
        print(f"Friends: {friends.get('Friends Count', 'N/A')}")
    else:
        print(user_info["Error"])

    input("\nPress Enter to exit...")  
