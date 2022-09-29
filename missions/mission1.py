from pybricks.parameters import Port, Stop, Direction, Button, Color

def run(bb: BaseBits):
    print("Running mission 1")
    # # bb.robot.straight(368)
    # bb.ev3.speaker.beep(200)
    # bb.left_attachment_motor.run_time(200, 2000)
    # bb.ev3.speaker.beep(400)
    # bb.right_attachment_motor.run_time(-100, 1800)
    # bb.ev3.speaker.beep(600)
    # #bb.robot.straight(-400)
    # bb.open_bay_doors()
    # bb.close_bay_doors()
    bb.robot.straight(1200)
    # bb.robot.turn(40)
    # bb.robot.straight(100)
    bb.open_bay_doors()