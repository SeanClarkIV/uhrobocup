import time
import config

""" WALKING STEPS GO HERE

# Walking steps for each indivicual move

def walkStep1():
    Head     = [+0, +0]

    LeftArm  = [+0, +0, +0, +0, +0, +0]
    RightArm = [+0, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, +0, +0, +0, +0]
    RightLeg = [+0, +0, +0, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
"""

def walkFowardTimed(walkTime):

    #This walk walks for a walkTime amount of time and then stops. 
    motionProxy = config.loadProxy("ALMotion")
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
def walkBackTimed(walkTime):

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy = config.loadProxy("ALMotion")
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
    motionProxy = config.loadProxy("ALMotion")
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
    motionProxy = config.loadProxy("ALMotion")
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