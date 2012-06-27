import stand
import config
import motion
import time
motionProxy = config.loadProxy("ALMotion")
pNames = "Body"
def dive1():
    Head     = [+0, +0]

    LeftArm  = [+90, +20, +0, +0, +0, +0]
    RightArm = [+90, -20, +0, +0, +0, +0]

    LeftLeg  = [+0, 00, -55, +121, -90, +0]
    RightLeg = [+0, 00, -55, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveleft1():
    Head     = [+0, +0]

    LeftArm  = [-90, 0, +0, +0, +0, +0]
    RightArm = [-90, -0, +0, +0, +0, +0]

    LeftLeg  = [+0, -0, -55, +121, -90, +0]
    RightLeg = [+0, -00, -00, +0, -0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveleft2():
    Head     = [+0, +0]

    LeftArm  = [+0, +0, +90, -60, +0, +0]
    RightArm = [+0, -0, +0, +90, +0, +0]

    LeftLeg  = [+0, -0, -90, +121, -00, +0]
    RightLeg = [+0, -0, -90, +121, -0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveleft3():
    Head     = [+0, +0]

    LeftArm  = [-90, +0, +0, -0, +0, +0]
    RightArm = [+0, -0, +90, +90, +0, +0]

    LeftLeg  = [+0, -0, -00, +121, -90, +0]
    RightLeg = [+0, -0, -90, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveleft4():
    Head     = [+0, +0]

    LeftArm  = [-0, +0, -90, -90, +0, +0]
    RightArm = [+0, -0, +90, +90, +0, +0]

    LeftLeg  = [-65.6, -0, -120, +121, -90, +0]
    RightLeg = [-65.6, -0, -120, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveleft5():
    Head     = [+0, +0]

    LeftArm  = [+20, +0, -90, -0, +0, +0]
    RightArm = [+20, -0, +90, +00, +0, +0]

    LeftLeg  = [-65.6, -0, -120, +00, -30, +0]
    RightLeg = [-65.6, -0, -120, +00, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveright1():
    Head     = [+0, +0]

    LeftArm  = [-90, 0, +0, +0, +0, +0]
    RightArm = [-90, -0, +0, +0, +0, +0]

    LeftLeg  = [+0, -0, -00, +00, -00, +0]
    RightLeg = [+0, -00, -55, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveright2():
    Head     = [+0, +0]

    LeftArm  = [+0, +0, +00, -90, +0, +0]
    RightArm = [+0, -0, -90, +60, +0, +0]

    LeftLeg  = [+0, -0, -90, +121, -00, +0]
    RightLeg = [+0, -0, -90, +121, -0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveright3():
    Head     = [+0, +0]

    LeftArm  = [-00, +0, -90, -90, +0, +0]
    RightArm = [-90, -0, +00, +00, +0, +0]

    LeftLeg  = [+0, -0, -90, +121, -90, +0]
    RightLeg = [+0, -0, -00, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveright4():
    Head     = [+0, +0]

    LeftArm  = [-0, +0, +90, +90, +0, +0]
    RightArm = [+0, -0, -90, -90, +0, +0]

    LeftLeg  = [-65.6, -0, -120, +121, -90, +0]
    RightLeg = [-65.6, -0, -120, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveright5():
    Head     = [+0, +0]

    LeftArm  = [+20, +0, +90, -0, +0, +0]
    RightArm = [+20, -0, -90, +00, +0, +0]

    LeftLeg  = [-65.6, -0, -120, +00, -30, +0]
    RightLeg = [-65.6, -0, -120, +00, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def diveleft():
    config.StiffnessOn()
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, dive1(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, diveleft1(), 1)
    time.sleep(3)
    motionProxy.setFallManagerEnabled(True)
    motionProxy.angleInterpolationWithSpeed(pNames, diveleft2(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, diveleft3(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, diveleft4(), 1)
    motionProxy.angleInterpolationWithSpeed(pNames, diveleft5(), 1)
    stand.standfromsit()
def diveright():
    config.StiffnessOn()
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, dive1(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, diveright1(), 1)
    time.sleep(3)
    motionProxy.setFallManagerEnabled(True)
    motionProxy.angleInterpolationWithSpeed(pNames, diveright2(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, diveright3(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, diveright4(), 1)
    motionProxy.angleInterpolationWithSpeed(pNames, diveright5(), 1)
    stand.standfromsit()