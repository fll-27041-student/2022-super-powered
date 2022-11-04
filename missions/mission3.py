from pybricks.parameters import Port, Stop, Direction, Button, Color

# Seamus
def run(bb: BaseBits):
    print("Running mission 3")

    # Drive out to the circle with the mission model
    bb.robot.straight(1300)

    # Drop it off, and drive back a bit
    bb.robot.straight(-150)
    
    # Drive to the rechargeable cell
    bb.robot.turn(45)

    bb.robot.stop()
    bb.robot.settings(straight_speed=1000, straight_acceleration=300, turn_rate=200, turn_acceleration=100)
    bb.robot.straight(1600)
    bb.robot.stop()
    bb.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)

    # Push it back to the right side's home

    #bb.robot.straight(1200)
    # bb.robot.turn(94)
    # bb.robot.straight(100)
    # bb.robot.turn(93)
    # bb.robot.straight(-300)
    # bb.robot.turn(83)
    # bb.robot.straight(1130)
    # bb.robot.straight(100)
    #bb.open_bay_doors()