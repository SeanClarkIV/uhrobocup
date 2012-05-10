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

    LeftArm  = [+135, +0, +00, +40, +00, +00]
    RightArm = [+45, -00, -00, -40, +00, +00]

    LeftLeg  = [+00, +02, -30, +40, +00, +00]
    RightLeg = [+00, +02, -30, +00, +20, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [+00, +00]

    LeftArm  = [+45, +00, +00, +00, +00, +00]
    RightArm = [+135, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, +2, -30, +00, +20, +00]
    RightLeg = [+00, +2, -30, +20, -10, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [+00, +00]

    LeftArm  = [+135, +00, +00, +40, +00, +00]
    RightArm = [+45, -00, -00, -40, +00, +00]

    LeftLeg  = [+00, -02, -30, +00, +20, +00]
    RightLeg = [+00, -02, -30, +40, +00, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():
    Head     = [+00, +00]

    LeftArm  = [+45, +00, +00, +00, +00, +00]
    RightArm = [+135, -00, -00, -00, +00, +00]

    LeftLeg  = [+00, -2, -30, +20, -10, +00]
    RightLeg = [+00, -2, -30, +00, +20, +00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles