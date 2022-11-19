from pybricks.parameters import Port, Stop, Direction, Button, Color

# Charles
def run(bb: BaseBits):
    print("Running mission 5")

    bb.left_attachment_motor.run_time(300, 600)
    print("Here 1")
    bb.robot.straight(600)
    print("Here 2")
    bb.left_attachment_motor.run_time(-800, 550)

    print("Here 3")
    bb.robot.straight(60)
    bb.left_attachment_motor.run_time(800, 550)

    bb.robot.straight(1400)
    bb.left_attachment_motor.stop()
    # bb.lower_forklift()

    
    # bb.robot.straight(450)
    # bb.robot.turn(45)
    # bb.robot.straight(200)
    # bb.robot.turn(-45)
    # bb.robot.straight(300)
    # bb.robot.turn(-90)
    # bb.lift_forklift()
    # bb.robot.straight(-20)
    # bb.lower_forklift()
    # bb.robot.straight(-200)
    # bb.robot.turn(75)
    # bb.robot.straight(600)