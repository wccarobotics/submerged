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
    # get to tree
    br.moveLeftAttachmentMotorForDegrees(220, .5, wait=False)
    br.driveForDistance(mm(26), 50)
    # raise arm
    br.moveLeftAttachmentMotorForDegrees(-360, .01)
    br.driveForDistance(mm(-24), speedPct=100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
