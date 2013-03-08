import stand
import config
import motion
motionProxy = config.loadProxy("ALMotion")
pNames = "Body"
def goaliePosition():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-10, +0, -50, +121, -68, +0]
    RightLeg = [-10, 00, -50, +121, -68, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def goalieSit():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-50.3, -1, -89, +97.5, +38, +15.7]
    RightLeg = [-50.3, +1, -89, +97.5, +38, -15.7]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveLeft1():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-65.6, 38, -38.3, -5.3, +52.9, -3.8]
    RightLeg = [-65.6, -79.1, -83.4, +66.6, 53.4, +2.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveRight1():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-65.6, 79.1, -83.4, 66.6, +53.4, 2.2]
    RightLeg = [-65.6, -38, -38.3, -5.3, 52.9,-3.8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def goaliePose():
    config.stiffnessOn()
    motionProxy.angleInterpolationWithSpeed(pNames, goaliePosition(), 0.3)
def diveLeft():
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goaliePosition(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, goalieSit(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, diveLeft1(), .1)
    motionProxy.setFallManagerEnabled(True)
    stand.standFromSit()
    goaliePose()
def diveRight():
    config.stiffnessOn()
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goaliePosition(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, goalieSit(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, diveRight1(), .1)
    motionProxy.setFallManagerEnabled(True)
    stand.standFromSit()
    goaliePose()
def diveLeftGoal():
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goalieSit(), .8)
    motionProxy.angleInterpolationWithSpeed(pNames, diveLeft1(), .7)
    motionProxy.setFallManagerEnabled(True)
    stand.standFromSit()
    goaliePose()
def diveRightGoal():
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goalieSit(), .8)
    motionProxy.angleInterpolationWithSpeed(pNames, diveRight1(), .7)
    motionProxy.setFallManagerEnabled(True)
    stand.standFromSit()
    goaliePose()