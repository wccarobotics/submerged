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
    br.driveForDistance(mm(5.8), speedPct=45, then=Stop.NONE)
    br.moveRightAttachmentMotorForDegrees(200, 20, wait=False)
    br.turnInPlace(-135, -30)

    # gyro to start turn for MOAR RELIABILITY!
    br.moveRightAttachmentMotorForDegrees(-230, 20) # wait=False should be at the end of this line of code
    print("Initial heading: " + str(initial_heading))
    print("Current heading: " + str(br.hub.imu.heading()))
    turn_angle = ((initial_heading - br.hub.imu.heading())) - 92
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)

    # raise coral buds & grab diver
    br.driveForDistance(mm(3), speedPct=20, then=Stop.NONE)
    br.driveForDistance(mm(3), speedPct=20, wait=False)
    br.moveRightAttachmentMotorForDegrees(210, speedPct=20)
    #wait(500)

    # visit Marcus
    br.driveForDistance(mm(-4), speedPct=50, accelerationPct=30)
    br.turnInPlace(35, then=Stop.NONE)
    br.driveForDistance(mm(8.7), speedPct=50)

    # say good bye to marcus
    br.driveForDistance(mm(-10), speedPct=40, accelerationPct=30)

    # align with coral reef
    turn_angle = ((initial_heading - br.hub.imu.heading())) - 0
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)

    # deliver diver
    br.moveRightAttachmentMotorForDegrees(-90, speedPct=15)
    br.waitForMillis(500)
    br.driveForDistance(mm(1), speedPct=50)
    br.moveRightAttachmentMotorForDegrees(-100, speedPct=15)

    

    # get home
    turn_angle = ((initial_heading - br.hub.imu.heading())) + 35
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)
    br.driveForMillis(3000, speedPct=-100)


# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
