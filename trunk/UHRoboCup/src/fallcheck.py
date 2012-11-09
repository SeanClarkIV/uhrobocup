import config
import stand
motionProxy = config.load_proxy("ALMotion")

def handle_fall():
    proxy = config.load_proxy("ALRobotPose")
    temp = proxy.getActualPoseAndTime()
    pose = temp[0]
    print "\n" + pose
    if pose == "Belly": #Checks to see if he is on his belly or back.
        stand.stand_upon_front()
    elif pose == "Back":
        stand.stand_up()
    else:
        stand.stand_up()
        config.pose_init()
    print "Fall handled"

def check_fall():
    memoryProxy = config.load_proxy("ALMemory")
    onfeet = True
    onfeet = memoryProxy.getData("footContact") #Checks to see if there is any footcontact.
    if not onfeet: #If there is no contact then it runs the code that picks a stand up. 
        print "fall detected"
        handle_fall()