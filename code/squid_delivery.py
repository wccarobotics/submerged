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
    # The Robot must be lined up along the South Wall using the Square Aligner.
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # The Robot must be aligned along the South Wall and againt the Square and Rectagle Aligners.

    br.curve(mm(5), -40, speedPct=25)
    br.driveForDistance(mm(24.5))
    br.turnInPlace(17.5)
    br.driveForDistance(mm(-4.5))
    br.turnInPlace(-25)
    br.driveForDistance(mm(-10))
    br.turnInPlace(-20)
    br.driveForDistance(mm(-30))


    
 


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
