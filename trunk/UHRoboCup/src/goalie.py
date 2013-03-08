import track
import walk
import config
import dive
import math
motionProxy = config.loadProxy("ALMotion")
pNames = "Body"
timeProxy = config.loadProxy("DCM")
redballtracker = config.loadProxy("ALRedBallTracker")
def goaliePose():   #This is the pose the goalie will be using.
    config.stiffnessOn()
    motionProxy.angleInterpolationWithSpeed(pNames, dive.goaliePosition(), .5)
def goalie():
    goaliePose()
    while True:
        track.findRedBall()
        redballtracker.startTracker()
        if counter == 0:     #This is for the first time to define redballposition since it will be updated after redballposition2
            redballposition = redballtracker.getPosition()
            counter == 1
        redballposition2 = redballposition   #redballposition2 stores the old position of the ball and we get the difference of them
        print "redballposition2 :",   redballposition2
        while count < 100:
            redballtracker.setWholeBodyOn(True)
            redballposition2 = redballposition
            redballposition = redballtracker.getPosition()   #Updates the position of the ball
            print "redballposition:", redballposition
            distance = math.sqrt(math.pow(redballposition[0],2) + math.pow(redballposition[1],2) + math.pow(redballposition[2],2))
            print "distance:" , distance
            velocity = math.sqrt(math.pow((redballposition[0] - redballposition2[0]), 2))/ .1
            print "velocity:" , velocity, "count" , count
            
            
            if velocity >= .2 and redballposition[1] > .1 and redballposition[0] < 2:
                redballtracker.stopTracker()
                dive.diveLeftGoal()
                goaliePose()
                redballtracker.startTracker()
                count = 100
            elif velocity >= .2 and redballposition[1] < -.1 and redballposition[0] < 2:
                redballtracker.stopTracker()
                dive.diveRightGoal()
                goaliePose()
                redballtracker.startTracker()
                count = 100
            elif velocity == 0:   #If the ball has not moved the count goes up by one and if reaches 100 looks for ball again.
                count += 1    
        count = 0
        counter = 0
def goalieImproved(option):
    redballposition=track.findRedBall()
    print redballposition
    redballtracker.startTracker()
    if option == 1:
        walk.walkClockwise()
        while redballposition[1]<-.31:
            redballposition= redballtracker.getPosition()
            print "Walking!", redballposition[1]
        redballtracker.stopTracker()
        walk.stop()
    else:
        walk.walkCounterclockwise()
        while redballposition[1] > .31:
            redballposition= redballtracker.getPosition()
            print "counter", redballposition[1]
        redballtracker.stopTracker()
        walk.stop()
    goaliePose()