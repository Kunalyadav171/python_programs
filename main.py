import webbrowser

site_name = input("Enter site name: ").lower()

sites = [
    ["youtube" , "https:/www.youtube.com"],
    ["google" , "https:/www.google.com"],
    ["monkeytype" , "https:/www.monkeytype.com"]
]

site_found = True

for site in sites:
    if site[0] == site_name:
        print(f"Opening {site_name}")
        webbrowser.open(site[1])
        # site_found = True
        break
    
if not site_found:
    print("Site not found.")