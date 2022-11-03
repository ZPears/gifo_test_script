from gpiozero import Button

# See link below for list of valid pin numbers:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
#
# Note that these numbers are the GPIO numbers, NOT the hardware pin numbers.
LEFT_PINS = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]
RIGHT_PINS = [14, 15, 18, 23, 24,25, 8, 7, 12, 16, 20, 21]

def button_callback(button: Button) -> None:
    button_number = str(button.pin.number)
    print(f"Input on pin number {button_number}")

def main():
    pins = LEFT_PINS + RIGHT_PINS
    buttons = [Button(i) for i in pins]
    for button in buttons:
        button.when_pressed = button_callback

if __name__ == "__main__":
    main()
