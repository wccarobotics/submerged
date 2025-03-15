from base_robot import *
from pybricks.tools import Matrix

CLEAN_WHEELS_1 = Matrix(
    [
        [0, 100, 100, 100, 0],
        [100, 0, 50, 0, 100],
        [100, 50, 100, 50, 100],
        [100, 0, 50, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)

CLEAN_WHEELS_2 = Matrix(
    [
        [0, 100, 100, 100, 0],
        [100, 50, 0, 50, 100],
        [100, 0, 100, 0, 100],
        [100, 50, 0, 50, 100],
        [0, 100, 100, 100, 0],
    ]
)


def Run(br: BaseRobot):
    frame = 0
    while not Button.CENTER in br.hub.buttons.pressed():
        frame += 0.2
        if frame > 1:
            frame = -0.1
        if frame < 0.5:
            br.hub.display.icon(CLEAN_WHEELS_1)
        if frame >= 0.5:
            br.hub.display.icon(CLEAN_WHEELS_2)
        br.driveForMillis(100, 25, gyro=False, accelerationPct=100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
