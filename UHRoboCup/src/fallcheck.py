import config
import stand
motionProxy = config.loadProxy("ALMotion")

def handleFall():
    proxy = config.loadProxy("ALRobotPose")
    temp = proxy.getActualPoseAndTime()
    pose = temp[0]
    print "\n" + pose
    if pose == "Belly": #Checks to see if he is on his belly or back.
        stand.stand_upon_front()
    elif pose == "Back":
        stand.standUp()
    else:
        stand.standUp()
        config.poseInit()
    print "Fall handled"

def checkFall():
    memoryProxy = config.loadProxy("ALMemory")
    onfeet = True
    onfeet = memoryProxy.getData("footContact") #Checks to see if there is any footcontact.
    if not onfeet: #If there is no contact then it runs the code that picks a stand up. 
        print "fall detected"
        handleFall()