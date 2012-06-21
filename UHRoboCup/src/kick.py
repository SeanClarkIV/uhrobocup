import config
import motion

motionProxy = config.loadProxy("ALMotion")
pNames = "Body"

def stand():
    Head     = [+0, +90]

    LeftArm  = [+90, +0, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, +0, +0, +0, +0]
    RightLeg = [+0, +0, +0, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step1():
    Head     = [+0, +0]

    LeftArm  = [+135, +90, +0, +0, +0, +0]
    RightArm = [+135, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -10, +0, +0, +8]
    RightLeg = [+0, +0, -10, +0, +0, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step5():
    Head     = [+0, +0]

    LeftArm  = [+135, +0, +0, +0, +0, +0]
    RightArm = [+135, -90, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -10, +0, +0, -8]
    RightLeg = [+0, +0, -10, +0, +0, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -10, +0, +0, +8]
    RightLeg = [+0, +4, -10, +0, -10, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+180, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -15, +0, +0, +10]
    RightLeg = [+0, +0, -10, +60, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():
    Head     = [+0, +0]

    LeftArm  = [+90, +50, +0, +0, +0, +0]
    RightArm = [+180, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -12, +0, +0, +1]
    RightLeg = [+0, +0, -40, +0, +10, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step5():
    Head     = [+0, +0]

    LeftArm  = [+135, +0, +0, +0, +0, +0]
    RightArm = [+135, -90, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -10, +0, +0, -8]
    RightLeg = [+0, +0, -10, +0, +0, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step6():
    Head     = [+0, +0]

    LeftArm  = [+90, +0, +0, +0, +0, +0]
    RightArm = [+90, -80, +0, +0, +0, +0]

    LeftLeg  = [+0, -4, -10, +0, -10, -8]
    RightLeg = [+0, -4, -10, +0, +0, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step7():
    Head     = [+0, +0]

    LeftArm  = [+180, +0, +0, +0, +0, +0]
    RightArm = [+90, -80, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -10, +60, -30, +0]
    RightLeg = [+0, -4, -15, +0, +0, -10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step8():
    Head     = [+0, +0]

    LeftArm  = [+180, +0, +0, +0, +0, +0]
    RightArm = [+90, -50, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -40, +0, +10, +0]
    RightLeg = [+0, -4, -12, +0, +0, -7]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def kickRightFoot():    # Kick ball with right foot.
    config.StiffnessOn(motionmotionProxy)   # Turns the stiffness on.

    motionmotionProxy.angleInterpolationWithSpeed(pNames, step1(), 0.1)
    motionmotionProxy.angleInterpolationWithSpeed(pNames, step2(), 0.5)
    motionmotionProxy.angleInterpolationWithSpeed(pNames, step3(), 0.4)
    motionmotionProxy.angleInterpolationWithSpeed(pNames, step4(), 1.0)
    motionmotionProxy.angleInterpolationWithSpeed(pNames, step1(), 0.2)
    config.PoseInit(motionProxy, 0.5)

def kickLeftFoot():     # Kick ball with left foot.
    config.StiffnessOn(motionProxy) #Turns the stiffness on.

    motionProxy.angleInterpolationWithSpeed(pNames, step5(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, step6(), 0.5)
    motionProxy.angleInterpolationWithSpeed(pNames, step7(), 0.4)
    motionProxy.angleInterpolationWithSpeed(pNames, step8(), 1.0)
    motionProxy.angleInterpolationWithSpeed(pNames, step5(), 0.1)
    config.PoseInit(motionProxy, 0.5)