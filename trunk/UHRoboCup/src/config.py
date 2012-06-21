import motion
from naoqi import ALProxy

IP = "169.254.229.195" # set your Ip adress here
PORT = 9559
if (IP == ""):
  print "IP address not defined, aborting"
  print "Please define it in " + __file__
  exit(1)

def loadProxy(proxyName):
  print "----- Loading " + proxyName + " -----"
  proxy = ALProxy(proxyName, IP, PORT)
  return proxy

def StiffnessOn(proxy):
  #We use the "Body" name to signify the collection of all joints
  pNames = "Body"
  pStiffnessLists = 1.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
  proxy.setSmartStiffnessEnabled(True)
  smartstiffness = proxy.getSmartStiffnessEnabled()
  if smartstiffness == True:
      print "Smart Stiffness Enabled"
  else:
      print "Smart Stiffness NOT Enabled"

def StiffnessOff(proxy):
 #We use the "Body" name to signify the collection of all joints
  pNames = "Body"
  pStiffnessLists = 0.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
  proxy.setSmartStiffnessEnabled(False)
  smartstiffness = proxy.getSmartStiffnessEnabled()
  if smartstiffness == False:
      print "Smart Stiffness Disabled"
  else:
      print "Smart Stiffness NOT Disabled"

def PoseInit(proxy, pMaxSpeedFraction = 0.2):
    StiffnessOff(proxy)
    Head     = [+0, +0]

    LeftArm  = [+80, +20, -80, -60, +0, +0]
    RightArm = [+80, -20, +80, +60, +0, +0]

    LeftLeg  = [+0, +0, -20, +40, -20, +0]
    RightLeg = [+0, +0, -20, +40, -20, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]

    proxy.angleInterpolationWithSpeed("Body", pTargetAngles, pMaxSpeedFraction)