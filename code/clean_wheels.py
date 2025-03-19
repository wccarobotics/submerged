from base_robot import *
from pybricks.tools import Matrix
import images


def Run(br: BaseRobot):
    br.hub.display.animate([images.CLEAN_WHEELS_1, images.CLEAN_WHEELS_2], 300)
    while not Button.CENTER in br.hub.buttons.pressed():
        br.driveForMillis(100, 40, gyro=False, accelerationPct=100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
