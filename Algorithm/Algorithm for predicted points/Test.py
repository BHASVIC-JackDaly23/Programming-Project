import requests

response = requests.get("https://dashboard.api-football.com/soccer/requests")
print(response.status_code)

