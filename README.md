# Instructions

1. After installing the RPi OS (I would use ["Raspberry Pi OS with Recommended Software"](https://www.raspberrypi.com/software/operating-systems/), since it likely includes everything you'll need), open a terminal window.
2. Go to the home directory (in case you aren't already there): `cd ~`
3. Clone this repository: `git clone https://github.com/ZPears/gifo_test_script.git`
4. Go into the cloned repository: `cd ~/gifo_test_script`
5. Install dependencies (just the GPIO library): `pip install -r requirements.txt`
6. Start program: `python test.py`
7. Press buttons and see if there's any output to the console. It should print "Input on pin number $PIN_NUMBER" whenever a pin receives input.

# Notes

Note that in [this documentation link for the GPIO library](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering), the software numbering for the pins is not the same as the hardware pin numbers. So do not worry about discrepancies there.
