import requests

# Get API key from the api_key.txt file
with open("api_contents/api_key.txt", "r") as file:
    API_KEY = file.read().strip()

# Function to search for events near the current location
def search_nearby_events(lat, lon, radius=10, unit='miles'):
    base_url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": API_KEY,
        "latlong": f"{lat},{lon}",
        "radius": radius,
        "unit": unit,
        "sort": "date,asc"
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        events = data.get("_embedded", {}).get("events", [])
        return events
    else:
        print(f"Error fetching events: {response.status_code}\n{response.text}")
        return []

# Function to display the events
def display_events(events):
    if not events:
        print("No events found nearby.")
        return

    print(f"\nFound {len(events)} events nearby:")
    print("-" * 50)
    for event in events:
        name = event.get("name", "No name")
        url = event.get("url", "No URL")
        dates = event.get("dates", {}).get("start", {})
        local_date = dates.get("localDate", "No date")
        venues = event.get("_embedded", {}).get("venues", [])
        venue_name = venues[0].get("name", "No venue") if venues else "No venue"
        
        print(f"Event: {name}")
        print(f"Date: {local_date}")
        print(f"Venue: {venue_name}")
        print(f"More Info: {url}")
        print("-" * 50)

# Function to search for events near a specific location
def specific_search(city, radius):
    base_url = f"https://app.ticketmaster.com/discovery/v2/events?apikey={API_KEY}&locale=*&city={city}"
    params = {
        "apikey": API_KEY,
        "city": city,
        "radius": radius,
        "unit": 'km',
        "sort": "date,asc"
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        events = data.get("_embedded", {}).get("events", [])
        return events
    else:
        print(f"Error fetching events: {response.status_code}\n{response.text}")
        return []


def main():  
    radius = input("Input radius in km: ")

    events = specific_search(city = "Groningen", radius = radius)
    display_events(events)

if __name__ == "__main__":
    main()
