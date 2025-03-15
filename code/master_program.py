from base_robot import *
from pybricks.tools import hub_menu

# Import missions
import reef_and_shark, raise_mast, board_cross, squid, squid_delivery, r06_change_shipping_lanes, send_over_submersible, crabz, celebrate


br = BaseRobot()

pressed = []
run_number = 0

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
br.hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
br.hub.light.on(Color.BLUE)
run = 0
while True:
    pressed = br.hub.buttons.pressed()
    if Button.RIGHT in pressed:
        run += 1
        wait(150)
    if Button.LEFT in pressed:
        run -= 1
        wait(150)
    if run < 0:
        run = len(runs) - 1
    if run > len(runs) - 1:
        run = 0
    if Button.CENTER in pressed:
        br.hub.light.on(Color.GREEN)
        runs[run](br)
        run += 1
        if run > len(runs) - 1:
            celebrate.Run(br)
    br.hub.light.on(Color.BLUE)
    br.hub.display.number(run)
