# Calendar display for Recurse Center's Never Graduate Week 2022

## Required Hardware
AdaFruit [MagTag](https://www.adafruit.com/product/4800), you will likely want to get a battery and the magnet feet.

You may also want the [hardware kit](https://www.adafruit.com/product/4807) so you have a backplate to hold the battery, and the front plate for looking cool.

## Configuration
You will need to add two Python keys to the secrets.py file on the MagTag.
In addition to filling in the SSID and password for your 2G wifi network, you will want to add 'timezone' and 'rc_calendar_token'.
The [calendar settings](https://www.recurse.com/settings/calendar) page has a 'Subscription URL' field with contents that look like `https://www.recurse.com/calendar/events.ics?token=randomlettersandnumbers`. You want to put the randomlettersandnumbers value into the value for the 'rc_calendar_token' key, as shown below.
```python
secrets = {
	'ssid' : 'Mass Distraction_2G',             # Keep the two '' quotes around the name
	'password' : 'thepassword',         # Keep the two '' quotes around password
	'timezone' : "America/New_York",  # http://worldtimeapi.org/timezones
	'rc_calendar_token' : 'randomlettersandnumbers',
}
```

## Circuit Python Libraries required
The libraries below will need to be in the CIRCUITPY/lib directory on the MagTag.
- adafruit_bitmap_font
- adafruit_display_shapes
- adafruit_io
- adafruit_magtag
- adafruit_minimqtt
- simpleio.mpy

## Fonts required
The files below can be found in the [fonts](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/MagTag_Google_Calendar/fonts) directory of the origin project. Also, you want to download these via browser, you don't want to clone this massive repo!
Much like the origin project, you will want these files in the CIRCUITPY/fonts directory on the MagTag.
- Arial-12.pcf
- Arial-14.pcf
- Arial-18.pcf
