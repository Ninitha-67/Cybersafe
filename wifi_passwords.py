import subprocess

def get_wifi_passwords():
    networks = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
    profiles = [line.split(":")[1].strip() for line in networks.split('\n') if "All User Profiles" in line]


    if not profiles:
        print(f"No saved Wi-Fi profiles found.")
        return
    

    for profile in profiles:
        print(f"\n Checking Wi-Fiprofile: {profile}")
        try:
            result = subprocess.check_output(
                f'netsh wlan show profile name="{profile}"key=clear',shell=True).decode(errors="ignore")
            
            for line in result.split("\n"):
                if "Key Content" in line:
                    password = line.split(":")[1].strip()
                    print(f"wi-Fi: {profile} | Password: {password}")
                    break
                else:
                    print(f"Wo-Fi: {profile} | Password:Not Found")
        except subprocess.CalledProcessError:
            print(f"Error reading password for {profile}")


if __name__ == "__main__":
    print("WI-FI PAssword Extractor Running...")
    get_wifi_passwords()