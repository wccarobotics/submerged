from base_robot import *
from pybricks.tools import hub_menu

# Import missions
import reef_and_shark, raise_mast, board_cross, squid, squid_delivery, angler, r06_change_shipping_lanes, send_over_submersible, crabz


br = BaseRobot()

pressed = []
# col = br.colorSensor.color()
run_number = 0

runs = {
    0: reef_and_shark.Run,
    1: raise_mast.Run,
    2: board_cross.Run,
    3: squid.Run,
    4: squid_delivery.Run,
    5: angler.Run,
    6: r06_change_shipping_lanes.Run,
    7: send_over_submersible.Run,
    8: crabz.Run,
}
br.hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
br.hub.light.on(Color.BLUE)
run = 0
while True:
    pressed = br.hub.buttons.pressed()
    if Button.RIGHT in pressed:
        run += 1
    if Button.LEFT in pressed:
        run -= 1
    if run < 0:
        run = len(runs) - 1
    if run > len(runs) - 1:
        run = 0
    if Button.CENTER in pressed:
        br.hub.light.on(Color.GREEN)
        runs[run](br)
        run += 1
    br.hub.light.on(Color.BLUE)
    br.hub.display.number(run)
    wait(150)

    # while True:
    #     col = br.colorSensor.color()
    #     # The first thing this program does is it detects what color is
    #     # being help up to the robot color sensor.
    #     # If no color is detected, then it will display a sad face
    #     if col == Color.SENSOR_NONE:
    #         br.hub.display.icon(Icon.SAD)
    #         br.hub.light.on(Color.RED)
    #     else:  #  If a color is detected, then it will display a happy face
    #         br.hub.display.icon(Icon.HAPPY)
    #         br.hub.light.on(br.myColor2DefaultColorDict[col])

    #     wait(50)
    #     pressed = br.hub.buttons.pressed()
    #     #  When the left button is pressed, it will break out of the loop
    #     if Button.LEFT in pressed:
    #         break
    #     if Button.BLUETOOTH in pressed:
    #         # If the Bluetooth button is pressed, it will run the motors fast for
    #         # cleaning
    #         br.leftDriveMotor.run(1000)
    #         br.rightDriveMotor.run(1000)
    #         wait(25000)
    #         br.leftDriveMotor.brake()
    #         br.rightDriveMotor.brake()

    # # It will now launch the mission coresponding to the color
    # if col == Color.SENSOR_YELLOW:
    #     print("Launching Yellow")
    #     noah2.Run(br)
    #     br.waitForForwardButton()

    #     shaila.Run(br)

    # if col == Color.SENSOR_GREEN:
    #     print("Launching Green")
    #     GiosToast.Run(br)

    # if col == Color.SENSOR_LIME:
    #     print("Launching Lime")
    #     noahsdice.Run(br)

    # # if col == Color.SENSOR_MAGENTA:
    # #     print("Launching Magenta")
    # #     shaila.Run(br)

    # if col == Color.SENSOR_WHITE:
    #     print("Launching White")
    #     shaila2.Run(br)

    # if col == Color.SENSOR_ORANGE:
    #     print("Launching Orange")
    #     noah4.Run(br)

    # if col == Color.SENSOR_RED or col == Color.SENSOR_MAGENTA:
    #     print("Launching Red/Magenta")
    #     carternoah.Run(br)

    # if col == Color.SENSOR_BLUE:
    #     print("Launching Blue")
    #     Carovanni.Run(br)
