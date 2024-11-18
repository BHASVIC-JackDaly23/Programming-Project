# Initialize your Python environment
# Import required libraries


import requests
import json

# Define your API key
api_key = "Pg6RHBcK6V71HKUaYi2YUFJcgYjI663H0Pfpy3Meb6q4YdKNVyQ5Bd4B5otv"
# Define the API endpoint URL
base_url = "https://api.sportmonks.com/v3/football"
endpoint = "/leagues"
include = "country"
endpoint_url = f"{base_url}{endpoint}?include={include}"
# Include API key in request headers
headers = {"Authorization": api_key}
# Send a GET request to the Sportmonks API endpoint
response = requests.get(endpoint_url, headers=headers)
# Check if the request was successful
if response.status_code == 200:

    # Parse JSON response
    data = response.json()
    # Print formatted response data
    print("List of Football Leagues:")
    for league in data['data']:
        print(f"League ID: {league['id']}")
        print(f"Name: {league['name']}")
        print(f"Country ID: {league['country_id']}")
        print(f"Country: {league['country']['name']}")
        print(f"Short Code: {league['short_code']}")
        print(f"Image Path: {league['image_path']}")
        print(f"Type: {league['type']}")
        print(f"Sub Type: {league['sub_type']}")
        print(f"Last Played At: {league['last_played_at']}")
        print(f"Has Jerseys: {league['has_jerseys']}")
        print()
else:
    print("Failed to retrieve data. Status code:", response.status_code)