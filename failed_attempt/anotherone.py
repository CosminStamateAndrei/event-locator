import requests

token = "YOUR_OAUTH_TOKEN"
headers = {"Authorization": "Bearer " + token}
params = {"location.latitude": 40.7128, "location.longitude": -74.0060}
url = "https://www.eventbriteapi.com/v3/events/"

response = requests.get(url, headers=headers, params=params)
print(response.json())