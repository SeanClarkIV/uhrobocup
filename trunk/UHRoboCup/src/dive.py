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
def dive2():
    Head     = [+0, +0]

    LeftArm  = [-90, 0, +0, +0, +0, +0]
    RightArm = [-90, -0, +0, +0, +0, +0]

    LeftLeg  = [+0, -0, -55, +121, -90, +0]
    RightLeg = [+0, -00, -00, +0, -0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive3():
    Head     = [+0, +0]

    LeftArm  = [-90, 0, +0, +0, +0, +0]
    RightArm = [-90, -0, +0, +0, +0, +0]

    LeftLeg  = [+0, -0, -00, +0, +90, +0]
    RightLeg = [+0, -0, -00, +0, +90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive4():
    Head     = [+0, +0]

    LeftArm  = [+0, +0, +90, -60, +0, +0]
    RightArm = [+0, -0, +0, +90, +0, +0]

    LeftLeg  = [+0, -0, -90, +121, -00, +0]
    RightLeg = [+0, -0, -90, +121, -0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive5():
    Head     = [+0, +0]

    LeftArm  = [-90, +0, +0, -0, +0, +0]
    RightArm = [+0, -0, +90, +90, +0, +0]

    LeftLeg  = [+0, -0, -00, +121, -90, +0]
    RightLeg = [+0, -0, -90, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive6():
    Head     = [+0, +0]

    LeftArm  = [-0, +0, -90, -90, +0, +0]
    RightArm = [+0, -0, +90, +90, +0, +0]

    LeftLeg  = [-65.6, -0, -120, +121, -90, +0]
    RightLeg = [-65.6, -0, -120, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive7():
    Head     = [+0, +0]

    LeftArm  = [+20, +0, -90, -0, +0, +0]
    RightArm = [+20, -0, +90, +00, +0, +0]

    LeftLeg  = [-65.6, -0, -120, +121, -30, +0]
    RightLeg = [-65.6, -0, -120, +121, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive8():
    Head     = [+0, +0]

    LeftArm  = [+20, +0, -90, -0, +0, +0]
    RightArm = [+20, -0, +90, +00, +0, +0]

    LeftLeg  = [-20, -0, -55, +121, -90, +0]
    RightLeg = [-20, -0, -55, +121, -90, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive():
    config.StiffnessOn(motionProxy)
    motionProxy.angleInterpolationWithSpeed(pNames, dive1(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, dive2(), 1)
    time.sleep(1)
    motionProxy.angleInterpolationWithSpeed(pNames, dive3(), .5)
    time.sleep(3)
    motionProxy.angleInterpolationWithSpeed(pNames, dive4(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, dive5(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, dive6(), 1)
    motionProxy.angleInterpolationWithSpeed(pNames, dive7(), 1)
    motionProxy.angleInterpolationWithSpeed(pNames, dive8(), 1)
    motionProxy.angleInterpolationWithSpeed(pNames, dive1(), .5)