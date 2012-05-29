import config
import kick
from naoqi import ALProxy
import walk

# Common Variables
proxy = config.loadProxy("ALMotion")
tts = ALProxy("ALTextToSpeech", config.IP, 9559)

def main():
    def menu():
        #print what options you have
        print "\n*** OPTIONS ***"
        print "0) Quit"
        print "1) Turn stiffness ON"
        print "2) Turn stiffness OFF"
        print "3) Initial Pose"
        print "4) Left Kick"
        print "5) Right Kick"
        print "6) Walk"
        return input ("\nChoose your option: ")

    # NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
    loop = 1
    choice = 0
    while loop == 1:
        choice = menu()
        if choice == 0:
            loop = 0
        elif choice == 1:
            config.StiffnessOn(proxy)
        elif choice == 2:
            config.StiffnessOff(proxy)
        elif choice == 3:
            config.PoseInit(proxy, 0.5)
        elif choice == 4:
            kick.kickLeftFoot()
        elif choice == 5:
            kick.kickRightFoot()
        elif choice == 6:
            walk.walkTimed(5)

if __name__ == "__main__":
    main()