from pybricks.parameters import Port, Stop, Direction, Button, Color

# Seamus: mission model delivery
def run(bb: BaseBits):

    bb.lift_forklift()
    print("Running mission 6")
    #bb.robot.straight(756)
    #bb.lower_forklift()
    #bb.robot.straight(-6756)
    
     #un# next line
     #bb.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
    ## Drive out to the circle with the mission model
    bb.robot.straight(370)
    bb.robot.turn(-45)
    bb.robot.straight(530)
     # Drop it off, and drive back a bit
    bb.robot.straight(-150)
    
     # Drive to the rechargeable battery
    #bb.robot.turn(43)



    bb.robot.turn(54)
    ##change the speed settings
    bb.robot.stop()
    bb.robot.settings(straight_speed=4000, straight_acceleration=1000, turn_rate=200, turn_acceleration=100)

    bb.robot.straight(1060)

    bb.robot.stop()
    # Set speed to normal
    # bb.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
    bb.robot.settings(straight_speed=750, straight_acceleration=400, turn_rate=200, turn_acceleration=100)


    # Competition code #1
    # bb.robot.turn(45)  #60

    # bb.robot.straight(355)
    # bb.robot.turn(-90)

    # bb.robot.straight(387)

    #  # Drop it off, and drive back a bit
    # bb.robot.turn(90)

    #  # Drive to the rechargeable cell
    # bb.robot.straight(250)
    # bb.robot.turn(45)
    # bb.robot.straight(700)
