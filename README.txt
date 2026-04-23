ESP32Bluetooth.txt - A text file which is loaded onto the ESP32 as a .ino file (original file type could not be uploaded in teams for viewing purposes). Allows the ESP32 to emit a BLE5 communication channel. Sends the most recent RFID UID value to the Raspberry Pi 5.

Hardware_Startup.txt - A text file which is loaded onto the Raspberry Pi as a .desktop file (original file type could not be uploaded in teams for viewing purposes). Allows the Raspberry Pi to run the "EDAY-FINAL.py" python file immediately when the Raspberry Pi is turned on.

GUI_STARTUP.txt - A text file which is loaded onto the Raspberry Pi as a .desktop file (original file type could not be uploaded in teams for viewing purposes). Allows the Raspberry Pi to run the GUI python file immediately when the Raspberry Pi is turned on.

EDAY-FINAL.txt - A python file which is loaded onto the Raspberry Pi as a .py file. Allows the Raspberry Pi to work as a Bluetooth receiver for the ESP32. Intakes the Bluetooth data and sends information to the GUI using a CSV file. This python script also allows the additional PCB to work with the Bluetooth LED indicators and manual override/reset buttons.

EE491_Team14_GUI_Final.py - A python file which is loaded onto the Raspberry Pi as a .py file. It runs the GUI and it receives real time input from EDAY-FINAL.txt through a csv file that causes it to update in response to live external events.

GUI_Tester_Final.py - A python file which is ran on a user's computer simultaneously with the GUI. Both this and EE491_Team14_GUI_Final.py are ran at the same time. This script prompts the user to input a number to write to the CSV file to simulate the data that would be coming from the EDAY-FINAL.txt script. The purpose of this script is to be used to test the GUI without actually having the entire project put together.