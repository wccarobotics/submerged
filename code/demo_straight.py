from base_robot import *

# use this program to show the juges the gyro while driving straight


def Run(br: BaseRobot):

    br.driveForDistance(mm(120), 50)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
