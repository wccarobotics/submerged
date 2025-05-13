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
    # please do not use unnecessary waits and maybe don't use variables
    # use negative distance when driving backwards not negative speed

    # get to coral and diver
    initial_heading = br.hub.imu.heading()
    br.driveArcDist(mm(35.4), mm(26), 50, then=Stop.NONE)
    br.driveForDistance(mm(5.8), speedPct=45)
    br.moveRightAttachmentMotorForDegrees(200, 20, wait=False)
    br.turnInPlace(-135, -30)

    # gyro to start turn for MOAR RELIABILITY!
    br.moveRightAttachmentMotorForDegrees(-230, 20)
    print("Initial heading: " + str(initial_heading))
    print("Current heading: " + str(br.hub.imu.heading()))
    turn_angle = ((initial_heading - br.hub.imu.heading())) - 92
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)

    # raise coral buds
    br.driveForDistance(mm(6), speedPct=20)

    # grab diver
    br.moveRightAttachmentMotorForDegrees(210, speedPct=20)
    wait(500)

    # visit Marcus
    br.driveForDistance(mm(-4), speedPct=50, accelerationPct=30)
    wait(500)
    br.turnInPlace(35, then=Stop.NONE)
    br.driveForDistance(mm(8.7), speedPct=50)
    wait(40)

    # say good bye to marcus
    br.driveForDistance(mm(-9.2), speedPct=40, accelerationPct=30)

    # back up
    br.turnInPlace(35, 40)
    br.driveForDistance(-mm(2), 40)

    # align with coral reef
    br.turnInPlace(30, 20)
    br.driveForMillis(60, 50, then=Stop.NONE)
    br.driveForDistance(mm(-5.6), speedPct=30)

    # lower diver
    br.moveRightAttachmentMotorForDegrees(-55, speedPct=15)
    wait(50)

    # deliver diver
    br.turnInPlace(-17)
    br.driveForDistance(mm(10), speedPct=20)
    wait(60)
    br.moveRightAttachmentMotorForDegrees(-155, 100)

    # get home
    br.driveForDistance(mm(-2), speedPct=10, then=Stop.NONE)
    br.driveArcDist(mm(-20), mm(-10), 30, accelPct=30, then=Stop.NONE)
    br.driveForDistance(mm(-24), 100)


# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
