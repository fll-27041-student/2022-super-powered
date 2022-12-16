from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait

# Charles - Deliver dino and activate the power station
def run(bb: BaseBits):
    print("Running mission 5")

    #bb.left_attachment_motor.run_time(300, 600)
    print("Here 1")
    bb.robot.straight(690)
    print("Here 2")
    bb.left_attachment_motor.run_time(-1000, 700)

    print("Here 3")
    bb.robot.straight(60)
    bb.left_attachment_motor.run_time(1000, 1000)

#    bb.robot.straight(1200)

    bb.robot.drive(1000, -10)
    bb.robot.drive(25, 45)
    wait(2000)
    bb.robot.stop()
    bb.left_attachment_motor.stop()
