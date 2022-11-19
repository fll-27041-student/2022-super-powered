from pybricks.parameters import Port, Stop, Direction, Button, Color

def run(bb: BaseBits):
    print("Running mission 10")
from pybricks.parameters import Port, Stop, Direction, Button, Color

def run(bb: BaseBits):
    print("Running mission 1")

    # bb.lift_forklift()

    # # Go straight to line up with the hand
    # bb.robot.straight(890)
    # # Turn the robot to fce the hand
    # bb.robot.turn(91)
    # # Go strait to arive at the hand
    # bb.robot.straight(493.5)

    bb.robot.drive(200, 18)
    wait(5000)
    bb.robot.stop()


    # Lower the hook on the forklift down to catch on to the lever on the hand
    bb.lower_forklift()
    # Back up to pull the lever on the hand to lover the hand
    bb.robot.straight(-200)
    # lift up the forklift so I don't keep holding the lever
    bb.lift_forklift()
    # Turn towrds the first energy unit in the solar farm
    bb.robot.turn(-30)
    # Start moving twords the energy units
    bb.robot.straight(220)
    # The slight turn helps me make sure that I make it to the first energy unit incase I overstoot with the last turn
    bb.robot.turn(7)
    # Finsh getibng to the first energy unit
    bb.robot.straight(225)
    # Turn to catch the first energy unit and turn twords the next units
    bb.robot.turn(-60)
    # Drive to the next two energy units in the solar farm
    bb.robot.straight(200)
    # Turn to colect the two energy units in the solar farm 
    bb.robot.turn(-85)
    # Start driving foward twards home
    bb.robot.straight(290)
    # A stight turn is needed to make sure that I will stay clear of the hidroelectric dam
    bb.robot.turn(15)
    # finish off by going straight for a while to make sure that I make it all the way home so I am all the way off the board
    bb.robot.straight(700)

    # Coments tell what the the piece of code below it does


