from base_robot import *


def Run(br: BaseRobot):
    wait(250)

    br.curve(250, -65)
    br.driveForDistance(300)
    br.curve(250, 20)
    br.driveForDistance(400, speedPct=50)
    br.driveForDistance(200, speedPct=25)
    br.curve(-250, 25)
    br.driveForDistance(-175)
    br.turnInPlace(75)
    br.driveForDistance(-175)
    br.moveLeftAttachmentMotorForDegrees(-90)
    br.driveForDistance(-150)
    br.curve(-125, -75)
    br.curve(125, 10)
    br.driveForDistance(500)
    br.curve(250, 90)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
