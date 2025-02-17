# import eventbrite api library
from eventbrite import Eventbrite
import json
import geocoder

# Search by location and search events: Depricated since 2019

# import the api key from the api_key.txt file
with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

# create an instance of the Eventbrite class
eventbrite = Eventbrite(api_key)

# get the current location of the device
def get_location():
    g = geocoder.ip('me')
    return g.latlng

# search for events near the current location
def search_events(lat, long):
    events = eventbrite.get('/events/1/?expand=ticket_classes')
    print(json.dumps(events, indent=4))
    
    # iterate i over 10000 and do /events/{i}/?expand=ticket_classes
    for i in range(10000):
        events = eventbrite.get(f'/events/{i}/?expand=ticket_classes')
        print(json.dumps(events, indent=4))
        if(events['status_code'] == 200):
            break


# main function
def main():
    # get the current location
    lat, long = get_location()
    # search for events
    search_events(lat, long)

# run the main function
if __name__ == "__main__":
    main()