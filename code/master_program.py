from base_robot import *
from pybricks.tools import Matrix

# Import missions
import reef_and_shark, raise_mast, board_cross, squid, squid_delivery, r06_change_shipping_lanes, send_over_submersible, crabz, celebrate, clean_wheels


br = BaseRobot()

pressed = []

runs = {
    0: reef_and_shark.Run,
    1: raise_mast.Run,
    2: board_cross.Run,
    3: squid.Run,
    4: r06_change_shipping_lanes.Run,
    5: send_over_submersible.Run,
    6: squid_delivery.Run,
    # 8: crabz.Run,
}

options = {0: clean_wheels.Run, 1: celebrate.Run}
CLEAN_WHEELS = Matrix(
    [
        [0, 100, 100, 100, 0],
        [100, 0, 50, 0, 100],
        [100, 50, 100, 50, 100],
        [100, 0, 50, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)

STAR = Matrix(
    [
        [50, 0, 100, 0, 50],
        [0, 50, 100, 50, 0],
        [100, 100, 100, 100, 100],
        [0, 50, 100, 50, 0],
        [50, 0, 100, 0, 50],
    ]
)

br.hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
br.hub.light.on(Color.BLUE)
run = 0
mode = 0
func = 0
while True:
    pressed = br.hub.buttons.pressed()
    if mode == 0:
        if Button.RIGHT in pressed:
            run += 1
            wait(170)
        if Button.LEFT in pressed:
            run -= 1
            wait(170)
        if run < 0:
            run = len(runs) - 1
        if run > len(runs) - 1:
            run = 0
        if Button.CENTER in pressed:
            br.hub.light.on(Color.MAGENTA)
            runs[run](br)
            run += 1
            if run > len(runs) - 1:
                celebrate.Run(br)
        br.hub.display.number(run)
        br.hub.light.on(Color.GREEN)
        if Button.BLUETOOTH in pressed:
            wait(250)
            mode = 1
    pressed = br.hub.buttons.pressed()
    if mode == 1:
        if Button.RIGHT in pressed:
            func += 1
            wait(170)
        if Button.LEFT in pressed:
            func -= 1
            wait(170)
        if func < 0:
            func = len(options) - 1
        if func > len(options) - 1:
            func = 0
        if func == 0:
            br.hub.display.icon(CLEAN_WHEELS)
        if func == 1:
            br.hub.display.icon(STAR)
        if Button.CENTER in pressed:
            options[func](br)
        br.hub.light.on(Color.CYAN)
        if Button.BLUETOOTH in pressed:
            mode = 0
            wait(250)
