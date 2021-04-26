from datetime import datetime, timezone
from dotenv import load_dotenv
from ics import Calendar
import os
import requests

# loads environment variables from a .gitignore'd .env file
load_dotenv()

calendar_base = 'https://www.recurse.com/calendar/events.ics?token='
# token from RC calendar settings goes in .env like ICS_TOKEN=<token>
token = os.getenv('ICS_TOKEN')

c = Calendar(requests.get(calendar_base + token).text)
tl = c.timeline

for event in tl.today():
    # the events will always be in order, so we can return the first one happening after now
    if event.begin > datetime.now(timezone.utc):
        #TODO figure out how we want to pass this data to the eink script
        print(event.name)
        print(event.begin.astimezone(tz=None)) # tz=None forces system timezone
        print(event.end.astimezone(tz=None))
        print(event.location)
        break
