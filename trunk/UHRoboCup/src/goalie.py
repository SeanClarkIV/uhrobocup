import config
import dive
import math
import time
import camera
motionProxy = config.loadProxy("ALMotion")
pNames = "Body"
timeProxy = config.loadProxy("DCM")
redballtracker = config.loadProxy("ALRedBallTracker")
def goaliepose():   #This is the pose the goalie will be using.
    config.StiffnessOn()
    motionProxy.angleInterpolationWithSpeed(pNames, dive.dive1(), .5)
def goalie():
    goaliepose()
    timer = timeProxy.getTime(0) #Timer tells us the time so we can later find out velocity.
    print timer
    initialredballposition = redballtracker.getPosition() #Set the inital position as the first position the head is in,
    #assume the ball isnt the inital position
    camera.topCamera()
    redballtracker.startTracker()           #Starting the tracker.
    redballtracker.setWholeBodyOn(True)
    counter = 0
    count = 0
    while True:

        while redballtracker.getPosition() == initialredballposition:  # Ball lost.
                if redballtracker.isNewData() == False and count == 0: # Ball still lost.
                    print "Looking for red ball"
                    camera.topCamera()
                    motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, 1.433], 0.07)
                    time.sleep(2)
                    count = 1
                elif redballtracker.isNewData() == False and count == 1: #Switches cameras.
                    camera.bottomCamera()
                    motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, 1.433], 0.07)
                    time.sleep(2)
                    count = 0
        if counter == 0:     #This is for the first time to define redballposition since it will be updated after redballposition2
            redballposition = redballtracker.getPosition()
            counter == 1
            timer = timeProxy.getTime(0)
        redballposition2 = redballposition   #redballposition2 stores the old position of the ball and we get the difference of them
        #to get the velocity of the ball.
        print "redballposition2 :",   redballposition2, "timer:", timer
        while count < 100:
            redballtracker.startTracker() #Starts tracker again just in case. 
            redballtracker.setWholeBodyOn(True)
            redballposition2 = redballposition
            redballposition = redballtracker.getPosition()   #Updates the position of the ball
            print "redballposition:", redballposition
            timer = timeProxy.getTime(0)
            timer2 = timeProxy.getTime(0)
            distance = math.sqrt(math.pow(redballposition[0],2) + math.pow(redballposition[1],2) + math.pow(redballposition[2],2))
            print "distance:" , distance
            print "timer2:" , timer2, "timer:" , timer
            velocity = math.sqrt(math.pow((redballposition[0] - redballposition2[0]), 2) + math.pow((redballposition[1] - redballposition2[1]),2) + math.pow((redballposition[2] - redballposition2[2]),2))/ (timer2 - timer)
            print "velocity:" , velocity, "count" , count
            if velocity == 0:   #If the ball has not moved the count goes up by one and if reaches 100 looks for ball again.
                count += 1
            elif velocity >= .04 and redballposition[1] > .1 and redballposition[0] < 1.5:    #If the ball is moving quickly it will dive left if parameters are met
                redballtracker.stopTracker()
                dive.diveleft()
                goaliepose()
                redballtracker.startTracker()
                count = 100
            elif velocity >= .01 and redballposition[1] > .1 and redballposition[1] < .6:
                redballtracker.stopTracker()
                dive.diveleft()
                goaliepose()
                redballtracker.startTracker()
                count = 100
            elif velocity >= .04 and redballposition[1] < -.1 and redballposition[0] < 1.5:
                redballtracker.stopTracker()
                dive.diveright()
                goaliepose()
                redballtracker.startTracker()
                count = 100
            elif velocity >= .01 and redballposition[1] < -.1 and redballposition[0] < .6:
                redballtracker.stopTracker()
                dive.diveright()
                goaliepose()
                redballtracker.startTracker()
                count = 100
            


        initialredballposition= redballtracker.getPosition() #Resets the initial position so it looks for the ball again.
        count = 0
        counter = 0
