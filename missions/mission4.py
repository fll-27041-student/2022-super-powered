from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog


def run(bb: BaseBits):
    print("Running mission 4")
    #Make sure the forklift is lowered
    bb.lower_forklift()
    #Do the TV mission
    bb.robot.straight(377)
    bb.robot.straight(-115.5)
    #Align with the windmill
    bb.robot.turn(-48.2)
    bb.robot.straight(444.4)
    bb.robot.turn(87)
    #Setup for the windmill mission
    bb.robot.straight(62)
    #Move into the windmill
    for i in range (0,4):
        bb.robot.straight(70)
        wait(100)
        bb.robot.straight(-70)
    #Go back to HQ5
    bb.robot.turn(120.69)
    bb.robot.straight(507.68)
    
