import config
import motion
motionProxy = config.loadProxy("ALMotion")
pNames = "Body"
def floor1():
    Head     = [+0, +0]

    LeftArm  = [+135, +90, +0, +0, +0, +0]
    RightArm = [+135, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -12, +0, +0, +8]
    RightLeg = [+0, +0, -12, +0, +0, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def floor2():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -10, +0, +0, +8]
    RightLeg = [+0, +4, -10, +0, -30, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def floor3():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +10, +0, +0, +0, +10]
    RightLeg = [+0, -10, +0, +100, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def floor4():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +8, +10, +0, +0, +8]
    RightLeg = [+0, +30, -90, +0, +40, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def kickinair1():
    config.StiffnessOn()
    motionProxy.angleInterpolationWithSpeed(pNames, floor1(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, floor2(), .2)
    motionProxy.angleInterpolationWithSpeed(pNames, floor3(), .2)
    motionProxy.angleInterpolationWithSpeed(pNames, floor4(), 1)
    motionProxy.angleInterpolationWithSpeed(pNames, floor3(), .2)
    config.PoseInit()
