from base_robot import *
from pybricks.tools import Matrix

MARCUS = Matrix(
    [
        [0, 0, 0, 0, 0],
        [0, 50, 50 ,0, 50],
        [75 , 75, 100, 75, 100],
        [0, 50, 50, 0, 50],
        [0, 0, 0, 0, 0]
    ]
)
STAR = Matrix(
    [
        [50, 0, 100, 0, 50],
        [0, 50, 100, 50, 0],
        [100, 100, 100, 100, 100],
        [0, 50, 100, 50, 0],
        [50, 0, 100, 0, 50]
    ]
)

def Run(br: BaseRobot):
    br.hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
    br.hub.display.icon(STAR)
    br.hub.light.animate((Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN), 200)
    br.hub.speaker.play_notes(['G4/4', 'G4/4', 'E4/8', 'G4/4', 'E4/8', 'G4/8', 'E4/8', 'D4/8', 'G4/4', 'R/8', 'R/8', 'G4/8', 'D5/8', 'E5/8', 'D5/8', 'E5/8', 'D5/4', 'C5/16', 'B4/16', 'A4/8', 'G3/4', 'A3/4', 'G3/4', 'G5/4'], 160)
    while not Button.CENTER in br.hub.buttons.pressed():
        br.hub.light.on(Color.MAGENTA)
# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
