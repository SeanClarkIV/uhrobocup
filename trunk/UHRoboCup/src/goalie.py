import walk
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
    motionProxy.angleInterpolationWithSpeed(pNames, dive.goalieposition(), .5)
def goalie():
    walk.aligngoalie()
    goaliepose()
    initialredballposition = redballtracker.getPosition() #Set the inital position as the first position the head is in,
    #assume the ball isnt the inital position
    camera.topCamera()
    redballtracker.startTracker()           #Starting the tracker.
    redballtracker.setWholeBodyOn(True)
    counter = 0
    count = 0
    while True:
        times = 0;
        headpitchangle = 1.433;
        while redballtracker.getPosition() == initialredballposition:  # Ball lost.
            if redballtracker.isNewData() == False and count == 0: # Ball still lost.true if a new Red Ball was detected since the last getPosition().
                print "Looking for red ball"
                camera.topCamera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 1
                cameras = 0 # top camera
                times += 1
            elif redballtracker.isNewData() == False and count == 1:
                camera.bottomCamera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 0
                cameras = 1 # bottom camera
                times += 1
            if times > 1:
                number = float(times)
                if number % 2 == 1:
                    if headpitchangle < 0:
                        headpitchangle = 1.433
                    elif headpitchangle > .5:
                        headpitchangle = .2
                    else:
                        headpitchangle = headpitchangle - 0.2
                else:
                    pass
        if counter == 0:     #This is for the first time to define redballposition since it will be updated after redballposition2
            redballposition = redballtracker.getPosition()
            counter == 1
        redballposition2 = redballposition   #redballposition2 stores the old position of the ball and we get the difference of them
        print "redballposition2 :",   redballposition2
        while count < 100:
            ##redballtracker.startTracker() #Starts tracker again just in case. 
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
                dive.diveleftgoal()
                goaliepose()
                redballtracker.startTracker()
                count = 100
            elif velocity >= .2 and redballposition[1] < -.1 and redballposition[0] < 2:
                redballtracker.stopTracker()
                dive.diverightgoal()
                goaliepose()
                redballtracker.startTracker()
                count = 100
            elif velocity == 0:   #If the ball has not moved the count goes up by one and if reaches 100 looks for ball again.
                count += 1
            '''elif velocity >= 1 and redballposition[1] > .1 and redballposition[0] < 1.5:    #If the ball is moving quickly it will dive left if parameters are met
                redballtracker.stopTracker()
                dive.diveleftgoal()
                goaliepose()
                redballtracker.startTracker()
                count = 100
            elif velocity >= 1 and redballposition[1] < -.1 and redballposition[0] < 1.5:
                redballtracker.stopTracker()
                dive.diverightgoal()
                goaliepose()
                redballtracker.startTracker()
                count = 100'''
            
            


        initialredballposition= redballtracker.getPosition() #Resets the initial position so it looks for the ball again.
        count = 0
        counter = 0
def goalieimproved():
    # Set stiffnes ON
    config.StiffnessOn()
    config.PoseInit()
    #Make sure top camera is active
    camera.topCamera()

    # Start looking for red ball to track.
    redballtracker.stopTracker()
    redballtracker.startTracker()
    redballtracker.setWholeBodyOn(True)
    print "Tracking red ball"

    #Store initial red ball positon to variable
    initialredballposition = redballtracker.getPosition()
    print "Initial Position: ", initialredballposition
    cameras = 0 #Top camera
    count = 0
    counter = 0 #Used for Redballposition
    times = 0
    headpitchangle = 1.433
    blank = 0
    while blank==0: # runs while loop as long as redballtracker is active
        while redballtracker.getPosition() == initialredballposition:  # Ball lost.
            if redballtracker.isNewData() == False and count == 0: # Ball still lost.true if a new Red Ball was detected since the last getPosition().
                print "Looking for red ball"
                camera.topCamera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 1
                cameras = 0 # top camera
                times += 1
            elif redballtracker.isNewData() == False and count == 1:
                camera.bottomCamera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 0
                cameras = 1 # bottom camera
                times += 1
            # the next if condition is to look up slightly if he can't find the ball and then when it looks up 3 times
            # it decides turns left and starts all over again.
            if times > 1:
                number = float(times)
                if number % 2 == 1:
                    if headpitchangle < 0:
                        headpitchangle = 1.433
                        walk.ultimatewalkto(0, 0, 2)
                    elif headpitchangle > .5:
                        headpitchangle = .2
                    else:
                        headpitchangle = headpitchangle - 0.2
                    print headpitchangle
                else:
                    pass
        # Ball found.
        # Store found red ball positon to variable.
        #foundredballposition and foundredballposition 2 are to make sure there are no
        #random jumps so the robot doesn't randomly pick a different thing to go to.
        if counter == 0:
            foundredballposition2 = redballtracker.getPosition()
        foundredballposition = foundredballposition2
        foundredballposition2 = redballtracker.getPosition()
        print "Found red ball position: ", foundredballposition2
        blank = 1
    walk.walkclockwise()
    while foundredballposition2[1]<-.25:
        foundredballposition2= redballtracker.getPosition()
        print "Walking!", foundredballposition2[1]
    redballtracker.stopTracker()
    walk.stop()
    goaliepose()