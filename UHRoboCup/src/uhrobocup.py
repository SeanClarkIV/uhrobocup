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

    return (Head + LeftArm + LeftLeg + RightLeg + RightArm)

def kick1():
    Head     = [+00, +00]

    LeftArm  = [+90, +00, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +05, -00, +00, +00, +05]
    RightLeg = [+00, -00, -00, +00, -00, +00]

    return (Head + LeftArm + LeftLeg + RightLeg + RightArm)

def kick():
    Head     = [+00, +00]

    LeftArm  = [+90, +90, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +10, -20, +00, +00, +10]
    RightLeg = [+00, -20, -20, +90, -50, +00]

    return (Head + LeftArm + LeftLeg + RightLeg + RightArm)

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



    # Gather the joints together
    pTargetAngles = stand()

    # Convert to radians
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]

    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
    pMaxSpeedFraction = 0.1
    # Ask motion to do this with a blocking call
    proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)

if __name__ == "__main__":
    main()
