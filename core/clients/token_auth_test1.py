import requests
from pprint import pprint

# b33b1f1e68b048880c2492f64cf32aa8d716b440

def client():
    credentials = {
        'username': 'test_user',
        'password': 'testing321...'
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials,
        )
    
    print("Status code: ", response.status_code)

    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()