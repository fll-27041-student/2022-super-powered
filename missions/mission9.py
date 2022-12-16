from pybricks.parameters import Port, Stop, Direction, Button, Color

def run(bb: BaseBits):
    print("Running mission 9")
    #bb.robot.straight(500)
    bb.robot.straight(342)
    bb.robot.straight(-35)
    bb.lower_forklift()
    bb.robot.straight(-307)
    bb.lift_forklift()