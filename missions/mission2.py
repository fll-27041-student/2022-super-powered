from pybricks.tools import wait, StopWatch, DataLog

#Aidan's code
def run(bb: BaseBits):
    print("Running load (mission 2)")

    bb.lift_forklift()

    # drive towards oil rid
    bb.robot.straight (18 * 25.4)

    # turn to avoid oil rig and face the target
    bb.robot.turn(45)
    bb.robot.straight (7.75 * 25.4)
    bb.robot.turn(-45)

    # Drive up to target
    bb.robot.straight (7.45 * 25.4)

    # Drop items in
    bb.open_bay_doors()
    bb.close_bay_doors()

    # return to home
    bb.robot.straight (-3.8 * 25.4)
    bb.lower_forklift()
    bb.robot.straight (-9 * 25.4)
 
    # for i in range(0, 5):
    #     bb.robot.turn(3)
    #     bb.robot.straight (-5 * 25.4)


    bb.robot.drive(-200, 25)
    wait(4000)
    bb.robot.stop()
    
    bb.lift_forklift()