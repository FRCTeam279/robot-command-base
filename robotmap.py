import math

import wpilib


class ConfigHolder:
    """Dummy class to add config parameters too"""
    pass

# ----------------------------------------------------------
# Driveline Subsystem Config
# ----------------------------------------------------------
driveLine = ConfigHolder()
driveLine.leftMotorPort = 0
driveLine.rightMotorPort = 1
driveLine.invertLeft = True
driveLine.invertRight = False
driveLine.speedControllerType = "TALON"

print("RobotMap module completed load")

