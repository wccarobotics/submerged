from base_robot import *

# Copy this text into a new mission file. Name it something like
# r02_unexpected_encounter.  Don't use any spaces or punctuation,
# other than _. The name MUST end with .py
#
# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
#
# These existing comments can be deleted


def Run(br: BaseRobot):

    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    initial_heading = br.hub.imu.heading()

    # get to boat
    br.driveForDistance(mm(15), 50)
    br.curve(mm(2.5), -45, 40)
    br.driveForDistance(mm(0.7), 10)

    # rotate boat
    br.moveRightAttachmentMotorForDegrees(500, 30)
    br.driveForMillis(500, -30)

    # move atachment up(avoids getting caught on boat)
    wait(500)
    br.moveRightAttachmentMotorForDegrees(-250, 100)

    # get home
    br.curve(mm(-10), -45, 100, then=Stop.NONE)
    br.driveForMillis(1000, -100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
