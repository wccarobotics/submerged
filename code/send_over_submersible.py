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
    br.driveForDistance(mm(7.5), 50)
    br.curve(350, -52)
    br.driveForDistance(mm(19), 40)
    br.curve(0, 10)
    br.driveForDistance(mm(10), 50)
    br.driveForDistance(mm(-8), 20)
    br.driveForDistance(mm(9), 100)
    br.driveForDistance(mm(-6), 50)
    br.curve(0, 25, 30)
    br.driveForDistance(mm(-4),50)
    br.curve(0, -50, 50)
    br.curve(mm(80), 16, 50)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
