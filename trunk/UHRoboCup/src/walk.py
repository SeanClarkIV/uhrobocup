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
def walk():

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0.8
    Y = 0.0
    Theta = 0.0
    Frequency = 1.0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(walkTime)
def ewalk():

    #This walk walks for a walkTime amount of time and then stops.
    useSensors = True
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    angles = motionProxy.getAngles("Head", useSensors)
    X = 1.0
    Y = 0.0
    Theta = angles[0]/2.1
    Frequency = 0.5 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def stop():

    #This walk walks for a walkTime amount of time and then stops.
    useSensors = True
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    angles = motionProxy.getAngles("Head", useSensors)
    X = 0
    Y = 0.0
    Theta = 0
    Frequency = 0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def walkFowardto(x,y,z):
    #Set the velocity to zero to stop the walk
    Theta = z
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
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
def walkleft():

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0.0
    Y = 1.0
    Theta = 0.0
    Frequency = 1.0 # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(2)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def walkright():

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0.0
    Y = -1.0
    Theta = 0.0
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
    time.sleep(2.15)

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
    time.sleep(2.15)

    #Set the velocity to zero to stop the walk
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ultimatewalkto(x, y, z):
    # Set NAO in stiffness On
    config.StiffnessOn(motionProxy)
    theta = z

    # This example show customization for the both foot
    # with all the possible gait parameters
    motionProxy.walkTo(x, y, theta,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.015],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front

def ultimatewalktoball(x, y, z):
    # Set NAO in stiffness On
    config.StiffnessOn(motionProxy)
    x1 = x/5
    y1 = y/2
    theta = z/2

    # This example show customization for the both foot
    # with all the possible gait parameters
    motionProxy.walkTo(0, 0, theta,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.01],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front
    motionProxy.walkTo(0, 0, theta,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.01],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front
    motionProxy.walkTo(0, y1, 0,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.01],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front
    motionProxy.walkTo(0, y1, 0,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.01],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front
    motionProxy.walkTo(x1, 0, 0,
        [ ["MaxStepX", 0.06],         # step of x cm in front
          ["MaxStepY", 0.101],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.012],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front  
    motionProxy.walkTo(x1, 0, 0,
        [ ["MaxStepX", 0.06],         # step of x cm in front
          ["MaxStepY", 0.101],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.012],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front
