# SPDX-FileCopyrightText: 2021 Brent Rubell, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
# originally from https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/MagTag_Google_Calendar/code.py
import time
import rtc
import json
from adafruit_display_shapes.line import Line
from adafruit_magtag.magtag import MagTag

# Amount of time to wait between refreshing the calendar, in minutes
REFRESH_TIME = 1

# Add a secrets.py to your filesystem that has a dictionary called secrets with "ssid" and
# "password" keys with your WiFi credentials. DO NOT share that file or commit it into Git or other
# source control.
# pylint: disable=no-name-in-module,wrong-import-order
try:
    from secrets import secrets
except ImportError:
    print("Credentials and tokens are kept in secrets.py, please add them there!")
    raise

# Create a new MagTag object
magtag = MagTag()
r = rtc.RTC()

magtag.network.connect()

def get_calendar_events(calendar_id, max_events, time_min):
    """Returns upcoming events from the NGW calendar
    Response is the current date pretty printed, and a list of events ordered by their start date/time in ascending order.
    """

    headers = {
        "Accept": "application/json",
        "Content-Length": "0",
    }

    # this is the URL to the NGW calendar web service
    # url = ( "http://localhost:5000/rc-calendar?token={0}&tz={1}".format(rc_calendar_token,timezone) )
    resp = magtag.network.requests.get(url, headers=headers)
    resp_json = resp.json()
    if "error" in resp_json:
        raise RuntimeError("Error:", resp_json)
    resp.close()
    # parse the 'items' array so we can iterate over it easier
    items = []
    resp_items = resp_json["items"]
    if not resp_items:
        print("No events scheduled for today!")
    for event in range(0, len(resp_items)):
        items.append(resp_items[event])
    return items

def display_calendar_events(resp_events):
    # Display all calendar events
    for event_idx in range(len(resp_events)):
        event = resp_events[event_idx]
        # wrap event name if necessary
        event_name = magtag.wrap_nicely(event["name"], 37)
        event_location = event["location"]
        event_name = event_name[0] # only display 1 line of the event name
        event_start = event['start']
        event_end = event['end']
        print("-" * 40)
        print("Event Description: ", event_name)
        print("Event Start:", event_start)
        print("Event End:", event_end)
        print("Event Location:", event_location)
        print("-" * 40)
        # Generate labels holding event info
        magtag.add_text(
            text_font=font_event,
            text_position=(7, 33 + (event_idx * 35)),
            text_color=0x000000,
            text=event_start,
        )
        magtag.add_text(
            text_font=font_event,
            text_position=(7, 50 + (event_idx * 35)),
            text_color=0x000000,
            text=event_end,
        )
        magtag.add_text(
            text_font=font_event,
            text_position=(55, 33 + (event_idx * 35)),
            text_color=0x000000,
            text=event_name,
            line_spacing=0.65,
        )
        magtag.add_text(
            text_font=font_event,
            text_position=(55, 50 + (event_idx * 35)),
            text_color=0x000000,
            text=event_location,
            line_spacing=0.65,
        )



# demo data
json_events = """{
"date": "Sunday, May 08, 2022",
"events": [
{
"end": "11:30",
"location": "Not specified",
"name": "Test Event 1 - do not use",
"start": "11:00"
},
{
"end": "12:00",
"location": "Church",
"name": "Is this the real event? Is this just fantasy?",
"start": "11:30"
},
{
"end": "12:30",
"location": "Kitchen",
"name": "Hello, is this the event you're looking for?",
"start": "12:00"
}
]
}"""
# parse the json response
the_thing = json.loads(json_events)

# DisplayIO Setup
magtag.set_background(0xFFFFFF)

# Add the header
line_header = Line(0, 26, 320, 26, color=0x000000)
magtag.splash.append(line_header)

# Set up calendar event fonts
font_event = "fonts/Arial-12.pcf"

# fetch calendar events!
print("fetching local time...")

label_header = magtag.add_text(
    text_font="fonts/Arial-18.pcf",
    text_position=(5, 10),
    text_color=0x000000,
)
# setup header label
magtag.set_text(
    the_thing['date'], label_header, auto_refresh=False
)

print("fetching calendar events...")

print("displaying events")
display_calendar_events(the_thing['events'])

magtag.refresh()

print("Sleeping for %d minutes" % REFRESH_TIME)
magtag.exit_and_deep_sleep(REFRESH_TIME * 60)
