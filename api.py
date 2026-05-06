import requests

def get_earthquakes():
    # USGS Earthquake API URL
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    
    # Send GET request to API
    response = requests.get(url)
    
    # Convert response to Python data
    data = response.json()
    
    return data

# ADD THESE LINES AT THE BOTTOM
data = get_earthquakes()
print("Connection successful!")
print("Total earthquakes today:", len(data["features"]))