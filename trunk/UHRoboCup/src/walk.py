import motion

def stand():
    Head     = [+00, +00]

    LeftArm  = [+90, +00, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +00, -00, +00, +00, +00]
    RightLeg = [+00, -00, -00, +00, -00, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step1():
    Head     = [+00, +00]

    LeftArm  = [+45, +5, +00, +40, +00, +00]
    RightArm = [-45, -05, -00, -40, +00, +00]

    LeftLeg  = [+00, +4, -00, +00, +00, +00]
    RightLeg = [+00, +4, -60, +5, +50, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [+00, +00]

    LeftArm  = [+90, +90, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +2, +5, +00, +40, +00]
    RightLeg = [+00, +2, -00, +00, +00, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [+00, +00]

    LeftArm  = [+90, +90, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, -4, -00, +30, +00, +00]
    RightLeg = [+00, -4, -00, +00, -00, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():

    Head     = [+00, +00]

    LeftArm  = [+90, +90, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]


    LeftLeg  = [+00, +00, -00, +00, +00, +00]
    RightLeg = [+00, -00, +5, +00, +40, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles