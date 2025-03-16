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
    # please do not use unnecessary waits and maybe don't use variables

    # get to coral and diver
    br.driveArcDist(mm(35.4), mm(26))
    br.driveForDistance(mm(7.2), speedPct=45)
    br.turnInPlace(223, 30)

    # raise coral buds
    br.driveForDistance(mm(6), speedPct=40)

    # grab diver
    br.moveRightAttachmentMotorForDegrees(85, speedPct=30)

    # visit Marcus
    br.waitForMillis(30)
    br.driveForDistance(mm(-6), speedPct=50)
    br.waitForMillis(500)
    br.turnInPlace(37.5)
    br.driveForDistance(mm(9.2), speedPct=40)
    br.waitForMillis(40)

    # say good bye to marcus
    br.driveForDistance(mm(-9.2), speedPct=-40)

    # align with coral reef
    br.turnInPlace(65)
    br.driveForMillis(60)
    br.driveForDistance(mm(-7), speedPct=40)

    # lower diver
    br.moveRightAttachmentMotorForDegrees(-42, speedPct=4)
    br.waitForMillis(50)

    # deliver diver
    br.turnInPlace(-13)
    br.driveForDistance(mm(8.5), speedPct=20)
    br.waitForMillis(60)
    br.moveRightAttachmentMotorForDegrees(-40.4, speedPct=3)

    # get home
    br.driveArcDist(mm(-24), mm(-12), 40)



# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
