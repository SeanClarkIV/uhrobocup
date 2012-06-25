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

def right1():
    Head     = [+0, +0]

    LeftArm  = [+135, +90, +0, +0, +0, +0]
    RightArm = [+135, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -12, +0, +0, +8]
    RightLeg = [+0, +0, -12, +0, +0, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles




def right2():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -10, +0, +0, +8]
    RightLeg = [+0, +4, -10, +0, -10, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def right3():
    Head     = [+0, +0]

    LeftArm  = [+90, +80, +0, +0, +0, +0]
    RightArm = [+180, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +04, -12, +0, +0, +9]
    RightLeg = [+0, +0, -10, +60, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def right4():
    Head     = [+0, +0]

    LeftArm  = [+90, +50, +0, +0, +0, +0]
    RightArm = [+180, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +4, -12, +0, +0, +1]
    RightLeg = [+0, +0, -40, +0, +10, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left1():
    Head     = [+0, +0]

    LeftArm  = [+135, +0, +0, +0, +0, +0]
    RightArm = [+135, -90, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -12, +0, +0, -8]
    RightLeg = [+0, +0, -12, +0, +0, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left2():
    Head     = [+0, +0]

    LeftArm  = [+90, +0, +0, +0, +0, +0]
    RightArm = [+90, -80, +0, +0, +0, +0]

    LeftLeg  = [+0, -04.5, -10, +0, -10, -8]
    RightLeg = [+0, -04.5, -10, +0, +0, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left3():
    Head     = [+0, +0]

    LeftArm  = [+180, +0, +0, +0, +0, +0]
    RightArm = [+90, -80, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -10, +60, -30, +0]
    RightLeg = [+0, -04, -12, +0, +0, -9]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def left4():
    Head     = [+0, +0]

    LeftArm  = [+180, +0, +0, +0, +0, +0]
    RightArm = [+90, -50, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, -40, +0, +10, +0]
    RightLeg = [+0, -4, -12, +0, +0, -7]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def kickRightFoot():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, right1(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, right2(), 0.4)
    proxy.angleInterpolationWithSpeed(pNames, right3(), 0.4)
    proxy.angleInterpolationWithSpeed(pNames, right4(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, right1(), 0.2)

def kickLeftFoot():# Kick ball with left foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, left1(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, left2(), 0.3)
    proxy.angleInterpolationWithSpeed(pNames, left3(), 0.4)
    proxy.angleInterpolationWithSpeed(pNames, left4(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, left1(), 0.2)