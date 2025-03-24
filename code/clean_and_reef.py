from base_robot import *


def Run(br: BaseRobot):
    # Start on left side. Make a line between robot, debris, and mission. Place robot on the line facing misssion. If this is hard use the one skill you learned in the hours you wasted on fortnite and aim. That simple! Oh wait, you use aimbot and can't aim. Imagine getting roasted at your fortnite skills by someone who doesn't even play fortnite. Imagine!
    # get to mission and clean
    br.driveForDistance(mm(36), 60)
    br.driveForDistance(mm(-48), 100)


# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
