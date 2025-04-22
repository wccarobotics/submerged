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
    for i in range(4):
        pass
# br.driveForDistance(distance=500)  # Go fofoward
    # br.curve(mm(10), 90)
    # br.driveForDistance(distance=500)  # Go forward
    # br.curve(mm(10), 90)
    # br.driveForDistance(distance=500)  # Go fofoward
    # br.curve(mm(10), 90)  # Go forward
        
     

# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
