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

    br.curve(mm(10), -65, speedPct=50)

    br.driveForDistance(mm(14), speedPct=-50)
    # br.driveForDistance(mm(-18), speedPct=-50)

    br.turnInPlace(25)
    br.driveForDistance(mm(12), speedPct=-50)

    br.curve(mm(12), -65, speedPct=50)


    
 


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
