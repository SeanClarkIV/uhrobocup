import time
import config

motionProxy = config.loadProxy("ALMotion")

def walkFowardTimed(walkTime):

    #This walk walks for a walkTime amount of time and then stops. 
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0.8
    Y = 0.0
    Theta = 0.0
    Frequency = 1.0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(walkTime)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def walkFowardto(x,y,z):
    t=0
    x2=100
    while x2>0:
        x1= 0 + 1
        x2= x - x1
        t= t + 1
    x1= x1 - 1
    x2= x - x1
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = x1
    Y = 0
    Theta = 0
    Frequency = 1.0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(t)

    #Set the velocity to zero to stop the walk
    X = x2
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(1)
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

    t=0
    y2= 100
    while y2>0:
        y1= 0 + 1
        y2= y - y1
        t= t + 1
    y1= y1 - 1
    y2= y - y1
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0
    Y = y1
    Theta = 0
    Frequency = 1.0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(t)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = y2
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(1)
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

    t=0
    z2= 100
    while z2>0:
        z1= 0 + 1
        z2=z - z1
        t= t + 1
    z1= z1-1
    z2= z - z1
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0
    Y = 0
    Theta = z1
    Frequency = 1.0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(t)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = 0.0
    Theta = z2
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(1)
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def walkBackTimed(walkTime):

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = -0.8
    Y = 0.0
    Theta = 0.0
    Frequency = 1.0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(walkTime)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def turnleft():

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0.0
    Y = 0.0
    Theta = 1.0
    Frequency = 1.0 # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(2)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def turnright():

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0.0
    Y = 0.0
    Theta = -1.0
    Frequency = 1.0 # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(2)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ultimatewalkto():
    # Set NAO in stiffness On
    config.StiffnessOn(motionProxy)

    x     = 1
    y     = 0.0
    theta = 0.0

    # This example show customization for the both foot
    # with all the possible gait parameters
    motionProxy.walkTo(x, y, theta,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.101],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 1.667],  # low frequency
          ["StepHeight", 0.01],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front

    # This example show customization for the both foot
    # with just one gait parameter, in this case, the other
    # parameters are set to the default value
    motionProxy.walkTo(x, y, theta, [ ["StepHeight", 0.007] ]) # step height of 4 cm