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
    br.waitForMillis(60)
    br.driveForDistance(mm(9.3), speedPct=70)
    br.waitForMillis(60)
    br.turnInPlace(93.5)
    br.driveForDistance(mm(18), speedPct=79)
    br.waitForMillis(50)
    br.moveLeftAttachmentMotorForDegrees(mm(2), speedPct=-20)
    br.waitForMillis(50)
    # br.driveArcDist(mm(-56), mm(20), speedPct=23)
    br.driveForDistance(mm(20), speedPct=20)

# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
