from dotenv import load_dotenv
import fetch_calendar
import os
import time

# loads environment variables froma .gitignore'd .env file
load_dotenv()
# RC calendar token from .env
token = os.getenv('ICS_TOKEN')
inked_name = ''
inked_location = ''
inked_start = ''
inked_end = ''

while True:
    event = fetch_calendar.getNextEvent(token)

    if not event:
        print("No more events today")
    else:
        if event['name'] == inked_name and event['location'] == inked_location and event['start'] == inked_start and event['end'] == inked_end:
            print("We've already drawn this one to the display!")
        else:
            inked_name = event['name']
            inked_location = event['location']
            inked_start = event['start']
            inked_end = event['end']

            ####### WORKSHOP CODE GOES HERE #######
            print(event['name'])
            print(event['location'])
            print(event['start'])
            print(event['end'])

    # sleep 30 seconds
    time.sleep(30)


