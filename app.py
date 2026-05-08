from flask import Flask, jsonify
from api import get_earthquakes
from database import create_database, save_earthquake, get_saved_earthquakes, get_statistics, clear_database

app = Flask(__name__)

@app.route('/')
def home():
    return "🌋 Earthquake Monitor is running!"

@app.route('/earthquakes')
def earthquakes():
    data = get_earthquakes()
    create_database()
    clear_database()
    
    countries = ["Peru", "Chile", "Colombia", "Ecuador", "Bolivia"]
    
    for country in countries:
        for earthquake in data["features"]:
            magnitude = earthquake["properties"]["mag"]
            location = earthquake["properties"]["place"]
            date = earthquake["properties"]["time"]
            if country.lower() in str(location).lower():
                save_earthquake(magnitude, location, date)
    
    saved = get_saved_earthquakes()
    return jsonify(saved)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
