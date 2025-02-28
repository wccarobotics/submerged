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
    # br.moveRightAttachmentMotorForDegrees(mm(-4), speedPct=-20) # -- If i need to move the scuba diver one at the start 👌
    br.driveArcDist(mm(40), mm(31))
    br.waitForMillis(80)
    br.turnInPlace(-132)
    br.waitForMillis(70)
    br.driveForDistance(mm(4), speedPct=50)
    br.waitForMillis(40)
    br.moveRightAttachmentMotorForDegrees(mm(-4), speedPct=-20)
    br.driveForDistance(mm(-4), speedPct=-50)
    br.waitForMillis(60)
    br.turnInPlace(43)
    br.waitForMillis(60)
    br.driveForDistance(mm(9), speedPct=80)
    br.waitForMillis(40)
    br.driveForDistance(mm(-9), speedPct=-80)
    br.waitForMillis(60)
    br.turnInPlace(75)
    br.driveForMillis(60)
    br.driveForDistance(mm(-23), speedPct=-80)
    br.waitForMillis(60)

# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
