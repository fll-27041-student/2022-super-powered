from pybricks.parameters import Port, Stop, Direction, Button, Color

def run(bb: BaseBits):
    print("Running mission 6")
    #bb.robot.straight(756)
    #bb.lower_forklift()
    #bb.robot.straight(-6756)
    
     #un# next line
     #bb.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
     # Drive out to the circle with the mission model
    bb.robot.straight(360)
    bb.robot.turn(-45)
    bb.robot.straight(530)
     # Drop it off, and drive back a bit
    bb.robot.straight(-150)
    
     # Drive to the rechargeable cell
    bb.robot.turn(43)

    bb.robot.straight(355)
    bb.robot.turn(-90)

    bb.robot.straight(387)

     # Drop it off, and drive back a bit
    bb.robot.turn(90)

     # Drive to the rechargeable cell
    bb.robot.straight(250)
    bb.robot.turn(45)
    bb.robot.straight(700)
