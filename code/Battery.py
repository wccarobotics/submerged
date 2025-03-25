from base_robot import *
from pybricks.tools import Matrix
import images


def Run(br: BaseRobot):
    while not Button.CENTER in br.hub.buttons.pressed():
                v = br.hub.battery.voltage()
                vPct = RescaleBatteryVoltage(v)
                br.hub.display.number(vPct)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
