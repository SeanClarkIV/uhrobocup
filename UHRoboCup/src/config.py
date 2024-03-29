from naoqi import motion
from naoqi import ALProxy

IP = "127.0.0.1" # Robot IP Adress to establish connection.

PORT = 9559

if (IP == ""):
    print "IP Address is blank, or not defined in", __file__
    exit("FUNCTION ABORTED - No IP address defined.")

def loadProxy(proxyName):
  print "----- Loading " + proxyName + " -----"
  proxy = ALProxy(proxyName, IP, PORT)
  return proxy

motionProxy = ALProxy("ALMotion", IP, PORT)
videoProxy = ALProxy("ALVideoDevice", IP, PORT)
speechProxy = ALProxy("ALTextToSpeech", IP, PORT)

def stiffnessOn():
    pNames = "Body"       # Body is used for collection of all joints.
    pStiffnessLists = 1.0 # Maximum stiffness.
    pTimeLists = 1.0
    motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

    # Smart stiffness Enabled in order to conserve motor's power.
    motionProxy.setSmartStiffnessEnabled(True)
    smartstiffness = motionProxy.getSmartStiffnessEnabled()
    if smartstiffness == True:
        print "Smart Stiffness Enabled"
    else:
        print "Smart Stiffness NOT Enabled"

def stiffnessOff(pNames = "Body"):# Body is used for collection of all joints.
             
    pStiffnessLists = 0.0   # No stiffness.
    pTimeLists = 1.0
    motionProxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

    # Smart stiffness Disabled in order to turn off motor's power.
    motionProxy.setSmartStiffnessEnabled(False)
    smartstiffness = motionProxy.getSmartStiffnessEnabled()
    if smartstiffness == False:
        print "Smart Stiffness Disabled"
    else:
        print "Smart Stiffness NOT Disabled"

def poseInit():
    stiffnessOn()

    Head     = [+0, +0]

    LeftArm  = [+80, +20, -80, -60, +0, +0]
    RightArm = [+80, -20, +80, +60, +0, +0]

    LeftLeg  = [+0, +0, -20, +40, -20, +0]
    RightLeg = [+0, +0, -20, +40, -20, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]

    motionProxy.angleInterpolationWithSpeed("Body", pTargetAngles, 0.3)
