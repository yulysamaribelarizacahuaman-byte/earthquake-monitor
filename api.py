import requests

def get_earthquakes():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response = requests.get(url)
    data = response.json()
    return data

# Remove or comment these lines:
# data = get_earthquakes()
# print("Connection successful!")
# print("Total earthquakes today:", len(data["features"]))