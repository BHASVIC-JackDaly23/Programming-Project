import requests
import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "05163fc687b34571a2f4aae19f980f33"
    }

conn.request("GET", "/players/season=2022&league=61", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))





