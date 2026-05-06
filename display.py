def show_earthquakes(data, min_magnitude=0, location_filter=""):
    earthquakes = data["features"]
    
    print("🌋 EARTHQUAKE MONITOR 🌋")
    print("========================")
    print("Minimum magnitude: " + str(min_magnitude))
    print("Location filter: " + str(location_filter))
    print("========================")
    
    count = 0
    for earthquake in earthquakes:
        magnitude = earthquake["properties"]["mag"]
        location = earthquake["properties"]["place"]
        
        # Filter by magnitude AND location
        if magnitude >= min_magnitude and location_filter.lower() in str(location).lower():
            print("📍 Location: " + str(location))
            print("💥 Magnitude: " + str(magnitude))
            print("------------------------")
            count += 1
    
    print("Total earthquakes found: " + str(count))
