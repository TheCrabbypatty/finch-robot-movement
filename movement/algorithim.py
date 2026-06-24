from BirdBrain import Finch
import sys
bird = Finch()

def graph(response):
    response = response.strip().lower()
    if response == "circle":
        radius = int(input("What radius is your circle (Input an integer 2 to 5)"))
        if radius == 2:
            bird.setMotors(0,100)
        elif radius == 3:
            bird.setMotors(20,100)
        elif radius == 4:
            bird.setMotors(30,100)
        elif radius == 5:
            bird.setMotors(37,100)
        else:
            pass
    elif response == "linear":
        angle = int(input("What angle do you want your line (0-359)"))
        if 0 <= angle <= 359:
            bird.setTurn("L", angle, 100)
            bird.setMove("F",100,100)
        else:
            pass
    elif response == "exit":
        bird.stop()
        sys.exit()
    else:
        pass
   
while True:
    userResponse = input("What do you want to graph? (circle or linear) type exit to exit")
    graph(userResponse)