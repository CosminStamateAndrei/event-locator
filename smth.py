import requests
import geocoder

# Function to search for events near the current location
def search_nearby_events(api_key, lat, lon, radius, unit='miles'):
    base_url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": api_key,
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
def specific_search(api_key, city, radius):
    base_url = f"https://app.ticketmaster.com/discovery/v2/events?apikey=BTyfayvfZ6287xANJRbvsRHelbqbnR6I&locale=*&city=Groningen"
    params = {
        "apikey": api_key,
        "city": city,
        "radius": radius,
        "unit": 'kilometers',
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
    API_KEY = "BTyfayvfZ6287xANJRbvsRHelbqbnR6I"  

    radius = input("Input a radius in kilometers: ")
    radius = int(int(radius) * 0.621371) 

    events = search_nearby_events(API_KEY, lat, lon, radius=radius)
    display_events(events)

if __name__ == "__main__":
    main()
