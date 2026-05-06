import sqlite3

def create_database():
    connection = sqlite3.connect("earthquakes.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS earthquakes (
            id INTEGER PRIMARY KEY,
            magnitude REAL,
            location TEXT,
            date TEXT
        )
    """)
    connection.commit()
    connection.close()
    print("Database created successfully!")

def save_earthquake(magnitude, location, date):
    connection = sqlite3.connect("earthquakes.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO earthquakes (magnitude, location, date)
        VALUES (?, ?, ?)
    """, (magnitude, location, date))
    connection.commit()
    connection.close()

def get_saved_earthquakes():
    connection = sqlite3.connect("earthquakes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM earthquakes")
    earthquakes = cursor.fetchall()
    connection.close()
    return earthquakes

def clear_database():
    connection = sqlite3.connect("earthquakes.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM earthquakes")
    connection.commit()
    connection.close()
    print("Database cleared!")

def get_statistics():
    connection = sqlite3.connect("earthquakes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM earthquakes")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT MAX(magnitude) FROM earthquakes")
    strongest = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(magnitude) FROM earthquakes")
    average = cursor.fetchone()[0]
    cursor.execute("SELECT location FROM earthquakes WHERE magnitude = ?", (strongest,))
    strongest_location = cursor.fetchone()[0]
    connection.close()
    return total, strongest, average, strongest_location