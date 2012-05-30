import config
import motion

proxy = config.loadProxy("ALMotion")
pNames = "Body"
def crouch():
  ''' Makes NAO crouch. '''
  names = list()
  times = list()
  keys = list()

  names.append("HeadYaw")
  times.append([ 1.00000])
  keys.append([ -0.03379])

  names.append("HeadPitch")
  times.append([ 1.00000])
  keys.append([ 0.32823])

  names.append("LShoulderPitch")
  times.append([ 1.00000])
  keys.append([ 1.62600])

  names.append("LShoulderRoll")
  times.append([ 1.00000])
  keys.append([ -0.01998])

  names.append("LElbowYaw")
  times.append([ 1.00000])
  keys.append([ -0.98640])

  names.append("LElbowRoll")
  times.append([ 1.00000])
  keys.append([ -1.24250])

  names.append("LWristYaw")
  times.append([ 1.00000])
  keys.append([ 0.08433])

  names.append("LHand")
  times.append([ 1.00000])
  keys.append([ 0.00015])

  names.append("RShoulderPitch")
  times.append([ 1.00000])
  keys.append([ 1.51870])

  names.append("RShoulderRoll")
  times.append([ 1.00000])
  keys.append([ -0.05680])

  names.append("RElbowYaw")
  times.append([ 1.00000])
  keys.append([ 0.72554])

  names.append("RElbowRoll")
  times.append([ 1.00000])
  keys.append([ 1.26099])

  names.append("RWristYaw")
  times.append([ 1.00000])
  keys.append([ 0.72094])

  names.append("RHand")
  times.append([ 1.00000])
  keys.append([ 0.00018])

  names.append("LHipYawPitch")
  times.append([ 1.00000])
  keys.append([ 0.01538])

  names.append("LHipRoll")
  times.append([ 1.00000])
  keys.append([ -0.00456])

  names.append("LHipPitch")
  times.append([ 1.00000])
  keys.append([ -0.90962])

  names.append("LKneePitch")
  times.append([ 1.00000])
  keys.append([ 2.11255])

  names.append("LAnklePitch")
  times.append([ 1.00000])
  keys.append([ -1.18889])

  names.append("LAnkleRoll")
  times.append([ 1.00000])
  keys.append([ 0.00464])

  names.append("RHipRoll")
  times.append([ 1.00000])
  keys.append([ 0.10589])

  names.append("RHipPitch")
  times.append([ 1.00000])
  keys.append([ -0.90203])

  names.append("RKneePitch")
  times.append([ 1.00000])
  keys.append([ 2.11255])

  names.append("RAnklePitch")
  times.append([ 1.00000])
  keys.append([ -1.18630])

  names.append("RAnkleRoll")
  times.append([ 1.00000])
  keys.append([ -0.10427])

  proxy.angleInterpolation(names, keys, times, True)


def stand():
    Head     = [+0, +90]

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

def standup():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step1(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step2(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step3(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step4(), 0.2)
    proxy.angleInterpolationWithSpeed(pNames, step5(), 0.3)
    proxy.angleInterpolationWithSpeed(pNames, step6(), 0.2)
    proxy.angleInterpolationWithSpeed(pNames, step7(), 0.2)
    proxy.angleInterpolationWithSpeed(pNames, stand(), 0.2)