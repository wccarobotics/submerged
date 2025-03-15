from base_robot import *

# use this program to show the juges the gyro while turning


def Run(br: BaseRobot):

    br.curve(mm(8), 90, 50)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
