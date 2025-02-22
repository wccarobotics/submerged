TIRE_DIAMETER = 88  # mm - Large spike tires - 88 mm, small spike tires - 56 mm, projekt alpha tires 62.4 mm

# Drivebase parameters. None of these should ever be changed by users
if TIRE_DIAMETER == 56:
    DB_MAX_SPEED_MMSEC = 488
elif TIRE_DIAMETER == 88:
    DB_MAX_SPEED_MMSEC = 768
else:
    raise RuntimeError("Unknown tire")

# Straight Acceleration constants
# Anything above 800 mm/sec^2 causes wheel slippage, regardless of the
# tire size. The mass of the 56 and 88mm robots is about the same, so the
# force to maintain that acceleration is the same
# For 56mm, the maximum that can be set in the settings() command is 9775.
# For 88mm, the maximum that can be set in the settings() command is 15360.
DB_MAX_ACCEL_MMSEC2 = 800

# For turn rates, the best speed and acceleration was determined by testing
# It did not matter if it was on 56mm or 88mm tires, the values were the
# same for both. 180 deg/sec for speed and 360 deg/sec^2 for acceleration
# For 56mm, the maximum speed that can be set in the settings() command is 543
# For 88mm, the maximum speed that can be set in the settings() command is 854.
# For 88mm, the maximum accel that can be set in the settings() command is 17094.
DB_MAX_TURN_RATE_DEGSEC = 180
DB_MAX_TURN_ACCEL_DEGSEC2 = 360

AXLE_TRACK = (
    16 * 8
)  # distance between the wheels, mm - 16 studs * 8 mm each stud

# The drivebase can accept speeds down to zero, but is not very efficient and
# quite erratic. Realistically, 30 is a good minimum speed
DB_MIN_SPEED_MMSEC = 30

# Lowest usable accelleration, determined by testing
DB_MIN_ACCEL_MMSEC2 = 5

# Max and min turning speeds, determined by testing
# These are not affected by the tire size
DB_MIN_TURN_RATE_DEGSEC = 20
DB_MIN_TURN_ACCEL_DEGSEC2 = 10

# Not sure how these are used
DB_ABS_MAX_TORQUE_MNM = 700  # milli-newton-meters
DB_ABS_MIN_TORQUE_MNM = 20  # milli-newton-meters

# # Large Motor usable parameters
# LG_MOT_MAX_VOLTAGE = 9000  # mV
# LG_MOT_MIN_VOLTAGE = 3000  # mV
# LG_MOT_MAX_TORQUE = 560

# Medium Motor usable parameters
ATTACHMENT_MOT_MAX_SPEED_DEGSEC = 1000
# MED_MOT_MAX_ACCEL_DEGSEC2 = 20000
# MED_MOT_MIN_ACCEL_DEGSEC2 = 50
ATTACHMENT_MOT_MIN_SPEED_DEGSEC = 100
ATTACHMENT_MOT_MAX_TORQUE = 250  # milli-newton-meters
ATTACHMENT_MOT_MIN_TORQUE = 50  # milli-newton-meters


def Rescale(val, in_min, in_max, out_min, out_max):
    neg = val / abs(val)  # will either be 1 or -1
    val = abs(val)
    if in_max == in_min:
        return 0
    if val < in_min:
        val = in_min
    if val > in_max:
        val = in_max
    retVal = out_min + (val - in_min) * (
        (out_max - out_min) / (in_max - in_min)
    )
    if retVal > out_max:
        retVal = out_max
    if retVal < out_min:
        retVal = out_min
    return retVal * neg


def RescaleStraightSpeed(speedPct):
    return Rescale(
        speedPct,
        1,
        100,
        DB_MIN_SPEED_MMSEC,
        DB_MAX_SPEED_MMSEC,
    )


def RescaleStraightAccel(accelPct):
    return Rescale(
        accelPct,
        1,
        100,
        DB_MIN_ACCEL_MMSEC2,
        DB_MAX_ACCEL_MMSEC2,
    )


def RescaleTurnSpeed(turnSpeedPct):
    # print(turnSpeedPct)
    return Rescale(
        turnSpeedPct,
        1,
        100,
        DB_MIN_TURN_RATE_DEGSEC,
        DB_MAX_TURN_RATE_DEGSEC,
    )


def RescaleTurnAccel(turnAccelPct):
    return Rescale(
        turnAccelPct,
        1,
        100,
        DB_MIN_TURN_ACCEL_DEGSEC2,
        DB_MAX_TURN_ACCEL_DEGSEC2,
    )


def RescaleAttachmentMotSpeed(medMotSpeedPct):
    return Rescale(
        medMotSpeedPct,
        1,
        100,
        ATTACHMENT_MOT_MIN_SPEED_DEGSEC,
        ATTACHMENT_MOT_MAX_SPEED_DEGSEC,
    )


def RescaleAttachmentMotTorque(medMotTorquePct):
    return Rescale(
        medMotTorquePct,
        1,
        100,
        ATTACHMENT_MOT_MIN_TORQUE,
        ATTACHMENT_MOT_MAX_TORQUE,
    )


def RescaleDbTorque(dbTorquePct):
    return Rescale(
        dbTorquePct,
        1,
        100,
        DB_ABS_MIN_TORQUE_MNM,
        DB_ABS_MAX_TORQUE_MNM,
    )


def RescaleConvertFarToCel(DegF):
    return Rescale(DegF, 0, 212, -17.77, 100)


# def RescaleMedMotDutyLimit(medMotDutyLimitPct):
#     return Rescale(
#         medMotDutyLimitPct,
#         1,
#         100,
#         5,
#         195,
#     )


# def RescaleSensitivity(sens):
#     return Rescale(
#         sens,
#         1,
#         100,
#         1,
#         12,
#     )


def RescaleBatteryVoltage(volts):
    return Rescale(volts, 7000, 8000, 0, 100)
