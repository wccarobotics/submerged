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

    initial_heading = br.hub.imu.heading()

    br.driveForDistance(distance=1000)  # Go forward
    br.driveForDistance(distance=-1000)  # Go back

    # relative to start gyro turn
    print("Initial heading: " + str(initial_heading))
    print("Current heading: " + str(br.hub.imu.heading()))
    turn_angle = ((initial_heading - br.hub.imu.heading())) + 0
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
