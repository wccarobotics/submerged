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
    # Start on right side on the corner facing north
    # drive to mission
    br.driveForDistance(mm(7.5), 50)
    br.curve(350, -52)
    br.driveForDistance(mm(19), 50)

    # get aligned
    br.curve(0, 10)

    # first push
    br.driveForDistance(mm(9.5), 50)
    br.driveForDistance(mm(-7.5), 20)

    # second push(for reliability)
    br.driveForDistance(mm(8.5), 100)
    br.driveForDistance(mm(-6), 50)

    # turn to leave mission model
    br.curve(0, 25, 30)

    # leave mission model
    br.driveForDistance(mm(-4.5),50)

    # head towards sample
    br.curve(0, -50, 50)
    br.curve(mm(55), 14, 50)
    br.driveForDistance(mm(2), 50)

    # knock sample out
    br.curve(0, -45, 60)
    br.driveForDistance(mm(1), 50)
    br.curve(0, 30)
    
    # get home
    br.driveForDistance(mm(-24), 100)
    br.curve(mm(-4), -45, 100)
    br.driveForDistance(mm(-36), 100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
