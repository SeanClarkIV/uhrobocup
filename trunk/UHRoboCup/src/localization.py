import math
import time
import camera
import config

motionProxy = config.loadProxy("ALMotion")
redballtracker = config.loadProxy("ALRedBallTracker")

def getnaolocation():
    naoID = "goallie"
    (naoX, naoY, naoZ) = motionProxy.getRobotPosition(False)
    return (naoX, naoY, naoZ, naoID)

def getlocation():
    # Set stiffnes ON
    config.StiffnessOn()

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
    while redballtracker.isActive(): # runs while loop as long as redballtracker is active
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
        redballtracker.stopTracker()
        return (foundredballposition[0], foundredballposition[1])
def getvelocity():
    # Set stiffnes ON
    config.StiffnessOn()

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
    redballposition=initialredballposition
    redballposition2=redballposition
    time1 = 0
    while redballposition==redballposition2: # runs while loop as long as redballtracker is active
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
        if time1 == 0:
            redballposition = redballtracker.getPosition()
            redballposition2 = redballposition
            time1 = time.time()
        elif redballtracker.getPosition != redballposition:
            if redballtracker.getPosition()<= redballposition*1.05 & redballtracker.getPosition >= redballposition*.95:
                redballposition2 = redballtracker.getPosition()
                time1 = time.time()
                redballposition=redballposition2
            else:
                redballposition2 = redballtracker.getPosition()
                time2 = time.time()

        # Ball found.
        # Store found red ball positon to variable.
        #foundredballposition and foundredballposition 2 are to make sure there are no
        #random jumps so the robot doesn't randomly pick a different thing to go to.
    xi = redballposition[0]
    yi = redballposition[1]
    xf = redballposition2[0]
    yf = redballposition2[1]
    deltax = xf-xi
    deltay = yf-yi
    deltat = time2-time1
    vx = deltax/deltat
    vy = deltay/deltat
    print "velocity x is: ", vx, "velocity y is: ", vy, "positioninitial is: ", redballposition, "positionfinal is: ", redballposition2
    redballtracker.stopTracker()
    magnitudeofdistance = (math.sqrt(math.pow(redballposition2[0]-redballposition2[0],2)+math.pow(redballposition2[1]-redballposition[1],2)))
    unitvectorx = (redballposition2[0]-redballposition[0])/magnitudeofdistance
    unitvectory = (redballposition2[1]-redballposition[1])/magnitudeofdistance
    xposition=redballposition2[0]
    yposition=redballposition2[1]
    return (vx, vy, unitvectorx, unitvectory, xposition,yposition)
