# Initialize your Python environment
# Import required libraries
import requests

# Define your API key
api_key = "6EY6z8qgu7RrGaHwQQbJc6qdTFxC3uJmqNutFDlHBEnceoDuaWwZLsVbwEla"
# Define the API endpoint URL
base_url = "https://api.sportmonks.com/v3/football"
endpoint = "/fixtures/between/2023-08-11/2023-08-17"
filters = "fixtureLeagues:8"
include = "participants;statistics.player"
endpoint_url = f"{base_url}{endpoint}?filters={filters}&include={include}"
# Include API key in request headers
headers = {"Authorization": api_key}
# Send a GET request to the Sportmonks API endpoint
response = requests.get(endpoint_url, headers=headers)
# Check if the request was successful
if response.status_code == 200:

    # Parse JSON response
    data = response.json()

    #For Debugging Purposes
    print("Data Response: ", data)

    if 'data' in data:
        # Print formatted response data
            for participant in fixture['participants']:
                print(f"    Team Name: {participant['name']}")
                print(f"    Short Code: {participant['short_code']}")
                print(f"    Image Path: {participant['image_path']}")
                print(f"    Last Played At: {participant['last_played_at']}")
                print(f"    Location: {participant['meta']['location']}")
                print(f"    Winner: {participant['meta']['winner']}")
                print(f"    Position: {participant['meta']['position']}")
                print()
            print(f"Venue:")
            print(f"Statistics:")
            for stat in player['statistics']:
                print(f"    Statistic ID: {stat['id']}")
                print(f"    Type: {stat['type']['name']}")
                print(f"    Type ID: {stat['type_id']}")
                print(f"    Team: {stat['location']}")
                print(f"    Value: {stat['data']['value']}")
                print()
            print()
    else:
        print("Failed to retrieve data. Status code:", response.status_code)