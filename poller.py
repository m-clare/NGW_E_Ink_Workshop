from dotenv import load_dotenv
import fetch_calendarnnn
import fetch_formatted_text
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
            event_range = event['start'] + ' - ' + event['end']
            event_location = event['location'].split('/')[-1]
            print(event['name'])
            print(event_location)
            print(event_range)

            img = fetch_formatted_text.get_text_image(inky_display, (event['name'], event_range, event_location))
            # send to inky (comment out only on local machine)
            # fetch_formatted_text.rgb_to_inky(inky_display, img)


    # sleep 30 seconds
    time.sleep(30)


