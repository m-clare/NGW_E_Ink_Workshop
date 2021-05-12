# NGW_E_Ink_Workshop
Helper scripts for workshop with Pimoroni wHAT and pHAT

Talk slides available [here](https://docs.google.com/presentation/d/1zFcely572CDyV7RaiTGjxGSO8rh0fIeGNnI4kEsWmTw/edit?usp=sharing)

## Materials
- (1) [Raspberry Pi Zero WH](https://www.adafruit.com/product/3708) - $14 for a presoldered one
- (1) MicroSD card flashed with [Raspberry Pi OS](https://www.raspberrypi.org/software/) and wifi enabled (see instructions [here](https://code.mendhak.com/prepare-raspberry-pi/)) - $10 (min)
- (1)  [5V power supply](https://www.adafruit.com/product/1995) - $7.50
- (1) Pimoroni e-ink display! We will be working specifically with the Inky library for [Inky pHAT](https://www.adafruit.com/product/3743)  - $25 -$27 or [Inky wHAT](https://www.adafruit.com/product/4142) - $55 - $65.

## Configuring your Pi Zero WH

Follow the instructions at one of the following links to set up your Pi to be accessible over wifi via ssh (this is mainly to avoid having to work directly on the pi and utilize peripherals)

https://code.mendhak.com/prepare-raspberry-pi/

https://desertbot.io/blog/setup-pi-zero-w-headless-wifi

In addition, you need to enable the SPI Interface within the pi

```shell
sudo raspi-config
```

From the menu, go to interfacing options and enable ```P4 SPI```

While the pHAT and wHAT cover all 40 pins, they only use a [few of them](https://pinout.xyz/pinout/inky_phat#).

## Troubleshooting Raspian Buster

During the workshop we had some issues with missing libraries in Raspian Buster. The following additional libraries were required for the Python packages (mainly Pillow as a result of numpy) needed for image creation.

```shell
sudo apt-get install libatlas-base-dev
```

## Working with your Inky 
The helper scripts included should be modified (particularly if your Pi has issues autorecognizing your Inky). 

If you get an error that Inky cannot be autodetected, you can manually set the inky type:

```inky_display = auto()``` --> ```inky_display = InkyPHAT()``` or ```inky_display = InkyWHAT()```

Within ```poller.py```, you'll need to uncomment the ```fetch_formatted_text.rgb_to_inky(inky_display, img)``` to push anything to Inky. It is currently commented out to allow for image troubleshooting/adjustment with Pillow. You can show the image locally on your computer by adding ```img.show()```

To run ```poller.py``` continuously after disconnecting from SSH you can do the following:


```shell
pi@raspberrypi.local:~$ python3 poller.py > /dev/null &
pi@raspberrypi.local:~$ jobs -l
[2]+  7471 Running                 python3 poller.py > /dev/null &
pi@raspberrypi.local:~$ disown %2
```

Note that the number you'll want to pick for the disown command should match the number in front of the job you're looking to disown.

When you're ready to kill the script (because it will run into eternity!), you can kill the process manually by tracking down the PID and killing it:

```shell
pi@raspberrypi.local:~$ ps aux | grep poller.py
pi   7471 20.8  8.8  50824 33520 ?        S    15:26   3:47 python3 poller.py
pi@raspberrypi.local:~$ kill 7471
```
