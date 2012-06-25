def step1():
    Head     = [+0, +0]

    LeftArm  = [+40, +0, +40, +0, +0, +0]
    RightArm = [+40, +0, -40, +0, +0, +0]

    LeftLeg  = [+0, +4, +0, +0, +0, -5]
    RightLeg = [+0, +0, +0, +100, -29.6 +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def kickinair():
    config.StiffnessOn(motionProxy)
    motionProxy.angleInterpolationWithSpeed(pNames, step1(), 0.1)
