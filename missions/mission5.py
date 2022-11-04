from pybricks.parameters import Port, Stop, Direction, Button, Color

# Charles
def run(bb: BaseBits):
    print("Running mission 5")
    bb.lower_forklift()

    
    bb.robot.straight(450)
    bb.robot.turn(45)
    bb.robot.straight(200)
    bb.robot.turn(-45)
    bb.robot.straight(300)
    bb.robot.turn(-90)
    bb.lift_forklift()
    bb.robot.straight(-20)
    bb.lower_forklift()
    bb.robot.straight(-200)
    bb.robot.turn(75)
    bb.robot.straight(600)

    # lift up to raise

    # drive forward a little back

    # back up and 

    # # bb.robot.straight(368)
    # bb.ev3.speaker.beep(200)
    # bb.left_attachment_motor.run_time(200, 2000)
    # bb.ev3.speaker.beep(400)
    # bb.right_attachment_motor.run_time(-100, 1800)
    # bb.ev3.speaker.beep(600)
    # #bb.robot.straight(-400)
    # bb.open_bay_doors()
    # bb.close_bay_doors()
    
    # bb.robot.straight(100)