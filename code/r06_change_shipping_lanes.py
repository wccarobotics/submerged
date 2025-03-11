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

    br.driveForDistance(mm(13.7), 50)
    br.curve(mm(5), -45, 40)
    br.moveRightAttachmentMotorForDegrees(500, 30)
    br.moveRightAttachmentMotorForDegrees(-250, 100)
    br.driveForDistance(mm(-2),30)
    br.driveForDistance(mm(2),30)
    br.driveForDistance(mm(9.7), 50)
    br.curve(mm(5), -45, 40)
    br.driveForDistance(mm(2), 50)
    br.curve(mm(1), 80, 40)
    br.driveForDistance(mm(5))
    br.curve(0, 65, 50)
    br.driveForDistance(mm(-3),20)
    br.curve(0, 50, 40)
    br.driveForDistance(mm(14), 50)
    br.driveForDistance(mm(-6), 50)
    br.curve(0, 80, 40)
    br.driveForDistance(mm(24), 50)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
