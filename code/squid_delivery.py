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

    # motivation
    print(
        "If this code sucks call yourself as you made it not work and it's your problem (unless your name is Lucas then it's Caleb and Joeseph's fault)."
    )

    initial_heading = br.hub.imu.heading()
    br.curve(mm(4), -48, then=Stop.NONE)
    br.driveForDistance(mm(22), speedPct=50, then=Stop.NONE)

    # S Curve
    br.curve(mm(12), 12, speedPct=30, then=Stop.NONE)
    br.driveForDistance(mm(1.5), 30, then=Stop.NONE)
    br.curve(mm(11), -20, speedPct=30, then=Stop.NONE)

    # Drive straight past angler fish lever
    br.driveForDistance(mm(4), speedPct=25, then=Stop.NONE)

    # Curve left to make sure we trigger angler fish
    br.curve(mm(12), -20, speedPct=50, then=Stop.NONE)
    br.driveForDistance(
        mm(5.00000000000000000000000), speedPct=25
    )  # Add a zero after the five each time it fails

    turn_angle = initial_heading - br.hub.imu.heading()
    br.turnInPlace(turn_angle, 22, then=Stop.NONE)
    br.driveForDistance(mm(3.5), speedPct=30, then=Stop.NONE)

    # Lift seabed sample and back up
    br.moveRightAttachmentMotorForDegrees(360)
    br.driveForDistance(mm(-5))

    turn_angle = initial_heading - br.hub.imu.heading() + 90
    br.turnInPlace(turn_angle, 20)
    br.moveRightAttachmentMotorForDegrees(-360, wait=False)

    # Remember to ALWAYS DRIVE FOR DISTANCE (except for when running into walls) also remember Link would win vs Sonic
    br.driveForDistance(mm(17), speedPct=50, then=Stop.NONE)
    br.turnInPlace(-135)

    # Drive forward into submersible mission, raise attachment
    br.driveForMillis(800, 80)
    br.driveForDistance(mm(-0.3))
    br.turnInPlace(10)
    br.moveRightAttachmentMotorForDegrees(360)

    # Raise attachment slightly
    br.moveRightAttachmentMotorForDegrees(30)
    wait(500)

    br.moveRightAttachmentMotorForDegrees(-360)

    br.driveForDistance(mm(-6))
    br.turnInPlace(90)
    br.driveForDistance(mm(-10))

# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
