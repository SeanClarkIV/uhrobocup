import config
import kick
import stand
import track
import walk

motionProxy = config.loadProxy("ALMotion")
texttospeechProxy = config.loadProxy("ALTextToSpeech")

def main():
    def menu():
        #print what options you have
        print "\n*** OPTIONS ***"
        print "0) Quit                  4) Left Kick         8) Turn Left                12) Find Red Ball"
        print "1) Turn stiffness ON     5) Right Kick        9) Turn Right               13) Super Speed"
        print "2) Turn stiffness OFF    6) Walk Foward      10) stand up on back         14) Sit Down"
        print "3) Initial Pose          7) Walk Backwards   11) stand up on front        15)Stand Up from Sit"
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
                config.StiffnessOn(motionProxy)
            elif choice[k] == 2:
                config.StiffnessOff(motionProxy)
            elif choice[k] == 3:
                config.PoseInit(motionProxy, 0.5)
            elif choice[k] == 4:
                kick.kickLeftFoot()
            elif choice[k] == 5:
                kick.kickRightFoot()
            elif choice[k] == 6:
                walk.walkFowardTimed(5)
            elif choice[k] == 7:
                walk.ultimatewalkto(-1,.25,.2)
            elif choice[k] == 8:
                walk.ultimatewalkto(0,0,2)
            elif choice[k] == 9:
                walk.ultimatewalkto(0,0,-2)
            elif choice[k] == 10:
                stand.standup()
            elif choice[k] == 11:
                stand.standuponfront()
            elif choice[k] == 12:
                track.findRedBall()
            elif choice[k] == 13:
                walk.ultimatewalkto(1,0,0)
            elif choice[k] == 14:
                stand.sitdown()
            elif choice[k] == 15:
                stand.standfromsit()
            else:
                texttospeechProxy.say(choice[k])
            k = k+1
if __name__ == "__main__":
    main()
