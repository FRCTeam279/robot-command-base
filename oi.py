import math
from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

import robotmap
#from commands.navxresetyawangle import NavxResetYawAngle

class T16000M(Joystick):
    def __init__(self, port):
        super().__init__(port)
        self.port = port
        self.setXChannel(0)
        self.setYChannel(1)
        self.setZChannel(2)
        self.setThrottleChannel(3)
        self.setTwistChannel(2)


# ----------------------------------------------------------
# Config Values
# ----------------------------------------------------------

class ConfigHolder:
    pass


config = ConfigHolder()

# Driver Sticks
config.leftDriverStickNullZone = 0.1
config.rightDriverStickNullZone = 0.08

config.throttleFilterPower = 0.4
config.turnFilterPower = 0.4

# Left Joystickc
#config.btnDriveSlow = 1
#config.btnResetEncodersIndex = 2

# Right Joystick
config.btnResetYawAngleIndex = 2


# ----------------------------------------------------------
# Stick and Button Objects
# ----------------------------------------------------------

leftDriverStick = None
rightDriverStick = None
#resetYawBtn = None


# ----------------------------------------------------------
# Init
# ----------------------------------------------------------


def init():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    global leftDriverStick
    global rightDriverStick

    try:
        leftDriverStick = T16000M(0)
    except:
        print('OI: Error - Could not instantiate Left Driver Stick on USB port 0!!!')

    try:
        rightDriverStick = T16000M(1)
    except:
        print('OI: Error - Could not instantiate Right Driver Stick on USB port 0!!!')


    # ----------------------------------------------------------
    # Driver Controls
    # ----------------------------------------------------------
    #global resetYawBtn
    #resetYawBtn = JoystickButton(rightDriverStick, config.btnResetYawAngleIndex)
    #resetYawBtn.whenPressed(NavxResetYawAngle())




