import requests

# Base API URL
BASE_URL =  "https://ipinfo.io/134.201.250.155/json"

def GetIP ( endPoint , params:'None' ):
    try:
        response = requests.get(f"{BASE_URL}{endPoint}", params=params)
        response.raise_for_status()
        # .raise_for_status()
        return response.json()
    except(requests.RequestException, ValueError):
        print("Network connection error occurred")
        return None


        