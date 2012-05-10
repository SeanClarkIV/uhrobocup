import motion

def stand():
    Head     = [+00, +90]

    LeftArm  = [+90, +00, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +00, -00, +00, +00, +00]
    RightLeg = [+00, -00, -00, +00, -00, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step1():
    Head     = [+00, +00]

    LeftArm  = [+90, +80, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +5, -10, +00, +00, +10]
    RightLeg = [+00, +5, -10, +20, +00, +10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [+00, +00]

    LeftArm  = [+90, +80, +00, +00, +00, +00]
    RightArm = [+90, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +5, -10, +00, +00, +10]
    RightLeg = [+00, -00, -10, +20, -30, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [+00, +00]

    LeftArm  = [+90, +80, +00, +00, +00, +00]
    RightArm = [+180, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +5, -15, +00, +00, +10]
    RightLeg = [+00, -00, -10, +70, -40, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():
    Head     = [+00, +00]

    LeftArm  = [+90, +80, +00, +00, +00, +00]
    RightArm = [+180, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +5, -20, +00, +00, +10]
    RightLeg = [+00, -00, -60, +00, +50, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles