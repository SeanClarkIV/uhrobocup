import motion
from naoqi import ALProxy

IP = "127.0.0.1" # set your Ip adress here
PORT = 9559
if (IP == ""):
  print "IP address not defined, aborting"
  print "Please define it in " + __file__
  exit(1)

def loadProxy(pName):
  print "---------------------"
  print "Loading proxy"
  print "---------------------"
  proxy = ALProxy(pName, IP, PORT)
  print "---------------------"
  print "Starting " + pName + " Tests"
  print "---------------------"
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
  # Define The Initial Position
  HeadYawAngle       = 0
  HeadPitchAngle     = 0

  ShoulderPitchAngle = 80
  ShoulderRollAngle  = 20
  ElbowYawAngle      = -80
  ElbowRollAngle     = -60
  WristYawAngle      = 0
  HandAngle          = 0

  HipYawPitchAngle   = 0
  HipRollAngle       = 0
  HipPitchAngle      = -20
  KneePitchAngle     = 40
  AnklePitchAngle    = -20
  AnkleRollAngle     = 0

  # Get the Robot Configuration
  robotConfig = proxy.getRobotConfig()
  robotName = ""
  Head     = [HeadYawAngle, HeadPitchAngle]
  LeftArm  = [ShoulderPitchAngle, +ShoulderRollAngle, +ElbowYawAngle, +ElbowRollAngle, WristYawAngle, HandAngle]
  RightArm = [ShoulderPitchAngle, -ShoulderRollAngle, -ElbowYawAngle, -ElbowRollAngle, WristYawAngle, HandAngle]

  LeftLeg  = [HipYawPitchAngle, +HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, +AnkleRollAngle]
  RightLeg = [HipYawPitchAngle, -HipRollAngle, HipPitchAngle, KneePitchAngle, AnklePitchAngle, -AnkleRollAngle]
  # Gather the joints together
  pTargetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm

  # Convert to radians
  pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]

  #------------------------------ send the commands -----------------------------
  # We use the "Body" name to signify the collection of all joints
  pNames = "Body"
  # Ask motion to do this with a blocking call
  proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)

def poseZero(proxy):
  # We use the "Body" name to signify the collection of all joints and actuators
  pNames = "Body"

  # Get the Number of Joints
  numBodies = len(proxy.getJointNames(pNames))

  # We prepare a collection of floats
  pTargetAngles = [0.0] * numBodies

  # We set the fraction of max speed
  pMaxSpeedFraction = 0.3

  # Ask motion to do this with a blocking call
  proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)
