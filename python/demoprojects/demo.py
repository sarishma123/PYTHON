import requests

username = input("Enter the username to look up: ")

websites = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Instagram": "https://www.instagram.com/{}/"  # Added a trailing slash which helps with Instagram
}

# This header tells the website that the request is coming from a normal web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"\nSearching for '{username}' across websites...\n" + "-"*40)

for site_name, url_template in websites.items():
    target_url = url_template.format(username)
    
    try:
        # We pass the headers here so the website thinks we are using Chrome
        response = requests.get(target_url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            print(f"[+] ACTIVE on {site_name}: {target_url}")
        elif response.status_code == 404:
            print(f"[-] Not found on {site_name}")
        else:
            print(f"[?] Uncertain on {site_name} (Status Code: {response.status_code})")
            
    except requests.exceptions.RequestException:
        print(f"[!] Could not connect to {site_name} (Timeout or Connection Error)")