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
    # First Script
    # br.driveForDistance(mm(15), speedPct=50)
    # br.waitForMillis(500)
    # br.curve(mm(1.2), -15, speedPct=34)
    # br.driveForDistance(mm(1.5), speedPct=20)
    # br.turnInPlace(50)
    # br.driveForDistance(mm(-2), speedPct=35)
    # br.driveForDistance(mm(4), speedPct=45)
    # br.curve(mm(2.4), 25, speedPct=70)
    # br.curve(mm(-2.4), 25, speedPct=70)
    # br.driveForDistance(mm(-15))
    # br.waitForMillis(2500)
    # Second Script
    br.driveForDistance(mm(6.5), speedPct=50)
    br.waitForMillis(50)
    br.curve(mm(11), 37, speedPct=90)
    br.curve(mm(11), -37, speedPct=90)
    br.moveLeftAttachmentMotorForDegrees(mm(3), speedPct=-50)
    br.curve(mm(6), 31, speedPct=20)
    br.driveForDistance(mm(-0.7))
    br.curve(mm(-6), 31, speedPct=20)
    br.driveForDistance(mm(8), speedPct=70)
    br.moveLeftAttachmentMotorForDegrees(-240)
    br.turnInPlace(-9)
    br.driveForDistance(mm(14), speedPct=70)


# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
