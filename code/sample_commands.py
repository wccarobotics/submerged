from base_robot import *

# This file shows different commands you can run, with comments that explain
# what they do.


def Run(br: BaseRobot):

    # This will wait for 250 milliseconds.  You might want to do this at the
    # beginning of a mission to give yourself time to move your hand away
    # after pressing the button.
    # You might use it during a mission if there could be parts that are
    # swinging and you want to give them time to stop
    br.waitForMillis(250)

    # This drives forward for 100 mm (10 cm)
    br.driveForDistance(100)

    # If you want to use inches, you can use the mm conversion function.
    # This will drive for 10 inches
    br.driveForDistance(mm(10))

    # You can also control the speed.  This drives 10 inches at 25% speed
    br.driveForDistance(mm(10), speedPct=25)

    # If you want to go backwards, you can use a negative speed.
    # This will go backwards for 10 inches at 50% speed
    br.driveForDistance(mm(10), speedPct=-50)

    br.driveForMillis(500)

    # br.driveForMillis(2000, 50)
    # br.driveForDistance(-1000)

    br.driveForDistance(distance=1000)  #    Drive distance
    # br.turnInPlace(angle=180)
    br.driveForDistance(distance=-1000)  #    Drive distance
    # br.turnInPlace(angle=180)
    # br.moveLeftAttachmentMotorForDegrees(degrees=-720)
    # br.waitForForwardButton()
    # # br.driveUntilStalled(speedPct=80, stallPct=5)
    # # br.driveUntilStalled(speedPct=80)
    # br.moveRightAttachmentMotorForMillis(millis=1500)
    # br.waitForMillis(millis=1000)
    # # br.moveLeftAttachmentMotorUntilStalled(stallPct=100)
    # br.curve(radius=350, angle=70)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
