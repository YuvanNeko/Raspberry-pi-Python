import RPi.GPIO as Pin
from time import sleep
import os

button = 19
Pin.setmode(Pin.BCM)
Pin.setup(button, Pin.IN, pull_up_down=Pin.PUD_UP)

try:
  while True:
    if (Pin.input(button)==0):
      bashCommand = "echo \"hello, i was executed by a python program <3\""
      os.system(bashCommand)
      sleep(5)

except KeyboardInterrupt:
  Pin.cleanup()
