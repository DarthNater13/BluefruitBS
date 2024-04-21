# Bluefruit BS (Bluetooth Sniffer)

Author: Nate Sherman  
Date: 04/20/2024  

## Project Overview
This project is a Bluetooth sniffer program designed to track the distance of a connected Bluetooth device from the Bluefruit board. It utilizes Neopixel LEDs for visual feedback and allows the scans to be stopped by using the buttons on the Bluefruit board.

## Pervasive Computing Technologies Used
1. **Bluetooth Low Energy (BLE):** Utilized for wireless communication and scanning of nearby Bluetooth devices.
2. **NeoPixel LEDs:** Utilized to display a visual representation of the RSSI and distance of the connected Bluetooth device.

## Setup/Installation/Running Instructions

### Hardware Requirements
- **Bluefruit Device:** The program is designed to run on a Bluefruit device.
- **Other Bluetooth-Based Device** The program is used to find a Bluetooth device, so another device using Bluetooth will be needed.

### Software Requirements
- **Python Libraries:**
  - `adafruit_ble`
  - `neopixel`
  - `digitalio`
  - `board`
  - `gc`

### Running the Program
1. Copy and paste the provided code into a code editor, and save it as `code.py` on the Bluefruit device.
2. Power on the Bluefruit device and ensure it is in a suitable Bluetooth range.
3. The program will start scanning for nearby Bluetooth devices and track the distance of the closest device using Neopixel LEDs.

## Usage Notes
- The program uses Bluetooth scanning to determine the RSSI (Received Signal Strength Indication) of nearby devices.
- Neopixel LEDs display a visual representation of the RSSI, indicating the proximity of the connected Bluetooth device.
- Pressing both buttons on the Bluefruit simultaneously stops the scan and turns off the Neopixel LEDs. Pressing them again stops the program. If you do not press the buttons a second time, it will find the next nearest device.
---

This README provides an overview of the Bluefruit BS project, its hardware/software requirements, and instructions for setup and usage. Customize and enhance the program as needed for specific applications.
