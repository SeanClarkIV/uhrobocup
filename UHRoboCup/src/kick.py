import config
import motion

motionProxy = config.load_proxy("ALMotion")
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

def right_1():
    Head     = [+0, +0]

    LeftArm  = [+135, +90, +0, +0, +0, +0]
    RightArm = [+135, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -12, +0, +0, +8]
    RightLeg = [+0, +0, -12, +0, +0, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles




def right_2():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -10, +0, +0, +8]
    RightLeg = [+0, +4, -10, +0, -10, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def right_3():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+180, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +04, -12, +0, +0, +9]
    RightLeg = [+0, +0, -10, +60, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def right_4():
    Head     = [+0, +0]

    LeftArm  = [+90, +50, +0, +0, +0, +0]
    RightArm = [+180, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -12, +0, +0, +10]
    RightLeg = [+0, +0, -40, +0, +10, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left_1():
    Head     = [+0, +0]

    LeftArm  = [+135, +0, +0, +0, +0, +0]
    RightArm = [+135, -90, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -12, +0, +0, -8]
    RightLeg = [+0, +0, -12, +0, +0, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left_2():
    Head     = [+0, +0]

    LeftArm  = [+90, +0, +0, +0, +0, +0]
    RightArm = [+90, -80, +0, +0, +0, +0]

    LeftLeg  = [+0, -04.5, -10, +0, -10, -8]
    RightLeg = [+0, -04.5, -10, +0, +0, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left_3():
    Head     = [+0, +0]

    LeftArm  = [+180, +0, +0, +0, +0, +0]
    RightArm = [+90, -80, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -10, +60, -30, +0]
    RightLeg = [+0, -04, -12, +0, +0, -9]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left_4():
    Head     = [+0, +0]

    LeftArm  = [+180, +0, +0, +0, +0, +0]
    RightArm = [+90, -50, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -40, +0, +10, +0]
    RightLeg = [+0, -4, -12, +0, +0, -7]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def kick_right_foot():# Kick ball with right foot.
    #Turns the stiffness on.
    config.stiffness_on()
    motionProxy.angleInterpolationWithSpeed(pNames, right_1(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, right_2(), 0.4)
    motionProxy.angleInterpolationWithSpeed(pNames, right_3(), 0.4)
    motionProxy.angleInterpolationWithSpeed(pNames, right_4(), 1.0)
    motionProxy.angleInterpolationWithSpeed(pNames, right_1(), 0.2)

def kick_left_foot():# Kick ball with left foot.
    #Turns the stiffness on.
    config.stiffness_on()
    motionProxy.angleInterpolationWithSpeed(pNames, left_1(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, left_2(), 0.3)
    motionProxy.angleInterpolationWithSpeed(pNames, left_3(), 0.4)
    motionProxy.angleInterpolationWithSpeed(pNames, left_4(), 1.0)
    motionProxy.angleInterpolationWithSpeed(pNames, left_1(), 0.2)
