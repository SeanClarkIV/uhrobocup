import kalmanthreaded
import config
import kick
import stand
import track
import walk
import dive
import goalie
import mapping
import kalmanfilter
import sudoarchitecture
import objectrecognition
motionProxy = config.loadProxy("ALMotion")
texttospeechProxy = config.loadProxy("ALTextToSpeech")
def main():
    def menu():
        #print what options you have
        print "\n*** OPTIONS ***"
        print "0) Quit           5) Right Kick       10) Walk Left         15) Stand Up from Sit      20) R to S       25)Goalie"
        print "1) Stiffness ON   6) Walk Foward      11) Walk Right        16) Find Red Ball L to R   21) R to L       26) Map"
        print "2) Stiffness OFF  7) Walk Backwards   12) stand up on back  17) Find Red Ball L to S   22) Stop Tracker 27) Kalman Filter"
        print "3) Goalie Pose    8) Turn Left        13) stand up on front 18) Find Red Ball L to L   23) Dive Left    28) Goalie intercepts clockwise"
        print "4) Left Kick      9) Turn Right       14) Sit Down          19) Find Red Ball R to L   24) Dive Right   29) Goalie intercepts counterclockwise"
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
                config.stiffnessOn()
            elif choice[k] == 2:
                config.stiffnessOff()
            elif choice[k] == 3:
                goalie.goaliePose()
            elif choice[k] == 4:
                kick.kickLeftFoot()
            elif choice[k] == 5:
                kick.kickRightFoot()
            elif choice[k] == 6:
                walk.ultimateWalkTo(1, 00, 00)
            elif choice[k] == 7:
                walk.ultimateWalkTo(-1, 00, 00)
            elif choice[k] == 8:
                walk.ultimateWalkTo(0,0,2)
            elif choice[k] == 9:
                walk.ultimateWalkTo(0,0,-2)
            elif choice[k] == 10:
                walk.ultimateWalkTo(0, -1, 0)
            elif choice[k] == 11:
                walk.ultimateWalkTo(0, 1, 0)
            elif choice[k] == 12:
                stand.standUp()
            elif choice[k] == 13:
                stand.standUpOnFront()
            elif choice[k] == 14:
                stand.sitDown()
            elif choice[k] == 15:
                stand.standFromSit()
            elif choice[k] == 16:
                track.findRedBallAndKick(1)
            elif choice[k] == 17:
                track.findRedBallAndKick(2)
            elif choice[k] == 18:
                track.findRedBallAndKick(3)
            elif choice[k] == 19:
                track.findRedBallAndKick(4)
            elif choice[k] == 20:
                track.findRedBallAndKick(5)
            elif choice[k] == 21:
                track.findRedBallAndKick(6)
            elif choice[k] == 22:
                track.stopTracker()
            elif choice[k] == 23:
                dive.diveLeft()
            elif choice[k] == 24:
                dive.diveRight()
            elif choice[k] == 25:
                goalie.goalie()
            elif choice[k] == 26:
                mapping.map()
            elif choice[k] == 27:
                kalmanthreaded.kalman().start()
            elif choice[k] == 28:
                goalie.goalieImproved(1)
            elif choice[k] == 29:
                goalie.goalieImproved(0)
            elif choice[k] == 30:
                kalmanthreaded.stop()
            elif isinstance(choice[k], basestring): #this checks to see if the input is a string.
                texttospeechProxy.say(choice[k])    #if it is a string it will make the nao speak it.
            else:
                #this else statement is used to try out new files that you dont want in the comand menu.
                #just type out what you want it to run.
                #example [kalmanthreaded.get('xposition')]
                choice[k]
            k = k+1
if __name__ == "__main__":
    main()
