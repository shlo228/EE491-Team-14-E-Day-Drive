import asyncio, csv, os
from bleak import BleakClient, BleakScanner
from gpiozero import Button, LED
from time import sleep

# Shared Data & Config
TARGET_DEVICE_NAME = "E-Day Drive"
CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"
filename, tempFileName = 'Garrick.csv', 'Garrick.tmp'
resVal, gateVal, overVal = 0, 0, 0
text = ""
btnRes, btnGate, btnPwr = Button(5), Button(6), Button(13)
rLED, yLED, gLED = LED(17), LED(27), LED(22)

async def monitor_buttons():
    global resVal, gateVal, overVal
    global text
    prevR, prevG, prevP = False, False, False
    while True:
        with open(tempFileName, 'w', newline='') as f:
            csv.writer(f).writerow([resVal, gateVal, overVal])
        os.replace(tempFileName, filename)

        if btnRes.is_pressed and not prevR:
            resVal += 1
            prevR = True
            text = "reset"
        elif not btnRes.is_pressed: prevR = False

        if btnGate.is_pressed and not prevG:
            overVal += 1 
            prevG = True
            text = "manual"
        elif not btnGate.is_pressed: prevG = False

        if btnPwr.is_pressed and not prevP:
            overVal += 2
            prevP = True
            text = "manual"
        elif not btnPwr.is_pressed: prevP = False
        #print(resVal, gateVal, overVal)        
        await asyncio.sleep(0.1)

async def run_ble_receiver():
    global gateVal  
    global text
    print("Scanning...")
    device = await BleakScanner.find_device_by_name(TARGET_DEVICE_NAME)
    if not device:
        rLED.on(); return
    
    yLED.on()
    try:
        async with BleakClient(device.address, timeout=45) as client:
            if client.is_connected:
                yLED.off(); gLED.on()
                prevGate = None
                while True:
                    try:
                        data = await client.read_gatt_char(CHARACTERISTIC_UUID)
                        text = data.decode('utf-8')
                        if text != prevGate:
                            match text:
                                case "a1a0af41":   #UID for Triangle Gate 
                                    gateVal += 3
                                case "ad7daf41":     #UID for Circle Gate 
                                    gateVal += 2
                                case "4f3caf41":     #UID for Square Gate
                                    gateVal += 1
                                case "e91a537":      #UID for Oval Gate
                                    gateVal += 4
                                case "7cc0b041":    #UID for Powerup1 Gate
                                    gateVal += 5
                                case "e956ea11":   #UIDs for Powerup2 Gate 
                                    gateVal += 6
                            prevGate = text
                        print("Data:", text)
                    except Exception: 
                        gLED.off(); rLED.on()
                        await asyncio.sleep(3)
                        rLED.off()
                    await asyncio.sleep(0.2)
    except Exception as e:
        print(f"Connection error: {e}")
        gLED.off(); rLED.on()
        await asyncio.sleep(3)
        rLED.off()

async def main():
    await asyncio.gather(monitor_buttons(), run_ble_receiver())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")
        rLED.off();
        yLED.off();
        gLED.off();
