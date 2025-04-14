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
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # The Robot must be aligned along the South Wall and againt the Square and Rectagle Aligners. Squid must be facing forward
    initial_heading = br.hub.imu.heading()

    # get to mission model
    br.driveForDistance(mm(3), 50, then=Stop.NONE)
    br.curve(mm(5), -56, 25, then=Stop.NONE)
    br.driveForDistance(mm(23), 50, then=Stop.NONE)
    br.turnInPlace(45, 50)
    br.driveForDistance(mm(4), 50)

    # angler fish
    br.turnInPlace(-47)
    br.driveForDistance(mm(5), 40)
    br.curve(mm(3), -35)
    br.driveForDistance(mm(3.2), 50)
    turn_angle = ((initial_heading - br.hub.imu.heading()-20))
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(10), 50)
    br.moveRightAttachmentMotorForDegrees(300)
    br.driveArcDist(mm(10), mm(-6), -50, then=Stop.NONE)
    br.driveForDistance(mm(-9))

# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
