import requests

API_URL = "http://34.66.193.111:5002/api/secure-data"
TOKEN = "bviurwbrvuijv1256"


headers = {
"Authorization": f"Bearer {TOKEN}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)