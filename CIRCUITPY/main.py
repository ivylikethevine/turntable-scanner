import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
from digitalio import DigitalInOut, Direction
from adafruit_debouncer import Debouncer
import neopixel

# I believe the waveshare RP2040-Zero neopixel uses GRB, not RGB
color_green = (127, 0, 0)
color_red = (0, 127, 0)
color_blue = (0, 0, 127)

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
keyboard = Keyboard(usb_hid.devices)
yellow_wire = DigitalInOut(board.GP0)
blue_wire = DigitalInOut(board.GP1)
black_wire = DigitalInOut(board.GP2)

yellow_wire.direction = Direction.INPUT
blue_wire.direction = Direction.INPUT
black_wire.direction = Direction.OUTPUT

yellow_switch = Debouncer(yellow_wire, interval=0.050)

count = 0
def shutter():
    print('Hold Still!')
    pixel.fill(color_red)
    time.sleep(1.000)

    print('Shutter')
    keyboard.press(Keycode.SPACEBAR)
    keyboard.release(Keycode.SPACEBAR)
    pixel.fill(color_green)

pixel.brightness = 0.2
pixel.fill(color_blue)
print('Ready')

while True:
    yellow_switch.update()

    if yellow_switch.fell:
        shutter()
        count += 1
        print("Pic :" + str(count))

