import requests
import pandas as pd
from datetime import datetime, timedelta

# Define API Key
api_key = "YOUR_API_KEY"

# API base URL
base_url = "https://api.sportmonks.com/v3/football"

# Define start and end dates for looping (modify as needed)
start_date = datetime(2023, 8, 11)
end_date = datetime(2024, 5, 19)

# Define weekly intervals (7 days per loop)
interval_days = 7

# Include relevant data fields
include = "lineups.player:display_name,image_path,position_id;lineups.details;scores"

# Headers for API authentication
headers = {"Authorization": api_key}

# Function to fetch data for a given date range
def fetch_fixture_data(start, end):
    matchdate = f"{start}/{end}"  # Format match date
    endpoint_url = f"{base_url}/fixtures/between/{matchdate}?include={include}"

    # API request
    response = requests.get(endpoint_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {start} to {end}. Status Code: {response.status_code}")
        return None

# Function to process data and save as CSV
def process_fixture_data(data, start, end):
    playerList, playerRating, playerClub, playerPosition = [], [], [], []

    if 'data' in data:
        for fixture in data['data']:
            for lineup in fixture.get('lineups', []):
                team_name = lineup['team']['name'] if 'team' in lineup else "Unknown Team"

                for playerstat in lineup.get('details', []):
                    if playerstat['type_id'] == 118:  # Assuming 118 is the stat type
                        player_name = lineup['player']['display_name']
                        player_rating = playerstat['data']['value']
                        position_id = lineup['player'].get('position_id', 'Unknown')

                        # Convert position ID to position name
                        position_mapping = {
                            24: "Goalkeeper",
                            25: "Defender",
                            26: "Midfielder",
                            27: "Attacker"
                        }
                        position = position_mapping.get(position_id, "Unknown")

                        # Append to lists
                        playerList.append(player_name)
                        playerRating.append(player_rating)
                        playerClub.append(team_name)
                        playerPosition.append(position)

    # Create DataFrame
    playerdata = pd.DataFrame({
        'Player Name': playerList,
        'Player Rating': playerRating,
        'Team Name': playerClub,
        'Position': playerPosition
    })

    # Save CSV for that week
    filename = f"fixtures_{start}_to_{end}.csv"
    playerdata.to_csv(filename, index=False)
    print(f"Saved data for {start} to {end} → {filename}")

# Loop through the date range in weekly intervals
current_date = start_date

while current_date < end_date:
    next_date = current_date + timedelta(days=interval_days)  # Move by interval
    date_start_str = current_date.strftime('%Y-%m-%d')
    date_end_str = next_date.strftime('%Y-%m-%d')

    # Fetch and process data
    data = fetch_fixture_data(date_start_str, date_end_str)
    if data:
        process_fixture_data(data, date_start_str, date_end_str)

    # Move to the next interval
    current_date = next_date



