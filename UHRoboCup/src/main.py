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
        print "6) Walk Fowards"
        print "7) Walk Backwards"
        print "8) Turn Left 90 degrees"
        print "9) Turn Right 90 degrees"
        print "type what you want him to say in quotations"
        return input ("\nChoose your option(s) as list: ")

    # NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
    loop = 1
    choice = 0
    while loop == 1:
        choice = menu()
        if len(choice) == 1:
            if choice[0] == 0:
                loop = 0
            elif choice[0] == 1:
                config.StiffnessOn(proxy)
            elif choice[0] == 2:
                config.StiffnessOff(proxy)
            elif choice[0] == 3:
                config.PoseInit(proxy, 0.5)
            elif choice[0] == 4:
                kick.kickLeftFoot()
            elif choice[0] == 5:
                kick.kickRightFoot()
            elif choice[0] == 6:
                walk.walkFowardTimed(5)
            elif choice[0] == 7:
                walk.walkBackTimed(5)
            elif choice[0] == 8:
                walk.turnleft()
            elif choice[0] == 9:
                walk.turnright()
            else:
                tts.say(choice[0])
        if len(choice) >1:
            k=0
            while k < len(choice):
                if choice[k] == 0:
                    loop = 0
                    break
                elif choice[k] == 1:
                    config.StiffnessOn(proxy)
                elif choice[k] == 2:
                    config.StiffnessOff(proxy)
                elif choice[k] == 3:
                    config.PoseInit(proxy, 0.5)
                elif choice[k] == 4:
                    kick.kickLeftFoot()
                elif choice[k] == 5:
                    kick.kickRightFoot()
                elif choice[k] == 6:
                    walk.walkFowardTimed(5)
                elif choice[k] == 7:
                    walk.walkBackTimed(5)
                elif choice[k] == 8:
                    walk.turnLeft()
                elif choice[k] == 9:
                    walk.turnright()
                else:
                    tts.say(choice[k])
                k = k+1
if __name__ == "__main__":
    main()