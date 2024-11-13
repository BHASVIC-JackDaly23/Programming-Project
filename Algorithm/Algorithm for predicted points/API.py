# Initialize your Python environment
# Import required libraries
import requests

# Define your API key
api_key = "6EY6z8qgu7RrGaHwQQbJc6qdTFxC3uJmqNutFDlHBEnceoDuaWwZLsVbwEla"
# Define the API endpoint URL
base_url = "https://api.sportmonks.com/v3/football"
endpoint = "/fixtures/between/2024-04-16/2024-04-17"
filters = "fixtureLeagues:2"
include = "participants;lineups.details;venue;statistics.type"
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
        print("Fixtures between 2024-04-16 and 2024-04-17:")
        for fixture in data.get('data', []):
            print(f"Fixture ID: {fixture['id']}")
            print(f"Name: {fixture['name']}")
            print(f"League ID: {fixture['league_id']}")
            print(f"Starting At: {fixture['starting_at']}")
            print(f"Result Info: {fixture['result_info']}")
            print(f"Participants:")
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
            venue = fixture['venue']
            print(f"    Venue ID: {venue['id']}")
            print(f"    Name: {venue['name']}")
            print(f"    City: {venue['city_name']}")
            print(f"    Address: {venue['address']}")
            print(f"    Capacity: {venue['capacity']}")
            print(f"    Surface: {venue['surface']}")
            print(f"    Image Path: {venue['image_path']}")
            print()
            print(f"Statistics:")
            for stat in fixture['statistics']:
                print(f"    Statistic ID: {stat['id']}")
                print(f"    Type: {stat['type']['name']}")
                print(f"    Type ID: {stat['type_id']}")
                print(f"    Team: {stat['location']}")
                print(f"    Value: {stat['data']['value']}")
                print()
            print()
    else:
        print("Failed to retrieve data. Status code:", response.status_code)