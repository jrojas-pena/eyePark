# This program allows a user to enter a
# Code. If the C-Button is pressed on the
# keypad, the input is reset. If the user
# hits the A-Button, the input is checked.

import RPi.GPIO as GPIO
import time


class KeyPad:

    def __init__(self):

        # These are the GPIO pin numbers where the
        # lines of the keypad matrix are connected
        self.L1 = 17
        self.L2 = 27
        self.L3 = 22
        self.L4 = 5

        # These are the four columns
        self.C1 = 6
        self.C2 = 13
        self.C3 = 19
        self.C4 = 26


        # The GPIO pin of the column of the key that is currently
        # being held down or -1 if no key is pressed
        self.keypadPressed = -1

        self.input = ""

        # Setup GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.L1, GPIO.OUT)
        GPIO.setup(self.L2, GPIO.OUT)
        GPIO.setup(self.L3, GPIO.OUT)
        GPIO.setup(self.L4, GPIO.OUT)

        # Use the internal pull-down resistors
        GPIO.setup(self.C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



        # Detect the rising edges on the column lines of the
        # keypad. This way, we can detect if the user presses
        # a button when we send a pulse.
        GPIO.add_event_detect(self.C1, GPIO.RISING, callback=self.keypadCallback)
        GPIO.add_event_detect(self.C2, GPIO.RISING, callback=self.keypadCallback)
        GPIO.add_event_detect(self.C3, GPIO.RISING, callback=self.keypadCallback)
        GPIO.add_event_detect(self.C4, GPIO.RISING, callback=self.keypadCallback)
    

    def readKey(self):
        # If a button was previously pressed,
        # check, whether the user has released it yet
        if self.keypadPressed != -1:
            self.setAllLines(GPIO.HIGH)
            if GPIO.input(self.keypadPressed) == 0:
                self.keypadPressed = -1
            else:
                time.sleep(0.1)
        # Otherwise, just read the input
        else:   
            if self.input.__len__() == 0:
                self.readLine(self.L1, ["1","2","3","A"])
                self.readLine(self.L2, ["4","5","6","B"])
                self.readLine(self.L3, ["7","8","9","C"])
                self.readLine(self.L4, ["*","0","#","D"])
            else:
                key = self.input
                self.input = ""
                return key

    
    # This callback registers the key that was pressed
    # if no other key is currently pressed
    def keypadCallback(self, channel):
        if self.keypadPressed == -1:
            self.keypadPressed = channel


    # Sets all lines to a specific state. This is a helper
    # for detecting when the user releases a button
    def setAllLines(self, state):
        GPIO.output(self.L1, state)
        GPIO.output(self.L2, state)
        GPIO.output(self.L3, state)
        GPIO.output(self.L4, state)

   

    # reads the columns and appends the value, that corresponds
    # to the button, to a variable
    def readLine(self, line, characters):
        # We have to send a pulse on each line to
        # detect button presses
        GPIO.output(line, GPIO.HIGH)
        if(GPIO.input(self.C1) == 1):
            self.input = self.input + characters[0]
        if(GPIO.input(self.C2) == 1):
            self.input = self.input + characters[1]
        if(GPIO.input(self.C3) == 1):
            self.input = self.input + characters[2]
        if(GPIO.input(self.C4) == 1):
            self.input = self.input + characters[3]
        GPIO.output(line, GPIO.LOW)
