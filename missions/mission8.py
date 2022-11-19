from pybricks.parameters import Port, Stop, Direction, Button, Color

# Will: Kobe
def run(bb: BaseBits):
    print("Running mission 8")
    distance = 390
    bb.robot.straight(distance)
    bb.left_attachment_motor.run_time(300, 350)
    bb.robot.straight(distance * -1)
    bb.robot.turn(-45)
    bb.robot.straight(1800)