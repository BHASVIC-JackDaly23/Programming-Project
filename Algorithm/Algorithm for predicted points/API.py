# Initialize your Python environment
# Import required libraries
import requests

# Define your API key
api_key = "6EY6z8qgu7RrGaHwQQbJc6qdTFxC3uJmqNutFDlHBEnceoDuaWwZLsVbwEla"
# Define the API endpoint URL
base_url = "https://api.sportmonks.com/v3/football"
endpoint = "/fixtures/between/2023-08-11/2023-08-17"

filters = "fixtureLeagues:8;player"
include = "&statistics.details"

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
        print("Player Statistics for Premier League Opening Week:")
        for fixture in data.get('data', []):
            print(f"\nFixture: {fixture['name']} (ID: {fixture['id']})")
            print(f"Date: {fixture['starting_at']}")

            # Check for player statistics
            if 'statistics' in player:
                for statistic in player['statistics']:
                    if 'statistic' in player:  # Ensure player statistics exist
                        player = statistic['player']
                        print(f"\nPlayer Name: {player['name']} (ID: {player['id']})")
                        print(f"    Team: {statistic['location']}")
                        print(f"    Position: {statistic['data']['position']}")
                        print(f"    Goals Scored: {statistic['data']['goals']}")
                        print(f"    Assists: {statistic['data']['assists']}")
                        print(f"    Shots: {statistic['data']['shots']}")
                        print(f"    Pass Accuracy: {statistic['data']['pass_accuracy']}%")
                        print(f"    Yellow Cards: {statistic['data']['yellow_cards']}")
                        print(f"    Red Cards: {statistic['data']['red_cards']}")
            else:
                print("No player statistics available for this fixture.")
    else:
        print("No data found in the response.")
else:
     print("Failed to retrieve data. Status code:", response.status_code)