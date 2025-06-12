from base_robot import *
from pybricks.tools import StopWatch


def Run(br: BaseRobot):
    # start on right side, facing north, on the third small black notch from the edge of the mat
    # get to boat
    initial_heading = br.hub.imu.heading()

    br.driveForDistance(mm(14.5), 50)
    br.curve(mm(3.5), -45, 40)
    br.driveForDistance(mm(.5), 10)

    # get to sonar
    turn_angle = ((initial_heading - br.hub.imu.heading())) - 50
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(10.7), 50, accelerationPct=40, then=Stop.NONE)
    br.curve(mm(7), -30, 40)
    br.driveForDistance(mm(.8), 50)

    # do sonar
    turn_angle = initial_heading - br.hub.imu.heading()
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(5.2), 10)
    br.driveForDistance(1, 10, then=Stop.NONE)
    timer = StopWatch()
    while (
        abs(initial_heading - br.hub.imu.heading()) <= 5
        and timer.time() <= 500
    ):
        pass
    br.driveForDistance(0)
    turn_angle = initial_heading - br.hub.imu.heading()
    print(turn_angle)
    br.curve(mm(-4), -turn_angle, 40)
    br.moveLeftAttachmentMotorForMillis(5500, 100)
    br.moveLeftAttachmentMotorForMillis(200, -100)

    # get to sample
    br.driveForDistance(mm(-4.5))
    turn_angle = ((initial_heading - br.hub.imu.heading())) + 65
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(3), 50, then=Stop.NONE)
    br.moveLeftAttachmentMotorForDegrees(-1000, wait=False)
    br.driveForMillis(1000, 50)

    # return home
    br.driveForDistance(mm(-9), 100)
    br.curve(0, 90, 100)
    br.driveForDistance(mm(36), 100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)