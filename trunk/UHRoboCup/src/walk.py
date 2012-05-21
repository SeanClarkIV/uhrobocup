import time
import config
import motion

""" WALKING STEPS GO HERE

# Walking steps for each indivicual move

def walkStep1():
    Head     = [+00, +00]

    LeftArm  = [+00, +00, +00, +00, +00, +00]
    RightArm = [+00, +00, +00, +00, +00, +00]

    LeftLeg  = [+00, +00, +00, +00, +00, +00]
    RightLeg = [+00, +00, +00, +00, +00, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
"""
## def walkStep1():
##  Head     = [+00, +00]

  ##  LeftArm  = [+00, +00, +00, +00, +00, +00]
 ##   RightArm = [+00, +00, +00, +00, +00, +00]

   ## LeftLeg  = [+00, +00, +00, +00, +00, +00]
   ## RightLeg = [+00, +00, +00, +00, +00, +00]

   ## pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
   ## pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
   ## return pTargetAngles
#This function makes the robot walk full speed for y seconds.
def walkTimed(walkTime):

    motionProxy = config.loadProxy("ALMotion")
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 1.0
    Y = 0.0
    Theta = 0.0
    Frequency = 1.0 # max speed

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(walkTime)

    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)