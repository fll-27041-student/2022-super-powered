from pybricks.parameters import Port, Stop, Direction, Button, Color

# Cha Cha
def run(bb: BaseBits):
    print("Running mission 7")
    #Set speed to go super fast
    bb.robot.settings(straight_speed=4000, straight_acceleration=1000, turn_rate=200, turn_acceleration=100)
    #Go forward
    bb.robot.straight(900)
    #Turn so it wont hit anything
    bb.robot.turn(-10)
    #Finish the journey
    bb.robot.straight(920)
    #Stop
    bb.robot.stop()
    #Set speed to normal
    bb.robot.settings(straight_speed=600, straight_acceleration=200, turn_rate=200, turn_acceleration=100)
