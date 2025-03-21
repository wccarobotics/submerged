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
    # start on right side, facing north, on the third small black notch from the edge of the mat
    # get to boat
    initial_heading = br.hub.imu.heading()

    br.driveForDistance(mm(13.5), 50)
    br.curve(mm(5), -45, 40)

    # rotate boat
    br.moveRightAttachmentMotorForDegrees(500, 30)

    # move atachment up(avoids getting caught on boat)
    wait(500)
    br.moveRightAttachmentMotorForDegrees(-250, 100)

    # get to sonar
    br.driveForDistance(mm(-2), 30)
    br.driveForDistance(mm(2), 30)
    br.driveForDistance(mm(9.7), 50, accelerationPct=40)
    br.curve(mm(7), -30, 40)
    br.driveForDistance(mm(5), 50)

    # do sonar
    br.curve(mm(0), 75, 40)
    br.driveForDistance(mm(5), 50)
    br.curve(0, 65, 50)
    br.driveForDistance(mm(-3),20)

    # get to sample
    print("Initial heading: " + str(initial_heading))
    print("Current heading: " + str(br.hub.imu.heading()))
    turn_angle = ((initial_heading - br.hub.imu.heading())) + 80
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(18), 50)

    # return home
    br.driveForDistance(mm(-8), 100)
    br.curve(0, 80, 100)
    br.driveForDistance(mm(24), 100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
