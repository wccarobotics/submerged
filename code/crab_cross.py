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
    # start on left side with the square aligner at the corner of the mat. put robot north of the square aligner facing east. have arm all the way up
    # get to mission model and lower atatchment
    br.moveRightAttachmentMotorForDegrees(-200, wait=False)
    br.driveForDistance(mm(24), 50, then=Stop.NONE)
    br.curve(mm(8), -45, 40, then=Stop.NONE)
    br.driveForDistance(mm(3), 50)
    br.moveLeftAttachmentMotorForDegrees(100, 20)

    # grab
    br.driveForDistance(mm(-10), 100)
    br.moveLeftAttachmentMotorForDegrees(-125, 100)
    br.moveLeftAttachmentMotorForDegrees(100, 100)

    # get to crabs
    br.turnInPlace(47)
    br.driveForDistance(mm(13.5), 50, then=Stop.NONE)
    br.driveArcDist(mm(3), mm(1), 40)

    # do crabs
    br.moveRightAttachmentMotorForDegrees(200, 50)
    wait(50)
    br.driveForDistance(mm(-8.5), 80)
    br.moveRightAttachmentMotorForDegrees(-300)
    br.driveForDistance(mm(-2), 50, then=Stop.NONE)
    br.driveArcDist(mm(-11.5), mm(5))
    br.driveArcDist(mm(26), mm(24), then=Stop.NONE)
    br.turnInPlace(22)
    br.driveForDistance(mm(-24))
    br.driveForDistance(mm(36))
    #br.driveForDistance(mm(24))


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
