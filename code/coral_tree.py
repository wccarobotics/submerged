from base_robot import *
import images

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
    done = False
    # grab tree
    br.driveForDistance(mm(16), 50)
    br.driveForMillis(1500, -100)

    # waits until user imput
    br.hub.display.icon(images.CORAL_TREE)
    while not done:
        pressed = br.hub.buttons.pressed()
        if Button.BLUETOOTH in pressed:
            done = True
    br.hub.display.animate(
        [
            images.RUNNING_1,
            images.RUNNING_2,
            images.RUNNING_3,
            images.RUNNING_4,
            images.RUNNING_5,
            images.RUNNING_6,
            images.RUNNING_7,
        ],
        300,
    )

    # deliver tree
    br.driveForDistance(mm(18), 100)
    br.driveForMillis(3000, -50, accelerationPct=100)


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
