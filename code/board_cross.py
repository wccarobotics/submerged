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
    br.driveForDistance(mm(24), 50)
    br.curve(mm(8), -45, 40)
    br.driveForDistance(mm(3), 50)
    br.moveLeftAttachmentMotorForDegrees(120, 20)

    # grab
    br.driveForDistance(mm(-12), 100)
    br.moveLeftAttachmentMotorForDegrees(-200, 100)
    br.moveLeftAttachmentMotorForDegrees(100, 100)

    # get to the right side
    br.curve(mm(15), 52, 100)
    br.driveArcDist(mm(96), mm(48))


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
