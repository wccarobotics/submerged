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
    # use negative distance when driving backwards not negative speed

    # get to coral and diver
    br.driveArcDist(mm(35.4), mm(26), 50)
    br.driveForDistance(mm(5.8), speedPct=45)
    br.moveRightAttachmentMotorForDegrees(180, 20)
    br.turnInPlace(-135, 30)
    br.moveRightAttachmentMotorForDegrees(-180, 20)

    # raise coral buds
    br.driveForDistance(mm(5.5), speedPct=20)

    # grab diver
    br.moveRightAttachmentMotorForDegrees(190, speedPct=20)
    wait(500)

    # visit Marcus
    br.driveForDistance(mm(-6), speedPct=50, accelerationPct=30)
    wait(500)
    br.turnInPlace(35)
    br.driveForDistance(mm(9.7), speedPct=20)
    wait(40)

    # say good bye to marcus
    br.driveForDistance(mm(-9.2), speedPct=40, accelerationPct=30)

    # back up
    br.turnInPlace(35, 40)
    br.driveForDistance(-mm(2), 40)

    # align with coral reef
    br.turnInPlace(30, 20)
    br.driveForMillis(60, 50)
    br.driveForDistance(mm(-3), speedPct=30)

    # lower diver
    br.moveRightAttachmentMotorForDegrees(-120, speedPct=15)
    wait(50)

    # deliver diver
    br.turnInPlace(-10)
    br.driveForDistance(mm(7.5), speedPct=20)
    wait(60)
    br.moveRightAttachmentMotorForDegrees(-120, 100)

    # get home
    br.driveArcDist(mm(-20), mm(-10), 30, accelPct=30)
    br.driveForDistance(mm(-24), 100)


# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
