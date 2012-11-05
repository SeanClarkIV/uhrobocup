import localization
import config
import kick
import stand
import track
import walk
import kickinair
import dive
import goalie
import mapping
motionProxy = config.loadProxy("ALMotion")
texttospeechProxy = config.loadProxy("ALTextToSpeech")
def main():
    def menu():
        #print what options you have
        print "\n*** OPTIONS ***"
        print "0) Quit                  5) Right Kick         10) Walk Left         15) Stand Up from Sit      20) R to S       25)Dive Right"
        print "1) Turn stiffness ON     6) Walk Foward        11) Walk Right        16) Find Red Ball L to R   21) R to L       26) Goalie"
        print "2) Turn stiffness OFF    7) Walk Backwards     12) stand up on back  17) Find Red Ball L to S   22) Stop Tracker 27) Map"
        print "3) goalie Pose          8) Turn Left          13) stand up on front 18) Find Red Ball L to L   23) Kick in air"
        print "4) Left Kick             9) Turn Right         14) Sit Down          19) Find Red Ball R to L   24) Dive Left"
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
                config.StiffnessOn()
            elif choice[k] == 2:
                config.StiffnessOff()
            elif choice[k] == 3:
                goalie.goaliepose()
            elif choice[k] == 4:
                kick.kickLeftFoot()
            elif choice[k] == 5:
                kick.kickRightFoot()
            elif choice[k] == 6:
                walk.ultimatewalkto(1, 00, 00)
            elif choice[k] == 7:
                walk.ultimatewalkto(-1, 00, 00)
            elif choice[k] == 8:
                walk.ultimatewalkto(0,0,2)
            elif choice[k] == 9:
                walk.ultimatewalkto(0,0,-2)
            elif choice[k] == 10:
                walk.ultimatewalkto(0, -1, 0)
            elif choice[k] == 11:
                walk.ultimatewalkto(0, 1, 0)
            elif choice[k] == 12:
                stand.standup()
            elif choice[k] == 13:
                stand.standuponfront()
            elif choice[k] == 14:
                stand.sitdown()
            elif choice[k] == 15:
                stand.standfromsit()
            elif choice[k] == 16:
                track.findRedBall(1)
            elif choice[k] == 17:
                track.findRedBall(2)
            elif choice[k] == 18:
                track.findRedBall(3)
            elif choice[k] == 19:
                track.findRedBall(4)
            elif choice[k] == 20:
                track.findRedBall(5)
            elif choice[k] == 21:
                track.findRedBall(6)
            elif choice[k] == 22:
                track.stoptracker()
            elif choice[k] == 23:
                kickinair.kickinair1()
            elif choice[k] == 24:
                dive.diveleft()
            elif choice[k] == 25:
                dive.diveright()
            elif choice[k] == 26:
                goalie.goalie()
            elif choice[k] == 27:
                mapping.map()
            elif choice[k] == 28:
                localization.getvelocity()
            else:
                texttospeechProxy.say(choice[k])
            k = k+1
if __name__ == "__main__":
    '''fx = open('naoX.txt','w+')
    fy = open('naoY.txt','w+')
    if fx.read() == '':   #This is to start working on storing location of nao in a txt file
        naoX = 100
        naoY = 270
        fx.write('100')
        fy.write('270')'''
    main()
