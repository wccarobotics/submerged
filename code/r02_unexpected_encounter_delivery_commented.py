from base_robot import *


def Run(br: BaseRobot):
    wait(250)

    # Start against south wall using square and short side of rectangle spacers
    # Squid should be inside attachment fork with gate down so the squid
    # will be dragged bacwards when the robot moves backwards

    # Curve left and then drive straight to go past the squid mission model
    br.curve(250, -65)
    br.driveForDistance(300)

    # Curve right to line up for the angler fish
    br.curve(250, 20)

    # Drive past angler fish to activate it
    # Drive slowly on the second part to more reliably activate the lever
    br.driveForDistance(400, speedPct=50)
    br.driveForDistance(200, speedPct=25)

    # Turn left to line up facing away from squid delivery, then back up to it
    br.curve(-250, 25)
    br.driveForDistance(-175)

    # Turn right in place, then back up.  This should result in the squid being
    # in the delivery area
    br.turnInPlace(75)
    br.driveForDistance(-175)

    # Lift attachment gate to release squid
    br.moveLeftAttachmentMotorForDegrees(-90)

    # Go backwards (south) and leave the squid in its delivery area
    br.driveForDistance(-150)

    # Head back home.  Make a sharp "right" turn while going bacwards
    br.curve(-125, -75)

    # Robot should be pointed more or less towards right home now
    # Curve slightly to the right, drive straight, and then curve to the right
    # again to aim for corner of home
    br.curve(125, 10)
    br.driveForDistance(500)
    br.curve(250, 90)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
