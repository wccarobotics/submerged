from base_robot import *
from pybricks.tools import StopWatch

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
    # start on left side with the square aligner at the corner of the mat. put robot north of the square aligner facing east. have arm all the way up
    # get to mission model and lower atatchment
    initial_heading = br.hub.imu.heading()
    br.moveRightAttachmentMotorForDegrees(-200, wait=False)
    br.driveForDistance(mm(22), 50, then=Stop.NONE)
    br.moveLeftAttachmentMotorForDegrees(160, 20, wait=False)
    br.curve(mm(8), -45, 40, then=Stop.NONE)
    br.driveForDistance(mm(7), 50)

    # grab
    br.moveLeftAttachmentMotorForDegrees(-100, wait=False)
    br.driveForDistance(mm(-9), 100)

    # get to crabs
    br.turnInPlace(55)
    br.driveForDistance(mm(7.5), 50, then=Stop.NONE)
    br.driveForMillis(500, speedPct=25)
    br.turnInPlace(10)
    timer = StopWatch()
    while (
        abs(initial_heading - br.hub.imu.heading()) <= 5
        and timer.time() <= 500
    ):
        pass

    # do crabs
    br.moveRightAttachmentMotorForDegrees(219, 50)
    wait(50)
    br.driveForDistance(mm(-8.5), 80)
    br.moveRightAttachmentMotorForDegrees(-300)

    # get to squid
    turn_angle = initial_heading - br.hub.imu.heading() - 0
    print(turn_angle)
    br.turnInPlace(turn_angle, 30)
    br.driveForDistance(mm(-3), 50, then=Stop.NONE)
    br.driveArcDist(mm(-14), mm(5), then=Stop.NONE)
    br.driveArcDist(mm(17), mm(6), then=Stop.NONE)
    br.driveForDistance(mm(4), then=Stop.NONE)
    br.driveArcDist(mm(30), mm(18))
    br.turnInPlace(27)
    br.driveForMillis(1000, -75)
    print("Initial heading: " + str(initial_heading))
    print("Current heading: " + str(br.hub.imu.heading()))
    turn_angle = ((initial_heading - br.hub.imu.heading())) + 45
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(36))


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
