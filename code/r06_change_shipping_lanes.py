from base_robot import *


def Run(br: BaseRobot):
    # start on right side, facing north, on the third small black notch from the edge of the mat
    # get to boat
    initial_heading = br.hub.imu.heading()

    br.driveForDistance(mm(14), 50)
    br.curve(mm(3.5), -45, 40)
    br.driveForDistance(mm(.5), 10)

    # rotate boat
    br.moveRightAttachmentMotorForDegrees(500, 30)
    br.driveForMillis(500, -30)
    br.driveForDistance(mm(2), 30)

    # move atachment up(avoids getting caught on boat)
    wait(500)
    br.moveRightAttachmentMotorForDegrees(-250, 100)

    # get to sonar
    print("Initial heading: " + str(initial_heading))
    print("Current heading: " + str(br.hub.imu.heading()))
    turn_angle = ((initial_heading - br.hub.imu.heading())) - 50
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(10.7), 50, accelerationPct=40, then=Stop.NONE)
    br.curve(mm(7), -30, 40)
    br.driveForDistance(mm(0.4), 50)

    # do sonar
    turn_angle = initial_heading - br.hub.imu.heading()
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(5.2), 10)
    turn_angle = initial_heading - br.hub.imu.heading()
    br.curve(0, turn_angle, 40)
    br.moveLeftAttachmentMotorForMillis(5500, 100)

    # get to sample
    br.driveForDistance(mm(-1))
    print("Initial heading: " + str(initial_heading))
    print("Current heading: " + str(br.hub.imu.heading()))
    turn_angle = ((initial_heading - br.hub.imu.heading())) + 88
    print("Turn angle: " + str(turn_angle))
    br.curve(0, turn_angle, 40)
    br.driveForDistance(mm(3), 50, then=Stop.NONE)
    br.moveLeftAttachmentMotorForDegrees(-1000, wait=False)
    br.driveForMillis(1000, 50)

    # return home
    br.driveForDistance(mm(-9), 100)
    br.curve(0, 70, 100)
    br.driveForDistance(mm(36), 100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
