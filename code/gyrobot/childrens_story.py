# This code is based on the PyBricks balancing robot sample here:
# https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-robot-inventor/other-models/balancer
#
# It requires PyBricks firmware build 3510 or higher, as this included a fix to async which
# better allows the bot to balance and play music at the same time

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait, StopWatch, run_task, multitask, Matrix
from pybricks.geometry import Axis
from pybricks.iodevices import XboxController
from pybricks.parameters import Button
from pybricks.parameters import Icon
from SoundPlayer import *

NOTE = Matrix(
    [
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
    ]
) * 100

YES = Matrix(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
    ]
) * 100

NO = Matrix(
    [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
    ]
) * 100

# Initialize motors.
left = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right = Motor(Port.F)
left.reset_angle(0)
right.reset_angle(0)

# Initialize hub and color sensor.
# You can also use the TechnicHub and/or the ColorDistanceSensor
# instead.
hub = InventorHub()
#sensor = ColorSensor(Port.A)

sound_player = SoundPlayer(hub)

print("Pairing controller...")
controller = XboxController()
print("Controller paired, press A")

async def balance():
    global hub, left, right, controller

    hub.display.icon(Icon.HAPPY)

    # Initialize position buffer for speed calculation.
    DT = 5
    window = int(300 / DT)
    buf = [0] * window
    idx = 0
    angle = 0
    #DRIVE_SPEED = 300
    DRIVE_SPEED = 400
    PAUSE = 5000

    running = False

    # Timer to generate reference position.
    watch = StopWatch()
    await_watch = StopWatch()
    reference = 0

    while True:
        if Button.A in controller.buttons.pressed() or Button.RIGHT in hub.buttons.pressed():
            running = True
            watch = StopWatch()
            reference = 0
            idx = 0
            angle = 0
            buf = [0] * window
            left.reset_angle(0)
            right.reset_angle(0)
        elif Button.B in controller.buttons.pressed():
            running = False
        elif Button.X in controller.buttons.pressed():
            sound_player.Play()
        elif Button.Y in controller.buttons.pressed():
            await sound_player.Stop()
        elif Button.UP in controller.buttons.pressed():
            hub.light.off()
            hub.display.icon(Icon.HAPPY)
        elif Button.DOWN in controller.buttons.pressed():
            hub.light.off()
            hub.display.icon(Icon.SAD)
        elif Button.RIGHT in controller.buttons.pressed():
            hub.light.off()
            hub.display.icon(Icon.HEART)
        elif Button.LEFT in controller.buttons.pressed():
            hub.light.off()
            hub.display.icon(NOTE)
        elif Button.LB in controller.buttons.pressed():
            hub.display.icon(NO)
            hub.light.on(Color.RED)
        elif Button.RB in controller.buttons.pressed():
            hub.display.icon(YES)
            hub.light.on(Color.GREEN)

        # Get angular rate and estimated angle.
        rate = hub.imu.angular_velocity(Axis.Y)
        angle += rate * DT / 1000

        if running and (angle > 45 or angle < -45):
            running = False
            hub.display.icon(Icon.SAD)
            sound_player.WompWomp()

        # Get motor position.
        position = (left.angle() + right.angle()) / 2

        # Calculate motor speed.
        speed = (position - buf[idx]) / (window * DT) * 1000
        buf[idx] = position
        idx = (idx + 1) % window

        # Calculate reference position, which just grows linearly with
        # time.
        #reference = -max(watch.time() - PAUSE, 0) / 1000 * DRIVE_SPEED
        speed_input = (controller.triggers()[1] - controller.triggers()[0]) / 2

        reference = reference - speed_input / 100.0 * 4 * DRIVE_SPEED * DT / 1000.0
        #reference = -max(watch.time() - PAUSE, 0) / 1000 * speed_input / 100.0 * 2 * DRIVE_SPEED

        # Calculate duty cycle.
        diff = position - reference
        duty = 0.018 * rate + 19 * angle + 0.45 * diff + 0.16 * speed

        # Account for battery level and type.
        duty *= 7200 / hub.battery.voltage()

        # Calculate steering.
        #reflection = sensor.reflection()
        #steering = (reflection - 28) * 0.6
        steering = 0
        steering = controller.joystick_left()[0] * .3

        # Apply duty cycle for balancing and steering.
        if (running):
            left.dc(duty + steering)
            right.dc(duty - steering)
        else:
            left.dc(0)
            right.dc(0)
        # Wait some time.
        await wait(DT)
        # w = StopWatch()
        # while (w.time() < DT):
        #     pass

        # if (await_watch.time() > 100):
        #     await wait(1)
        #     await_watch.reset()

async def sound():
    global hub
    print("playing")




async def main():
    await multitask(balance(), sound_player.run())

#run_task(main(), loop_time=0)
run_task(main())