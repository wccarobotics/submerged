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
    br.curve(mm(4), -55)
    br.driveForDistance(mm(15), speedPct=100)
    turn_angle = initial_heading - br.hub.imu.heading() - 48
    print(turn_angle)
    br.driveForDistance(mm(10))
    turn_angle = initial_heading - br.hub.imu.heading() - 45
    print(turn_angle)
    # br.curve(mm(12), 26, speedPct=40)
    # br.curve(mm(12), -30)
    # br.driveForDistance(mm(8))

    # turn_angle = initial_heading - br.hub.imu.heading() - 52
    # print(turn_angle)
    # br.turnInPlace(turn_angle, 30)  # often tweaked
    # br.driveForDistance(mm(15), speedPct=50)
    # turn_angle = initial_heading - br.hub.imu.heading() - 52
    # print(turn_angle)
    # br.turnInPlace(turn_angle, 30)  # often tweaked
    # br.driveForDistance(mm(4))
    # br.curve(mm(20), -30, speedPct=100, accelerationPct=50)
    # turn_angle = initial_heading - br.hub.imu.heading() - 0
    # print(turn_angle)
    # br.turnInPlace(turn_angle, 30)
    # br.driveForMillis(1000, speedPct=20)
    # br.moveRightAttachmentMotorForDegrees(360)
    # br.driveForDistance(mm(-3))
    # br.turnInPlace(90)
    # br.moveRightAttachmentMotorForDegrees(-360)
    # br.driveForDistance(mm(5))
    # turn_angle = initial_heading - br.hub.imu.heading() + 20
    # br.turnInPlace(turn_angle, 30)  # often tweaked
    # br.moveRightAttachmentMotorForDegrees(360, speedPct=25, wait=False)
    # br.driveForMillis(500)
    # wait(2000)
    # br.driveForDistance(mm(-3))
    # turn_angle = initial_heading - br.hub.imu.heading() + 135
    # br.turnInPlace(turn_angle, 30)  # often tweaked
    # br.driveForDistance(mm(6))
    # br.turnInPlace(-60)
    # br.driveForDistance(mm(-2))


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
