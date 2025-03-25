from base_robot import *
from pybricks.tools import Matrix

# Import missions
import reef_and_shark, raise_mast, board_cross, squid, squid_delivery, r06_change_shipping_lanes, send_over_submersible, Battery, celebrate, clean_wheels, images, demo_straight, demo_turn, clean_and_reef


br = BaseRobot()

pressed = []

runs = {
    0: clean_and_reef.Run,
    1: reef_and_shark.Run,
    2: raise_mast.Run,
    3: board_cross.Run,
    4: squid.Run,
    5: r06_change_shipping_lanes.Run,
    6: send_over_submersible.Run,
    7 : squid_delivery.Run,
}

utilities = {
    0: clean_wheels.Run,
    1: Battery.Run,
    2: celebrate.Run,
    3: demo_straight.Run,
    4: demo_turn.Run,
}

utility_images = {
    0: images.CLEAN_WHEELS_1,
    1: images.BATTERY,
    2: images.STAR,
    3: images.UP_ARROW,
    4: images.LEFT_TURN_ARROW,
}

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
            wait(200)
        if Button.LEFT in pressed:
            run -= 1
            wait(200)
        if run < 0:
            run = len(runs) - 1
        if run > len(runs) - 1:
            run = 0
        if Button.CENTER in pressed:
            br.hub.light.on(Color.MAGENTA)
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
            wait(500)
            br.hub.system.set_stop_button([Button.CENTER])
            runs[run](br)
            br.hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
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
            wait(200)
        if Button.LEFT in pressed:
            func -= 1
            wait(200)
        if func < 0:
            func = len(utilities) - 1
        if func > len(utilities) - 1:
            func = 0
        br.hub.display.icon(utility_images[func])
        if Button.CENTER in pressed:
            br.hub.light.on(Color.MAGENTA)
            wait(170)
            utilities[func](br)
            wait(170)
        br.hub.light.on(Color.CYAN)
        if Button.BLUETOOTH in pressed:
            mode = 0
            func = 0
            wait(250)
