from api import get_earthquakes
from display import show_earthquakes
from database import create_database, save_earthquake, get_saved_earthquakes, get_statistics, clear_database

def main():
    print("Fetching earthquake data...")
    data = get_earthquakes()
    
    # Create and clear database
    create_database()
    clear_database()
    
    # Save South American earthquakes to database
    countries = ["Peru", "Chile", "Colombia", "Ecuador", "Bolivia"]
    
    for country in countries:
        earthquakes = data["features"]
        for earthquake in earthquakes:
            magnitude = earthquake["properties"]["mag"]
            location = earthquake["properties"]["place"]
            date = earthquake["properties"]["time"]
            
            if country.lower() in str(location).lower():
                save_earthquake(magnitude, location, date)
                print("Saved: " + str(location))
    
    # Show saved earthquakes
    print("\nSAVED EARTHQUAKES IN DATABASE:")
    print("==================================")
    saved = get_saved_earthquakes()
    for eq in saved:
        print("ID: " + str(eq[0]))
        print("Magnitude: " + str(eq[1]))
        print("Location: " + str(eq[2]))
        print("------------------------")
    
    print("Total saved: " + str(len(saved)))
    
    # Show statistics
    print("\nEARTHQUAKE STATISTICS:")
    print("==================================")
    total, strongest, average, location = get_statistics()
    print("Total earthquakes recorded: " + str(total))
    print("Strongest earthquake: " + str(strongest))
    print("Strongest location: " + str(location))
    print("Average magnitude: " + str(round(average, 2)))

main()