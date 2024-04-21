"""
Author: Nate Sherman
Date: 04/20/2024
Title: Bluefriut BS (Bluetooth Sniffer)
Description: This program tracks the distance of a connected Bluetooth device from the Bluefruit.
"""
from time import sleep
import board
import neopixel
import gc
import digitalio
import adafruit_ble

# Setup Bluetooth
ble = adafruit_ble.BLERadio()
ble.name = "SHERMAN_Bluefruit"

# initialize neopixels
NUM_LEDS = 10
pixels = neopixel.NeoPixel(board.NEOPIXEL, NUM_LEDS, brightness=0.15, auto_write=False)

# named colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)

# set pixels to off initially
for i in range(NUM_LEDS):
    pixels[i] = OFF
pixels.show()

# Initialize Buttons under variables for assignment
btnA = digitalio.DigitalInOut(board.BUTTON_A)
btnA.switch_to_input(pull=digitalio.Pull.DOWN)

btnB = digitalio.DigitalInOut(board.BUTTON_B)
btnB.switch_to_input(pull=digitalio.Pull.DOWN)


BTN_TIMER_DELAY = 15
btn_timer = 0


done = False
locked = False

closest_device = None
closest_rssi = float("-inf")
rssi_normalized = float("-inf")

while not done:

    # Start scan and find the nearest device
    print("Starting Scan")
    scan_results = ble.start_scan(timeout=5)
    sleep(5)
    ble.stop_scan()


    # Review each scanned device and find the device with the lowest RSSI
    for advertisement in scan_results:
        # Check if the device has an RSSI value
        if advertisement.rssi is not None:
            # Check if the RSSI value is lower than the current closest RSSI
            if advertisement.rssi > closest_rssi:
                closest_device = advertisement.address # Record device address of the closest device
                closest_rssi = advertisement.rssi  # Record RSSI value of the closest device

                print(closest_device)
                print(closest_rssi)
                locked = True
                sleep(1)
        else:
            print("No nearby Bluetooth devices found.")

    while locked:
        # Start Bluetooth scan
        scan_results = ble.start_scan(timeout=2)
        sleep(2)
        ble.stop_scan()
        # Search for the device located earlier
        for advertisement in scan_results:
            if advertisement.address == closest_device:

                # Convert RSSI to positive
                closest_rssi_abs = advertisement.rssi * -1

                # Normalize RSSI (lower limit 30, upper limit 80) for LEDs
                rssi_normalized = int((closest_rssi_abs - 30) * (NUM_LEDS - 1) / (80 - 30))
                print(advertisement.rssi)

                # Set LED color and brightness based on normalized RSSI value
                for i in range(NUM_LEDS):
                    if i >= rssi_normalized:
                        pixels[i] = (0, 255 - i * (255 // NUM_LEDS), i * (255 // NUM_LEDS))
                    else:
                        pixels[i] = (0, 0, 0)
                pixels.show()
                break

        # Provide an option to end the loop and search for a new device
        if btnA.value and btnB.value:
            print("Stopping Focus")

            # Turn off LEDs
            for i in range(NUM_LEDS):
                pixels[i] = (0, 0, 0)
            pixels.show()
            sleep(5)
            locked = False
            break

    # Provide the user with an opportunity to stop the program by pressing both buttons
    print("Waiting for next command (will start scanning again in 5 seconds)")
    for i in range(5):
        if btnA.value and btnB.value:
            print("Ending program shortly")
            done = True
            break
        else:
            locked = False
            sleep(1)


    sleep(.1)
    gc.collect()

print("Program done - exiting.")
