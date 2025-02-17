# This will be the main file for the locator program. It will be responsible for the following:
# 1. Finding your current location (of the device)
# 2. Searching on google through eventbri api for events near your location
# 3. It will output those events in a list and format them to see the name, location, and time of the event

# Importing the necessary libraries
import geocoder
import requests
import json


# Function to search for events near the current location
# Query parameter authentication : /v3/users/me/?token=MYTOKEN
def search_events(lat, long):
    # Eventbrite API key
    api_key = "VM563APY6T332DKUA5A2"
    # Eventbrite API endpoint
    url = "https://www.eventbriteapi.com/v3/users/me/?token=VM563APY6T332DKUA5A2"
    # Parameters for the search
    params = {
        "token": api_key,
        "location.latitude": lat,
        "location.longitude": long
    }
    # Make a request to the API
    response = requests.get(url, params=params)
    # Get the JSON data
    data = response.json()
    # Print the data
    print(json.dumps(data, indent=4))



# Function to get the current location of the device
def get_location():
    g = geocoder.ip('me')
    return g.latlng


# Main function
def main():
    # Get the current location
    lat, long = get_location()
    # Search for events
    search_events(lat, long)

# Run the main function
if __name__ == "__main__":
    main()