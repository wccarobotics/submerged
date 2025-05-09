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
    br.curve(mm(8), -45, 40, then=Stop.NONE)
    br.driveForDistance(mm(3), 50)
    br.moveLeftAttachmentMotorForDegrees(160, 20)

    # grab
    br.driveForDistance(mm(-7), 100)
    br.driveForDistance(mm(2))
    br.moveLeftAttachmentMotorForDegrees(-125, 100)
    br.moveLeftAttachmentMotorForDegrees(100, 100)
    br.driveForMillis(500, 30)
    br.driveForDistance(mm(-5))

    # get to crabs
    br.turnInPlace(54)
    br.driveForDistance(mm(7.5), 50, then=Stop.NONE)
    br.driveForMillis(500, speedPct=25)
    br.turnInPlace(5)
    timer = StopWatch()
    while (
        abs(initial_heading - br.hub.imu.heading()) <= 5
        and timer.time() <= 500
    ):
        pass

    # do crabs
    br.moveLeftAttachmentMotorForDegrees(-150, wait=False)
    br.moveRightAttachmentMotorForDegrees(219, 50)
    wait(50)
    br.driveForDistance(mm(-7.7), 80)
    br.moveRightAttachmentMotorForDegrees(-300)

    # get to squid
    turn_angle = initial_heading - br.hub.imu.heading() - 0
    print(turn_angle)
    br.turnInPlace(turn_angle, 30)
    br.driveForDistance(mm(-3), 50, then=Stop.NONE)
    br.driveArcDist(mm(-14), mm(5), then=Stop.NONE)
    br.driveArcDist(mm(17), mm(6))
    br.driveForDistance(mm(4))
    br.driveArcDist(mm(30), mm(18))
    br.turnInPlace(27)
    br.driveForMillis(1000, -75)
    br.driveForDistance(mm(36))


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
