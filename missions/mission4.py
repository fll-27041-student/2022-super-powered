from pybricks.parameters import Port, Stop, Direction, Button, Color

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
    bb.robot.straight(49)
    #Move into the windmill
    for i in range (0,3):
        bb.robot.straight(76)
        bb.robot.straight(-76)
    #Go back to HQ
    bb.robot.turn(130.69)
    bb.robot.straight(507.68)