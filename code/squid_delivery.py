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
    # br.driveForDistance(mm(1), 50, then=Stop.NONE)
    # br.curve(mm(5), -56, 25, then=Stop.NONE)
    # br.driveForDistance(mm(20.5), speedPct=50, then=Stop.NONE)  # often tweaked
    # br.turnInPlace(40, then=Stop.NONE)
    # br.driveForDistance(mm(8), speedPct=50, then=Stop.NONE)
    # br.turnInPlace(-50, then=Stop.NONE)
    # br.driveForDistance(mm(8), speedPct=50, then=Stop.NONE)
    # turn_angle = initial_heading - br.hub.imu.heading() - 20
    # br.curve(0, turn_angle, 30)  # often tweaked
    # br.driveForMillis(millis=750, then=Stop.NONE)
    # br.moveRightAttachmentMotorForDegrees(360)
    # br.turnInPlace(-45, then=Stop.NONE)
    # br.driveForDistance(mm(-6))

    br.driveForDistance(mm(3))
    br.turnInPlace(-54)
    br.driveForDistance(mm(25), speedPct=100, then=Stop.NONE)
    br.driveForDistance(mm(20), speedPct=50)
    br.turnInPlace(50)
    br.driveForMillis(500)
    br.moveRightAttachmentMotorForDegrees(360)
    br.driveForDistance(mm(-3))
    br.turnInPlace(-70)
    br.driveForDistance(mm(-10))


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
