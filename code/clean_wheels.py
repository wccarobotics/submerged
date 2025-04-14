from base_robot import *
from pybricks.tools import Matrix
import images


def Run(br: BaseRobot):
    br.hub.display.animate([images.CLEAN_WHEELS_1, images.CLEAN_WHEELS_2], 300)
    while not Button.CENTER in br.hub.buttons.pressed():
        if Button.RIGHT in br.hub.buttons.pressed():
            br.leftDriveMotor.run(500)
            br.rightDriveMotor.stop()
        if Button.LEFT in br.hub.buttons.pressed():
            br.rightDriveMotor.run(500)
            br.leftDriveMotor.stop()


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
