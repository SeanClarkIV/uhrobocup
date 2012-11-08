import math
import config
import numpy
import random
from matplotlib import pyplot
import camera
import time
motionProxy = config.loadProxy("ALMotion")
redballtracker = config.loadProxy("ALRedBallTracker")
def kalman_filter():
    # Set stiffnes ON
    config.StiffnessOn()

    #Make sure top camera is active
    camera.topCamera()

    # Start looking for red ball to track.
    redballtracker.stopTracker()
    redballtracker.startTracker()
    redballtracker.setWholeBodyOn(True)
    print "Tracking red ball"

    #Store initial red ball positon to variable
    initialredballposition = redballtracker.getPosition()
    print "Initial Position: ", initialredballposition
    cameras = 0 #Top camera
    count = 0
    counter = 0 #Used for Redballposition
    times = 0
    headpitchangle = 1.433
    while redballtracker.getPosition() == initialredballposition:  # Ball lost.
        if redballtracker.isNewData() == False and count == 0: # Ball still lost.true if a new Red Ball was detected since the last getPosition().
            print "Looking for red ball"
            camera.topCamera()
            motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, headpitchangle], 0.07)
            time.sleep(3)
            count = 1
            cameras = 0 # top camera
            times += 1
        elif redballtracker.isNewData() == False and count == 1:
            camera.bottomCamera()
            motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, headpitchangle], 0.07)
            time.sleep(3)
            count = 0
            cameras = 1 # bottom camera
            times += 1
        # the next if condition is to look up slightly if he can't find the ball and then when it looks up 3 times
        # it decides turns left and starts all over again.
        if times > 1:
            number = float(times)
            if number % 2 == 1:
                if headpitchangle < 0:
                    headpitchangle = 1.433
                    walk.ultimatewalkto(0, 0, 2)
                elif headpitchangle > .5:
                    headpitchangle = .2
                else:
                    headpitchangle = headpitchangle - 0.2
                print headpitchangle
            else:
                pass
    print "found red ball"

    t=0.01;
    a = -0.20;

    G  = numpy.matrix([[math.pow(t,2)/2],[math.pow(t,2)/2],[t],[t]])
    A  = numpy.matrix([[1,0,t,0],[0,1,0,t],[0,0,1,0],[0,0,0,1]])
    xb = [10]
    yb = [20]
    y  = [0]
    x  = [0]
    T  = [0]
    
    xb=0.1
    yb=0.1
    r=1;
    r1=1;

    R = numpy.matrix('1,0;0,1')*math.pow(r,2);
    H= numpy.matrix('1,0,0,0;0,1,0,0')

    Q = G*numpy.transpose(G)*math.pow(r1,2)

    Pk_1 = numpy.matrix([[1000,0,0,0],[0,1000,0,0],[0,0,1000,0],[0,0,0,1000]]);

    xhk_1=numpy.matrix([[1],[0],[1],[2]]);
   

    z1=[1]
    z2=[0]
    xpre=[1]
    ypre=[1]
    xb1=[0]
    yb1=[0]
    aj=0

    ##xh=x
    ##xh[0]=numpy.matrix('0;0;100;200')

    ##redballposition=redballtracker.getPosition()
    k=1
    Vx=0
    Vy=0
    xi=0
    yi=0
    #while math.fabs(xb)>0.00005 and math.fabs(yb)>0.00005:
    ni=100
    #while k<ni:
    while k<500:
        ##print "in kalman"
        ##print math.fabs(xb)
        ##print yb ##math.fabs(yb)
        redballposition=redballtracker.getPosition()
        zk= H*numpy.matrix([[redballposition[0]],[redballposition[1]],[xb],[yb]]) ;
        xhbk =  A*xhk_1
        Pbk = A * Pk_1 * numpy.transpose(A) + Q;
        
        Kk = Pbk*numpy.transpose(H)*numpy.linalg.inv((H * Pbk * numpy.transpose(H)) + R)
        xhk = xhbk + Kk*(zk-H*xhbk);
        print xhk[0][0]
        Pk = (numpy.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) - Kk*H)*Pbk;
        Pk_1=Pk
        xhk_1=xhk
        xb=xhk[2][0]
        yb=xhk[3][0]


        
        xb1.append(xb)
        yb1.append(yb)

        z1.append(zk[0][0])
        z2.append(zk[1][0])

        xpre.append(xhk[0][0])
        ypre.append(xhk[1][0])
        aj=aj+t
        T.append(aj)

        k=k+1
        xi=xhk[0][0]
        yi=xhk[1][0]
    pyplot.plot(T,z2,'r',T,ypre,'g',T,yb1,'b--')
    pyplot.legend(('Sensed Position', 'Kalman Estimate', 'Velocity'))
    pyplot.xlabel('Itterations')
    pyplot.ylabel('value')
    pyplot.show()

        #if k>5000:
        #    break

    '''xf=[xi]
    yf=[yi]
    dt=0
    Ti  = [0]
    aji=0
    xj=0
    yj=0
    while 1:
        dt=dt+t
        aji=aji+t
        Ti.append(aji)
        xj=xi+xb*dt
        yj=yi+yb*dt
        xf.append(xj)
        yf.append(yj)
        #print xj

        if xj<0:
            print "stopping iteration"
            break

    print yj*0.76
    return xj


    #pyplot.plot(Ti,yf,'r',Ti,xf,'b--')
    #pyplot.show()'''

