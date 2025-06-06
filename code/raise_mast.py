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

    initial_heading = br.hub.imu.heading()

    # get aligned with mission model
    br.driveForDistance(mm(15), speedPct=35, then=Stop.NONE)
    br.curve(mm(6), 20, speedPct=45, then=Stop.NONE)
    br.driveForDistance(mm(7), 30, then=Stop.NONE)
    turn_angle = initial_heading - br.hub.imu.heading() + 90
    br.curve(mm(0),turn_angle, 40)

    # raise mast and grab chest
    br.driveForDistance(mm(3), 50, then=Stop.NONE)
    br.driveForMillis(1575, speedPct=9)
    br.driveForDistance(mm(-5), speedPct=-40, then=Stop.NONE)

    # get home
    br.curve(mm(-2), 55, 100, then=Stop.NONE)
    br.driveForMillis(1500, speedPct=-100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
