from pybricks.tools import Matrix

# this file is a colection of all sprites used for our team

# first sprite in wheel animation, used in utilities screen
CLEAN_WHEELS_1 = Matrix(
    [
        [0, 100, 100, 100, 0],
        [100, 0, 50, 0, 100],
        [100, 50, 100, 50, 100],
        [100, 0, 50, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)

# second sprite in wheel animation
CLEAN_WHEELS_2 = Matrix(
    [
        [0, 100, 100, 100, 0],
        [100, 50, 0, 50, 100],
        [100, 0, 100, 0, 100],
        [100, 50, 0, 50, 100],
        [0, 100, 100, 100, 0],
    ]
)

# 8 pointed star sprite
STAR = Matrix(
    [
        [50, 0, 100, 0, 50],
        [0, 50, 100, 50, 0],
        [100, 100, 100, 100, 100],
        [0, 50, 100, 50, 0],
        [50, 0, 100, 0, 50],
    ]
)

# failed atempt at displaying marcus
MARCUS = Matrix(
    [
        [0, 0, 0, 0, 0],
        [0, 50, 50, 0, 50],
        [75, 75, 100, 75, 100],
        [0, 50, 50, 0, 50],
        [0, 0, 0, 0, 0],
    ]
)

# arrow pointing up
UP_ARROW = Matrix(
    [
        [0, 0, 100, 0, 0],
        [0, 100, 75, 100, 0],
        [100, 0, 75, 0, 100],
        [0, 0, 75, 0, 0],
        [0, 0, 75, 0, 0],
    ]
)

# arrow turning left
LEFT_TURN_ARROW = Matrix(
    [
        [0, 0, 100, 0, 0],
        [0, 100, 0, 0, 0],
        [100, 75, 75, 75, 0],
        [0, 100, 0, 0, 75],
        [0, 0, 100, 0, 75],
    ]
)

# 1st sprite in running animation
RUNNING_1 = Matrix(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 75, 0],
        [50, 0, 50, 100, 50],
        [20, 50, 25, 50, 25],
    ]
)

# 2st sprite in running animation
RUNNING_2 = Matrix(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 75, 0],
        [0, 50, 100, 50, 0],
        [50, 25, 50, 25, 50],
    ]
)
