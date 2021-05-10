from datetime import datetime, timezone
from ics import Calendar
import requests

calendar_base = 'https://www.recurse.com/calendar/events.ics?token='

def getNextEvent(token):
    if not token:
        return None
    c = Calendar(requests.get(calendar_base + token).text)
    tl = c.timeline

    for event in tl.today():
        # the events will always be in order, so we can return the first one happening after now
        if event.begin > datetime.now(timezone.utc):
            next_event = {
                'name': event.name,
                'location': event.location,
                'start': event.begin.astimezone(tz=None).strftime('%H:%M'),
                'end': event.end.astimezone(tz=None).strftime('%H:%M')
            }
            return next_event
    return None
