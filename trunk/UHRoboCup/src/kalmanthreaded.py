# Included in Python
import threading
import math

# Need to get from online
import numpy
from matplotlib import pyplot

# local classes
import track
import config

motionProxy = config.load_proxy("ALMotion")
redballtracker = config.load_proxy("ALRedBallTracker")
texttospeechProxy = config.load_proxy("ALTextToSpeech")
kalmanstop=threading.Event() #creates events so that we can stop it later
trackstop=threading.Event()
def stop():
    trackstop.set()#sets a flag that stops this if its looking for the ball
    kalmanstop.set()#sets the flag to stop the kalman filter
class kalman(threading.Thread):
    def run(self):
        kalmanstop.clear() #clears the flag that seting the event does.
        trackstop.clear()
        #initializing the vectors that store the variables.
        xvelocity = [0]
        yvelocity = [0]
        T  = [0] #Time elapsed
        xsensed=[1]
        ysensed=[0]
        xkalman=[1]
        ykalman=[1]

        #setting the constants
        t=0.01; #change in time
        r=1;
        r1=1;
        G  = numpy.matrix([[math.pow(t,2)/2],[math.pow(t,2)/2],[t],[t]])
        A  = numpy.matrix([[1,0,t,0],[0,1,0,t],[0,0,1,0],[0,0,0,1]])
        R = numpy.matrix('1,0;0,1')*math.pow(r,2);
        H= numpy.matrix('1,0,0,0;0,1,0,0')
        Q = G*numpy.transpose(G)*math.pow(r1,2)
        Pk_1 = numpy.matrix([[10,0,0,0],[0,10,0,0],[0,0,10,0],[0,0,0,10]]);
        xhk_1=numpy.matrix([[1],[0],[1],[2]]);


        #setting initial conditions
        xb=0.1
        yb=0.1
        aj=0  #the time in loop
        k=1
        iterations=500 #the number of iterations you want
        #now we look for and find the ball
        redballposition=track.find_red_ball(trackstop)
        redballtracker.startTracker() #you have to start the tracker after using the find_red_ball function
        while(not kalmanstop.is_set()):
            redballposition=redballtracker.getPosition();
            zk= H*numpy.matrix([[redballposition[0]],[redballposition[1]],[xb],[yb]]) ;
            xhbk =  A*xhk_1
            Pbk = A * Pk_1 * numpy.transpose(A) + Q;

            Kk = Pbk*numpy.transpose(H)*numpy.linalg.inv((H * Pbk * numpy.transpose(H)) + R);
            xhk = xhbk + Kk*(zk-H*xhbk);
            #print xhk[0][0] #prints the kalman estimate of the x position
            Pk = (numpy.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) - Kk*H)*Pbk;
            Pk_1=Pk;
            xhk_1=xhk;
            xb=xhk[2][0] #updates the x velocity
            yb=xhk[3][0] #updates the y velocity

            xvelocity.append(xb)
            yvelocity.append(yb)

            xsensed.append(zk[0][0])
            ysensed.append(zk[1][0])

            xkalman.append(xhk[0][0])
            ykalman.append(xhk[1][0])
            aj=aj+t
            T.append(aj)

            k=k+1;
        redballtracker.stopTracker()
        kalmanstop.clear()
        trackstop.clear()
        print 'done'