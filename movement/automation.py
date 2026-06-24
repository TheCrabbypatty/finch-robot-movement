from BirdBrain import Finch
bird = Finch()
bird.setBeak(100,0,0)
bird.setTail(2,0,100,0)
bird.setTail(3,0,0,100)
bird.setTail(4,100,0,100)
bird.setTail(1,75,25,0)
bird.playNote(60, 100)
bird.print("P")
while True:
    bird.print("P")
    bird.setDisplay([1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1])
    if bird.getDistance() < 100:
        bird.stop()
        bird.setTurn("R", 15, 100)
    bird.setMotors(100, 100)
    print("Distance to obstacle: ", bird.getDistance())
    if bird.getDistance() < 100:
        bird.stop()
        bird.setTurn("R", 15, 100)