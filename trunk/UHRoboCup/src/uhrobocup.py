#-*- coding: iso-8859-15 -*-

''' PoseInit: Small example to make Nao go to an initial position. '''

import config
import motion
import time

def stand():
    Head     = [+00, +00]

    LeftArm  = [+90, +00, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +00, -00, +00, +00, +00]
    RightLeg = [+00, -00, -00, +00, -00, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def kick1():
    Head     = [+00, +00]

    LeftArm  = [+90, +00, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +02, -00, +00, +00, +02]
    RightLeg = [+00, -00, -00, +00, -00, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def kick():
    Head     = [+00, +00]

    LeftArm  = [+90, +90, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +10, -20, +00, +00, +10]
    RightLeg = [+00, -20, -20, +90, -40, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def kick2():
    Head     = [+00, +00]

    LeftArm  = [+90, +90, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +10, -20, +00, +00, +10]
    RightLeg = [+00, -20, -20, +00, -10, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def main():
    proxy = config.loadProxy("ALMotion")
    motionProxy = config.loadProxy("ALMotion")

    #We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

    # Get the Robot Configuration
    robotConfig = proxy.getRobotConfig()
    robotName = ""

    # Convert to radians
    

    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
    pMaxSpeedFraction = 0.1
    pMaxSpeedFraction2 = 1.0
    # Ask motion to do this with a blocking call
    proxy.angleInterpolationWithSpeed(pNames, stand(), pMaxSpeedFraction)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick1(), pMaxSpeedFraction)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick(), pMaxSpeedFraction)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick2(), pMaxSpeedFraction2)

if __name__ == "__main__":
    main()
