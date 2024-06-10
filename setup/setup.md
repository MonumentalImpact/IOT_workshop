# Setup

## Install Thonny on the host computer
For the workshop computers, this will already be done. If you have your own computer, go to [thonny.org](https://thonny.org/) and download/install thonny. It's a free python development environment that's easy to use and has built-in support for micropython and microcontrollers like the ESP32 that we'll be using.

## Getting acquainted with the kit

## Flashing micropython
We use thonny to install micropython on the esp32.

From the Thonny "Run" menu, choose "Configure Interpreter"

Change the interpreter to "MicroPython (ESP32)"

Then click on "Install or update MicroPython (esptool)"

![image](https://github.com/MonumentalImpact/IOT_workshop/assets/12822917/68b2ee54-b14d-4d96-8f69-faf689feec99)

Your "Target port" may be different - that's OK.

Before you click the "Install" button, hold down the "boot" button on the ESP32, then hold down the other button (on the other side of the USB port), the release the other button, then release the "boot" button.

Then click "Install".

## First program - using Thonny

Now to test it all out....

Open [setup_light_test.py](https://github.com/MonumentalImpact/IOT_workshop/blob/main/1%20-%20setup/setup_light_test.py) in Thonny and click "Run". It should flash a blue light on the ESP32.

