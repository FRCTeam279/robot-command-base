import math

from wpilib.command import Command
import subsystems
import oi

class TankDriveTeleopDefaultSkid(Command):
    '''
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    '''


    def __init__(self):
        super().__init__('TankDriveTeleopDefaultSkid')
        self.requires(subsystems.driveline)
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)
    

    def execute(self):
        # the two axis are multiplied by -1.0 because the joystick values are negative for pushing forward and right
        # which is not what most coders/drivers will expect
        subsystems.driveline.driveRaw(oi.leftDriverStick.getY() * -1.0, oi.rightDriverStick.getY() * -1.0)

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False
    
    
    