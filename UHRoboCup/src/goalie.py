import track
import walk
import config
import dive
import math
motionProxy = config.load_proxy("ALMotion")
pNames = "Body"
timeProxy = config.load_proxy("DCM")
redballtracker = config.load_proxy("ALRedBallTracker")
def goalie_pose():   #This is the pose the goalie will be using.
    config.stiffness_on()
    motionProxy.angleInterpolationWithSpeed(pNames, dive.goalie_position(), .5)
def goalie():
    goalie_pose()
    while True:
        track.find_red_ball()
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
                dive.dive_left_goal()
                goalie_pose()
                redballtracker.startTracker()
                count = 100
            elif velocity >= .2 and redballposition[1] < -.1 and redballposition[0] < 2:
                redballtracker.stopTracker()
                dive.dive_right_goal()
                goalie_pose()
                redballtracker.startTracker()
                count = 100
            elif velocity == 0:   #If the ball has not moved the count goes up by one and if reaches 100 looks for ball again.
                count += 1    
        count = 0
        counter = 0
def goalie_improved(option):
    redballposition=track.find_red_ball()
    print redballposition
    redballtracker.startTracker()
    if option == 1:
        walk.walk_clockwise()
        while redballposition[1]<-.31:
            redballposition= redballtracker.getPosition()
            print "Walking!", redballposition[1]
        redballtracker.stopTracker()
        walk.stop()
    else:
        walk.walk_counterclockwise()
        while redballposition[1] > .31:
            redballposition= redballtracker.getPosition()
            print "counter", redballposition[1]
        redballtracker.stopTracker()
        walk.stop()
    goalie_pose()