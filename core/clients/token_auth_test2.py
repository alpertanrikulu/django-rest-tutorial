import requests
from pprint import pprint

# b33b1f1e68b048880c2492f64cf32aa8d716b440

def client():

    token = 'Token b33b1f1e68b048880c2492f64cf32aa8d716b440'
    headers = {
        'Authorization': token
    }

    response = requests.get(
        url='http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers=headers
        )
    
    print("Status code: ", response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == "__main__":
    client()