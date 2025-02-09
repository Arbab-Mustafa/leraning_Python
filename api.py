import requests

# Base API URL
BASE_URL =  "https://ipinfo.io/134.201.250.155/json"


def data_get(endpoint, params=None):
    
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=10)
        response.raise_for_status()
        res = response.json()
        print(res)
        return res
    
    
        
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    