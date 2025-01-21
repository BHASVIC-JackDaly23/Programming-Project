import requests
import pandas as pd

# Define your API key
api_key = "6EY6z8qgu7RrGaHwQQbJc6qdTFxC3uJmqNutFDlHBEnceoDuaWwZLsVbwEla"

matchdate = "2023-08-11/2023-08-17"
# Define the API endpoint URL
base_url = "https://api.sportmonks.com/v3/football"
endpoint = "/fixtures/between/2023-08-11/2023-08-17"

filters = "fixtureLeagues:8;statisticTypes:118"
include = "lineups.player:display_name,image_path;lineups.player.country:name,image_path;lineups.details;scores"

endpoint_url = f"{base_url}{endpoint}?include={include}&filters={filters}"

# Includes API key in request headers
headers = {"Authorization": api_key}
# Sends a GET request to the API endpoint
response = requests.get(endpoint_url, headers=headers)


def get_teamname(h):
    getteams = f"https://api.sportmonks.com/v3/football/teams/{lineup['team_id']}"
    teamname = requests.get(getteams, headers=h)
    return teamname.json()


# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    if 'data' in data:

        TeamNamePrinted = 0

        playerList = []
        playerRating = []

        print("Player Statistics for Premier League Opening Week:")
        for fixture in data.get('data', []):
            print(f"\nFixture: {fixture['name']} (ID: {fixture['id']})")
            print(f"Date: {fixture['starting_at']}")
            # Check for player statistics
            # TeamNamePrinted = fixture['team_id']

            for lineup in fixture.get('lineups', []):

                teamnamedata = get_teamname(headers)

                if TeamNamePrinted != teamnamedata['data']['id']:
                    TeamNamePrinted = 0

                for playerstat in lineup.get('details', []):
                    if playerstat['type_id'] == 118:
                        if TeamNamePrinted == 0:  # first time name been printed
                            #print(f"{teamnamedata['data']['name']}")
                            TeamNamePrinted = teamnamedata['data']['id']



                        #print(f"Player:{lineup['jersey_number']} {lineup['player']['display_name']} {lineup['player']['image_path']}")
                        #print(f"Player Rating : {playerstat['data']['value']}")

                        playerInfo = f"Player:{lineup['player']['display_name']} "
                        playerStuff = f"Player Rating : {playerstat['data']['value']}"
                        playerList.append(playerInfo)
                        playerRating.append(playerStuff)





    else:
        print("No data found in the response.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)

playerdata = pd.DataFrame({'Player Name':playerList, 'Player Rating':playerRating})
playerdata.to_csv('playerlist.csv', index=False)



for i in range(len(playerdata)-1):
    if playerdata.iloc[i]['Player Rating'] > playerdata.iloc[i + 1]['Player Rating']:
        #Swap the two rows
        placeholder = playerdata.iloc[i+1].copy()
        playerdata.iloc[i+1] = playerdata.iloc[i]
        playerdata.iloc[i] = placeholder

    else:
        placeholder = playerdata.iloc[i].copy()
        playerdata.iloc[i] = playerdata.iloc[i+1]
        playerdata.iloc[i+1] = placeholder

