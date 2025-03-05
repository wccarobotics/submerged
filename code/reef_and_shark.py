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
    # br.moveRightAttachmentMotorForDegrees(mm(-1.3), speedPct=-20) # -- If i need to move the scuba diver one at the start 👌
    a = -2.4
    b = 31
    pos_distance_to_yellow_thing = 2.5
    neg_distance_to_yellow_thing = -pos_distance_to_yellow_thing
    br.driveArcDist(mm(34), mm(b))
    br.waitForMillis(80)
    br.turnInPlace(-139.15)
    br.moveRightAttachmentMotorForDegrees(mm(0.7), speedPct=20)
    br.waitForMillis(70)
    br.driveForDistance(mm(4.1), speedPct=50)
    br.moveRightAttachmentMotorForDegrees(mm(1.37), speedPct=20)
    br.waitForMillis(30)
    br.moveRightAttachmentMotorForDegrees(mm(1.6), speedPct=-20)
    br.driveForDistance(mm(neg_distance_to_yellow_thing), speedPct=-43)
    br.waitForMillis(60)
    br.turnInPlace(40)
    br.waitForMillis(43)
    br.driveForDistance(mm(8), speedPct=80)
    br.waitForMillis(40)
    br.driveForDistance(mm(-8), speedPct=-80)
    br.turnInPlace(42)
    br.driveForMillis(60)
    br.moveRightAttachmentMotorForDegrees(mm(a - 0.36), speedPct=20)
    br.driveForDistance(mm(4), speedPct=-40)
    br.waitForMillis(60)


# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
