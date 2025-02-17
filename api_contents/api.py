import requests
import datetime

# Get API key from the api_key.txt file
with open("api_contents/api_key.txt", "r") as file:
    API_KEY = file.read().strip()

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
    base_url = "https://app.ticketmaster.com/discovery/v2/events"
    params = {
        "apikey": API_KEY,
        "city": city,
        "radius": radius,
        "unit": "km",
        "sort": "date,asc",
        "locale": "*",
        "page": 0  # Start with page 0
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print(f"Error fetching events: {response.status_code}\n{response.text}")
        return []
    
    data = response.json()
    events = data.get("_embedded", {}).get("events", [])
    
    page_info = data.get("page", {})
    total_pages = page_info.get("totalPages", 1)
    
    for page in range(1, total_pages):
        params["page"] = page
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            events += data.get("_embedded", {}).get("events", [])
        else:
            print(f"Error fetching page {page}: {response.status_code}\n{response.text}")
    
    now = datetime.datetime.utcnow()
    filtered_events = []
    for event in events:
        try:
            sales = event.get("sales", {})
            public = sales.get("public", {})
            end_str = public.get("endDateTime")
            if end_str:
                end_time = datetime.datetime.strptime(end_str, "%Y-%m-%dT%H:%M:%SZ")
                if end_time < now:
                    continue  
        except Exception as e:
            pass
        filtered_events.append(event)
    
    return filtered_events
