from base_robot import *

# Copy this text into a new mission file. Name it something like
# myname.py. You can name it pretty much anything, but don't use
# any spaces or punctuation, other than _ and -. The name MUST
# end with .py (unlike this file, which ends with .txt)
#
# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
# Please delete all of these comments, and consider writing your
# own here.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    wait(250)
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

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


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
