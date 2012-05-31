import config
import kick
import stand
from naoqi import ALProxy
import walk

# Common Variables
proxy = config.loadProxy("ALMotion")
tts = ALProxy("ALTextToSpeech", config.IP, 9559)

def main():
    def menu():
        #print what options you have
        print "\n*** OPTIONS ***"
        print "0) Quit               4) Left Kick         8) Turn Left"
        print "1) Turn stiffness ON  5) Right Kick        9) Turn Right"
        print "2) Turn stiffness OFF 6) Walk Foward       10) stand up on back"
        print "3) Initial Pose       7) Walk Backwards    11) stand up on front"
        print "type what you want him to say in quotations"
        return input ("\nChoose your option(s) as list: ")

    # NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
    loop = 1
    choice = 0
    while loop == 1:
        choice = menu()
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
                walk.turnleft()
            elif choice[k] == 9:
                walk.turnright()
            elif choice[k] == 10:
                stand.standuponback()
            elif choice[k] == 11:
                stand.standuponfront()
            else:
                tts.say(choice[k])
            k = k+1
if __name__ == "__main__":
    main()