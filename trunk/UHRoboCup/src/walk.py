import walk
import config
import camera
import time
motionProxy = config.loadProxy("ALMotion")
redballtracker = config.loadProxy("ALRedBallTracker")
def ewalk():

    #This walk walks for a walkTime amount of time and then stops.
    useSensors = True
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    angles = motionProxy.getAngles("Head", useSensors)
    X = 1.0
    Y = 0.0
    Theta = angles[0]/2.1
    Frequency = 1

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def stop():

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0
    Y = 0.0
    Theta = 0
    Frequency = 0

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ultimateWalkTo(x, y, z):
    # Set NAO in stiffness On
    config.stiffnessOn()

    # This example show customization for the both foot
    # with all the possible gait parameters
    motionProxy.walkTo(x, y, z,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.015],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front
def slowWalkTo(x, y, z):
    # Set NAO in stiffness On
    config.stiffnessOn()

    # This example show customization for the both foot
    # with all the possible gait parameters
    motionProxy.walkTo(x, y, z,
        [ ["MaxStepX", 0.007],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 1.667],  # low frequency
          ["StepHeight", 0.015],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front
def alignGoalie():
    config.stiffnessOn()
    config.poseInit()
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
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 1
                cameras = 0 # top camera
                times += 1
            elif redballtracker.isNewData() == False and count == 1:
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
                        walk.ultimateWalkTo(0, 0, 2)
                    elif headpitchangle > .5:
                        headpitchangle = .2
                    else:
                        headpitchangle = headpitchangle - 0.2
                    print headpitchangle
                else:
                    pass
        foundredballposition = redballtracker.getPosition()
        print "Found red ball position: ", foundredballposition
        redballtracker.stopTracker()
    walk.ultimatewalkto(0, foundredballposition[1], 0)
def walkClockwise():
    #This walk walks for a walkTime amount of time and then stops.
    useSensors = True
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    angles = motionProxy.getAngles("Head", useSensors)
    X = 0.0
    Y = -1.1 * .76
    Theta = -.15
    Frequency = 1
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def walkCounterclockwise():
    #This walk walks for a walkTime amount of time and then stops.
    useSensors = True
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    angles = motionProxy.getAngles("Head", useSensors)
    X = 0.0
    Y = 1.1 * .76
    Theta = .15
    Frequency = 1
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
