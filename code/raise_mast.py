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
    # The Robot must be aligned on the South Wall against the Square Aligner
    br.driveForDistance(mm(12.4), speedPct=50)
    br.curve(mm(10), 90, speedPct=50)
    br.driveForMillis(1575, speedPct=9)
    br.driveForDistance(mm(-10), speedPct=-40)
    br.turnInPlace(85)
    br.curve(330, 25)
    br.driveForDistance(mm(20), speedPct=35)

# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)



