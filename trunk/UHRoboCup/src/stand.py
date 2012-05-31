import config
import motion

proxy = config.loadProxy("ALMotion")
pNames = "Body"
def stand():
    Head     = [+0, +0]

    LeftArm  = [+90, +0, +0, +0, +0, +0]
    RightArm = [+90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +00, +0, +0, +0, +0]
    RightLeg = [+0, -00, +0, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step():
    Head     = [+0, +0]

    LeftArm  = [+110, +40, +20, -90, +0, +0]
    RightArm = [+110, -40, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +00, +0, +0]
    RightLeg = [+0, -0, -90, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step1():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +00, +0, +0]
    RightLeg = [+0, -0, -90, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -40, +00, +0, +0]
    RightLeg = [+0, -0, -40, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -70, +0, +0]
    RightArm = [+110, -20, -10, +70, +0, +0]

    LeftLeg  = [-50, +0, -90, +70, +80, +0]
    RightLeg = [-50, -0, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -00, +0, +0]
    RightArm = [+110, -20, -10, +00, +0, +0]

    LeftLeg  = [-90, +20, -90, +70, +50, +0]
    RightLeg = [-90, -20, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step5():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -00, +0, +0]
    RightArm = [+110, -20, -10, +00, +0, +0]

    LeftLeg  = [-90, +20, -50, +121, -25, -40]
    RightLeg = [-90, -20, -90, +30, +30, +20]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step6():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -00, +0, +0]
    RightArm = [+110, -20, -10, +00, +0, +0]

    LeftLeg  = [-90, +20, -50, +121, -20, -40]
    RightLeg = [-90, -20, -90, +121, -20, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step7():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -00, +0, +0]
    RightArm = [+110, -20, -10, +00, +0, +0]

    LeftLeg  = [-90, -0, -90, +121, -10, -10]
    RightLeg = [-90, +0, -90, +121, -10, +10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step8():
    Head     = [+0, -90]

    LeftArm  = [-90, -90, -90, -90, +0, +0]
    RightArm = [-90, +90, +90, +90, +0, +0]

    LeftLeg  = [-90, +90, -40, +00, +70, -00]
    RightLeg = [-90, -90, -40, +00, +70, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step9():
    Head     = [+0, -90]

    LeftArm  = [+40, -20, -00, -00, +00, +0]
    RightArm = [+40, +20, +00, +00, +00, +0]

    LeftLeg  = [-90, +90, -180, +00, +70, -00]
    RightLeg = [-90, -90, -180, +00, +70, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step10():
    Head     = [+0, -90]

    LeftArm  = [+00, +90, -00, -0, +0, +0]
    RightArm = [+00, -90, +00, +0, +0, +0]

    LeftLeg  = [-90, +90, -100, +0, +90, -00]
    RightLeg = [-90, -90, -100, +0, +90, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step11():
    Head     = [+0, -90]

    LeftArm  = [+40, +90, +0, -00, +0, +0]
    RightArm = [+40, -90, -0, +00, +0, +0]

    LeftLeg  = [-90, +90, -100, +20, +90, -00]
    RightLeg = [-90, -90, -100, +20, +90, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step12():
    Head     = [+0, -90]

    LeftArm  = [-45, +0, +0, -00, +0, +0]
    RightArm = [-45, -0, -0, +00, +0, +0]

    LeftLeg  = [-0, +0, -100, +0, +0, -00]
    RightLeg = [-0, -0, -100, +0, +0, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step13():
    Head     = [+0, -90]

    LeftArm  = [-90, +00, +0, -00, +0, +0]
    RightArm = [-90, +00, -0, +00, +0, +0]

    LeftLeg  = [-0, +0, -00, +0, -0, -00]
    RightLeg = [-0, -0, -00, +0, -0, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def standuponback():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step(), 0.8)
    proxy.angleInterpolationWithSpeed(pNames, step1(), 0.8)
    proxy.angleInterpolationWithSpeed(pNames, step2(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step3(), 0.6)
    proxy.angleInterpolationWithSpeed(pNames, step4(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step5(), 0.46)
    proxy.angleInterpolationWithSpeed(pNames, step6(), 0.45)
    proxy.angleInterpolationWithSpeed(pNames, step7(), 0.4)
    proxy.angleInterpolationWithSpeed(pNames, stand(), 0.4)
def standuponfront():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step13(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step8(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step9(), 0.2)
    proxy.angleInterpolationWithSpeed(pNames, step10(), 0.2)
    proxy.angleInterpolationWithSpeed(pNames, step11(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step12(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step4(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step5(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step6(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step7(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, stand(), 0.1)
