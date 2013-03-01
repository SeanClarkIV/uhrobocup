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
from thread import start_new_thread
motionProxy = config.load_proxy("ALMotion")
texttospeechProxy = config.load_proxy("ALTextToSpeech")
def main():
    def menu():
        #print what options you have
        print "\n*** OPTIONS ***"
        print "0) Quit                  5) Right Kick         10) Walk Left         15) Stand Up from Sit      20) R to S       25)Goalie"
        print "1) Turn stiffness ON     6) Walk Foward        11) Walk Right        16) Find Red Ball L to R   21) R to L       26) Map"
        print "2) Turn stiffness OFF    7) Walk Backwards     12) stand up on back  17) Find Red Ball L to S   22) Stop Tracker 27) Kalman Filter"
        print "3) goalie Pose          8) Turn Left          13) stand up on front 18) Find Red Ball L to L   23) Dive Left     28) Goalie intercepts clockwise"
        print "4) Left Kick             9) Turn Right         14) Sit Down          19) Find Red Ball R to L   24) Dive Right   29) Goalie intercepts counterclockwise"
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
                config.stiffness_on()
            elif choice[k] == 2:
                config.stiffness_off()
            elif choice[k] == 3:
                goalie.goalie_pose()
            elif choice[k] == 4:
                kick.kick_left_foot()
            elif choice[k] == 5:
                kick.kick_right_foot()
            elif choice[k] == 6:
                walk.ultimate_walk_to(1, 00, 00)
            elif choice[k] == 7:
                walk.ultimate_walk_to(-1, 00, 00)
            elif choice[k] == 8:
                walk.ultimate_walk_to(0,0,2)
            elif choice[k] == 9:
                walk.ultimate_walk_to(0,0,-2)
            elif choice[k] == 10:
                walk.ultimate_walk_to(0, -1, 0)
            elif choice[k] == 11:
                walk.ultimate_walk_to(0, 1, 0)
            elif choice[k] == 12:
                stand.stand_up()
            elif choice[k] == 13:
                stand.stand_up_on_front()
            elif choice[k] == 14:
                stand.sit_down()
            elif choice[k] == 15:
                stand.stand_from_sit()
            elif choice[k] == 16:
                track.find_red_ball_and_kick(1)
            elif choice[k] == 17:
                track.find_red_ball_and_kick(2)
            elif choice[k] == 18:
                track.find_red_ball_and_kick(3)
            elif choice[k] == 19:
                track.find_red_ball_and_kick(4)
            elif choice[k] == 20:
                track.find_red_ball_and_kick(5)
            elif choice[k] == 21:
                track.find_red_ball_and_kick(6)
            elif choice[k] == 22:
                track.stop_tracker()
            elif choice[k] == 23:
                dive.dive_left()
            elif choice[k] == 24:
                dive.dive_right()
            elif choice[k] == 25:
                goalie.goalie()
            elif choice[k] == 26:
                mapping.map()
            elif choice[k] == 27:
                kalmanthreaded.kalman().start()
            elif choice[k] == 28:
                goalie.goalie_improved(1)
            elif choice[k] == 29:
                goalie.goalie_improved(0)
            elif choice[k] == 30:
                kalmanthreaded.stop()
            else:
                texttospeechProxy.say(choice[k])
            k = k+1
if __name__ == "__main__":
    main()
