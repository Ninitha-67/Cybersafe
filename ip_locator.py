import requests 

def locate_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'success':
        print(f"\nIP Address: {ip}")
        print(f"Country    : {data['country']}")
        print(f"City       :{data['city']}")
        print(f"ISP        :{data['isp']}")
        print(f"Lat/Lon    :{data['lat']}, {data['lon']}")
    else:
        print("Invalid IP or request failed.")

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    locate_ip(ip)