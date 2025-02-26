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

    ## DRIVING STRAIGHT

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

    # You can also make the robot drive for an amount of time instead of a distance
    # This is especially useful when you want to drive into a mission model.
    # When driving into a mission model you usually want to keep driving as if
    # you were going to drive past it.  If you use a distance and the wheels
    # don't slip, then the robot may get stuck as it will never reach that distance.
    # This will drive forward for half a second
    br.driveForMillis(500)

    # This will drive forward for a quarter second at 25% speed
    br.driveForMillis(250, speedPct=25)

    # Use a negative speed if you want to go backwards
    # This will drive backwards at 50% speed for 1 second
    br.driveForMillis(1000, speedPct=-50)

    ## TURNING IN PLACE

    # Here is how you can turn in place.  This will rotate 90 degrees to the right (clockwise):
    br.turnInPlace(90)

    # This will rotate 45 degrees to the left (counterclockwise)
    br.turnInPlace(-45)

    ## Driving in a curve

    # There are two functions you can use to drive along a curve
    # Both of them let you specify the radius of the curve to drive along
    # With driveArcDist, you specify the distance along the curve that the robot
    # should drive.
    # With the curve function, you specify the angle or number of degrees that
    # the robot should drive.  A value of 360 would make the robot drive in a
    # complete circle, while 90 would travel 1/4 of the circle, resulting in a
    # 90 degree turn

    # This will drive along a curve curving to the right with a radius of 15 inches.
    # It will drive for 10 inches along the curve
    br.driveArcDist(mm(15), mm(10))

    # To curve to the left, use a negative value for the radius
    # You can also specify the speed to drive
    # This will curve to the left with a radius of 25 inches, driving for 5 inches,
    # with a speed of 50%
    br.driveArcDist(mm(-25), mm(5), speedPct=50)

    # To curve for a specified number of degrees, use the curve function.
    # This will curve to the right with a radius of 15 inches.  It will drive
    # until it has turned 45 degrees, and will drive at a speed of 50%
    br.curve(mm(15), 45, speedPct=50)

    # Other sample commands:
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
